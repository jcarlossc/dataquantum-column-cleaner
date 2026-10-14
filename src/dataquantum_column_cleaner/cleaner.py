"""Utilities for cleaning and standardizing DataFrame column names."""

import re

import pandas as pd


def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """Standardize column names and ensure their uniqueness.

    The function converts names to lowercase, replaces whitespace and
    hyphens with underscores, removes unsupported characters, and adds
    numeric suffixes when normalized names collide.

    The original DataFrame is not modified.

    Args:
        df: DataFrame whose column names should be standardized.

    Returns:
        A copy of the DataFrame with unique, standardized column names.
    """

    # Creates a copy of the original DataFrame.
    result = df.copy()

    # Creates an empty list to store the cleaned column names.
    cleaned_names: list[str] = []

    # Creates a set to store names that have already been 
    # used and avoid duplicates.
    used_names: set[str] = set()

    for column in result.columns:
        # Converts the name to text, removes leading and trailing spaces, 
        # and converts letters to lowercase.
        name = str(column).strip().lower()

        # Normalize whitespace and hyphens.
        name = re.sub(r"[\s-]+", "_", name)

        # Remove characters other than word characters and underscores.
        name = re.sub(r"[^\w]", "", name)

        # Remove leading and trailing underscores.
        name = name.strip("_")

        # Uses `name` if it is not empty; otherwise, 
        # uses "column" as the default name.
        base_name = name or "column"

        # Defines the initial column name.
        unique_name = base_name

        # Initializes the counter used to generate numeric suffixes.
        counter = 1

        # Find a name that has not been used.
        while unique_name in used_names:
            # adds a numeric suffix to the name, such as sales_1.
            unique_name = f"{base_name}_{counter}"

            # Increments the counter by 1 to try another suffix, if necessary.
            counter += 1

        # Adds the final name to the list of cleaned names.
        cleaned_names.append(unique_name)

        # Registers the name in the set of names already used.
        used_names.add(unique_name)

    # Replaces the column names of the copy with clean, unique names.
    result.columns = cleaned_names

    return result
