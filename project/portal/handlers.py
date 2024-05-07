from collections import Counter

import pandas as pd
from django.db.models import Model

from .models import Bill, Legislator, Vote, VoteResult

DEFAULT_IMPORTABLE_TABLES = [Legislator, Bill, Vote, VoteResult]


# TODO: move to a service class.
def handle_input_file(bytes_data: bytes) -> tuple[bool, dict | None, Model | None]:
    df = pd.read_csv(bytes_data)
    column_names = df.columns.tolist()

    for model in DEFAULT_IMPORTABLE_TABLES:
        model_fields = [f.name for f in model._meta.fields]

        if lists_have_same_elements(column_names, model_fields):
            records = df.to_dict(orient="records")

            legislator_field = [
                col for col in ["legislator_id", "sponsor_id"] if col in column_names
            ]
            bill_field = "bill_id" if "bill_id" in column_names else None
            vote_field = "vote_id" if "vote_id" in column_names else None

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

                rec_copy = rec.copy()
                id_field = rec_copy.pop("id")
                model.objects.update_or_create(id=id_field, defaults=rec_copy)
            return True, model, records
    return False, None, None


def lists_have_same_elements(list1: list[str], list2: list[str]) -> bool:
    return Counter(list1) == Counter(list2)
