import pandas as pd
import tempfile
from io import StringIO, BytesIO
from pathlib import Path
from .models import Legislator, Bill, Vote, VoteResult
from collections import Counter


DEFAULT_IMPORTABLE_TABLES = [Legislator, Bill, Vote, VoteResult]


def file_input_handler(bytes_data: bytes) -> bool:
    df = pd.read_csv(bytes_data)
    column_names = df.columns.tolist()

    for model in DEFAULT_IMPORTABLE_TABLES:
        model_fields = [f.name for f in model._meta.fields]

        if lists_have_same_elements(column_names, model_fields):
            records = df.to_dict(orient='records')
            
            legislator_field = [
                col for col in ['legislator_id', 'sponsor_id']
                if col in column_names
            ]
            bill_field = 'bill_id' if 'bill_id' in column_names else None
            vote_field = 'vote_id' if 'vote_id' in column_names else None

            for rec in records:
                if legislator_field:
                    legislator_id = rec.get(legislator_field[0])
                    legislator, _ = Legislator.objects.get_or_create(id=legislator_id)
                    rec[legislator_field[0]] = legislator

                if bill_field:
                    bill_id = rec.get(bill_field)
                    bill, _ = Bill.objects.get_or_create(id=bill_id)
                    rec[bill_field] = bill

                if vote_field:
                    vote_id = rec.get(vote_field)
                    vote, _ = Vote.objects.get_or_create(id=vote_id)
                    rec[vote_field] = vote
                
                id_field = rec.pop('id')
                model.objects.update_or_create(id=id_field, defaults=rec)
            return True
    return False

def lists_have_same_elements(list1: list[str], list2: list[str]) -> bool:
    return Counter(list1) == Counter(list2)
