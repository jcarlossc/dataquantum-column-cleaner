"""Utilities for cleaning and standardizing DataFrame column names."""

import re
import unicodedata

import pandas as pd


def clean_column_names(
    df: pd.DataFrame,
    remove_accents: bool = True,
) -> pd.DataFrame:
    """Standardize DataFrame column names and ensure uniqueness.

    Names are converted to lowercase, whitespace and hyphens are replaced
    with underscores, unsupported characters are removed, and numeric
    suffixes are added when normalized names collide.

    Accent removal is enabled by default and can be disabled.

    The original DataFrame is not modified.

    Args:
        df: DataFrame whose column names should be standardized.
        remove_accents: Whether to remove accents from column names.
            Defaults to True.

    Returns:
        A copy of the DataFrame with unique, standardized column names.

    Raises:
        TypeError: If df is not a pandas DataFrame.
        TypeError: If remove_accents is not a boolean.
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("df must be a pandas DataFrame.")

    if not isinstance(remove_accents, bool):
        raise TypeError("remove_accents must be a boolean.")

    result = df.copy()
    cleaned_names: list[str] = []
    used_names: set[str] = set()

    for column in result.columns:
        name = str(column).strip().lower()

        # Remove accents when requested.
        if remove_accents:
            name = unicodedata.normalize("NFKD", name)
            name = "".join(
                character for character in name if not unicodedata.combining(character)
            )

        # Normalize whitespace and hyphens.
        name = re.sub(r"[\s-]+", "_", name)

        # Remove unsupported characters.
        name = re.sub(r"[^\w]", "", name)

        # Remove leading and trailing underscores.
        name = name.strip("_")

        # Use a fallback for empty names.
        base_name = name or "column"
        unique_name = base_name
        counter = 1

        # Ensure that each name is unique.
        while unique_name in used_names:
            unique_name = f"{base_name}_{counter}"
            counter += 1

        cleaned_names.append(unique_name)
        used_names.add(unique_name)

    result.columns = cleaned_names

    return result
