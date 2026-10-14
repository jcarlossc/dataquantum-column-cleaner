
"""Tests for the column-cleaning utilities."""

import pandas as pd
from pandas.testing import assert_frame_equal

from dataquantum_column_cleaner.cleaner import clean_column_names


def test_standardizes_column_names() -> None:
    """Normalize case, whitespace, and hyphens."""
    df = pd.DataFrame(
        [[1, 2, 3]],
        columns=["Total Vendas", "total-vendas", " TOTAL   VENDAS "],
    )

    result = clean_column_names(df)

    assert result.columns.tolist() == [
        "total_vendas",
        "total_vendas_1",
        "total_vendas_2",
    ]


def test_preserves_original_dataframe() -> None:
    """Keep the original column names unchanged."""
    df = pd.DataFrame({" Total Vendas ": [100]})

    result = clean_column_names(df)

    assert df.columns.tolist() == [" Total Vendas "]
    assert result.columns.tolist() == ["total_vendas"]


def test_handles_empty_column_names() -> None:
    """Generate a fallback name for empty column labels."""
    df = pd.DataFrame([[1, 2]], columns=["", "!!!"])

    result = clean_column_names(df)

    assert result.columns.tolist() == ["column", "column_1"]


def test_handles_existing_numeric_suffixes() -> None:
    """Avoid collisions with names that already have suffixes."""
    df = pd.DataFrame(
        [[1, 2, 3]],
        columns=["Total Vendas", "Total Vendas", "total_vendas_1"],
    )

    result = clean_column_names(df)

    assert result.columns.tolist() == [
        "total_vendas",
        "total_vendas_1",
        "total_vendas_1_1",
    ]


def test_empty_dataframe() -> None:
    """Handle a DataFrame without columns."""
    df = pd.DataFrame()

    result = clean_column_names(df)

    assert result.empty
    assert len(result.columns) == 0
