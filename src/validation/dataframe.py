def check_uniqueness(df):
    unique_columns = {col: df[col].is_unique for col in df.columns}
    for col, is_unique in unique_columns.items():
        print(f"{col}: {'Unique' if is_unique else 'Not unique'}")