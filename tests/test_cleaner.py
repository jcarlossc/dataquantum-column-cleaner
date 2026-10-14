"""Tests for the column-cleaning utilities."""

import pandas as pd
import pytest

from dataquantum_column_cleaner import clean_column_names


def test_removes_accents_by_default() -> None:
    """Remove accents by default."""
    df = pd.DataFrame(columns=["Código", "Preço Médio", "Região"])

    result = clean_column_names(df)

    assert result.columns.tolist() == [
        "codigo",
        "preco_medio",
        "regiao",
    ]


def test_preserves_accents_when_disabled() -> None:
    """Preserve accents when remove_accents is False."""
    df = pd.DataFrame(columns=["Código", "Preço Médio"])

    result = clean_column_names(df, remove_accents=False)

    assert result.columns.tolist() == [
        "código",
        "preço_médio",
    ]


def test_normalizes_spaces_hyphens_and_uppercase() -> None:
    """Normalize uppercase letters, spaces, and hyphens."""
    df = pd.DataFrame(columns=[" Total Vendas ", "PREÇO-MÉDIO"])

    result = clean_column_names(df)

    assert result.columns.tolist() == [
        "total_vendas",
        "preco_medio",
    ]


def test_removes_special_characters() -> None:
    """Remove unsupported special characters."""
    df = pd.DataFrame(columns=["Preço ($)", "Produto@ID"])

    result = clean_column_names(df)

    assert result.columns.tolist() == [
        "preco",
        "produtoid",
    ]


def test_generates_unique_names() -> None:
    """Add numeric suffixes when normalized names collide."""
    df = pd.DataFrame(columns=["Total Vendas", "total-vendas", "TOTAL VENDAS"])

    result = clean_column_names(df)

    assert result.columns.tolist() == [
        "total_vendas",
        "total_vendas_1",
        "total_vendas_2",
    ]


def test_handles_empty_column_names() -> None:
    """Use a fallback name for empty or invalid column names."""
    df = pd.DataFrame(columns=["", "!!!", "   "])

    result = clean_column_names(df)

    assert result.columns.tolist() == [
        "column",
        "column_1",
        "column_2",
    ]


def test_handles_dataframe_without_columns() -> None:
    """Handle a DataFrame without columns."""
    df = pd.DataFrame()

    result = clean_column_names(df)

    assert result.empty
    assert len(result.columns) == 0


def test_does_not_modify_original_dataframe() -> None:
    """Preserve the original DataFrame column names."""
    df = pd.DataFrame(columns=["Preço Médio", "Total Vendas"])
    original_columns = df.columns.copy()

    clean_column_names(df)

    pd.testing.assert_index_equal(df.columns, original_columns)


def test_rejects_non_dataframe() -> None:
    """Raise TypeError when df is not a DataFrame."""
    with pytest.raises(TypeError, match="pandas DataFrame"):
        clean_column_names(["Preço"])  # type: ignore[arg-type]


def test_rejects_non_boolean_remove_accents() -> None:
    """Raise TypeError when remove_accents is not a boolean."""
    df = pd.DataFrame(columns=["Preço"])

    with pytest.raises(TypeError, match="remove_accents"):
        clean_column_names(df, remove_accents=1)  # type: ignore[arg-type]


def test_preserves_underscores() -> None:
    """Preserve valid underscores in column names."""
    df = pd.DataFrame(columns=["__Total_Vendas__"])

    result = clean_column_names(df)

    assert result.columns.tolist() == ["total_vendas"]
