import re

import pandas as pd


def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:

    result = df.copy()
    cleaned_names: list[str] = []
    used_names: set[str] = set()

    for column in result.columns:
        name = str(column).strip().lower()

        name = re.sub(r"[\s-]+", "_", name)

        name = re.sub(r"[^\w]", "", name)

        name = name.strip("_")

        base_name = name or "column"
        unique_name = base_name
        counter = 1

        while unique_name in used_names:
            unique_name = f"{base_name}_{counter}"
            counter += 1

        cleaned_names.append(unique_name)
        used_names.add(unique_name)

    result.columns = cleaned_names

    return result
