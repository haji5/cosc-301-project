import pandas as pd
from config import (
    RAW_DATA_PATH,
    CLEAN_DATA_PATH,
    PROCESSED_DIR,
    COLUMN_MAPPING,
    INVALID_CODES,
)

def load_raw_data() -> pd.DataFrame:
    return pd.read_excel(RAW_DATA_PATH)

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    cols_to_keep = [col for col in df.columns if col in COLUMN_MAPPING]
    df = df[cols_to_keep].rename(columns=COLUMN_MAPPING)
    df = df.loc[:, ~df.columns.duplicated()]
    df = df.drop_duplicates().dropna()

    for col in df.columns:
        df = df[~df[col].isin(INVALID_CODES)]

    df = df[df["Household_Income"] > 1].copy()

    df["No_Healthcare_Provider"] = (df["Regular_Healthcare_Provider"] == 5).astype(int)

    df["Sex"] = df["Sex_at_Birth"].map({1: "Male", 2: "Female"})

    return df

def save_clean_data(df: pd.DataFrame) -> None:
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    df.to_csv(CLEAN_DATA_PATH, index=False)

def main() -> None:
    print("Loading raw data...")
    raw_df = load_raw_data()

    print("Cleaning data...")
    clean_df = clean_data(raw_df)

    print("Saving cleaned CSV...")
    save_clean_data(clean_df)

    print(f"Done. Cleaned rows: {len(clean_df)}")
    print(f"Saved to: {CLEAN_DATA_PATH}")

if __name__ == "__main__":
    main()