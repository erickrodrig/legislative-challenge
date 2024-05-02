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
        print(column_names)
        print(model_fields)

        if lists_have_same_elements(column_names, model_fields):
            records = df.to_dict(orient='records')
            model.objects.bulk_create([model(**rec) for rec in records])
            return True
    return False

def lists_have_same_elements(list1, list2):
    return Counter(list1) == Counter(list2)
