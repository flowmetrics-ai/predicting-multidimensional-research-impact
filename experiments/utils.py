import ast


def parse_stringified_columns(df, columns_to_parse):
    """
    Converts stringified lists or list of tuples into real Python objects (lists).

    Parameters:
        df: pandas.DataFrame
        columns_to_parse: list of column names to parse

    Returns:
        df: pandas.DataFrame with parsed columns
    """
    for col in columns_to_parse:
        if col in df.columns:
            df[col] = df[col].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) else x)
    return df