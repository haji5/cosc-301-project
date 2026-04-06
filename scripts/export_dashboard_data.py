import pandas as pd
from config import CLEAN_DATA_PATH, PROCESSED_DIR, VALUE_MAPPINGS

DASHBOARD_PATH = PROCESSED_DIR / "cchs_2022_dashboard.csv"

def export_dashboard_data():
    df = pd.read_csv(CLEAN_DATA_PATH)

    # replace coded columns with readable labels
    for col, mapping in VALUE_MAPPINGS.items():
        if col in df.columns:
            df[col] = df[col].map(mapping).fillna(df[col])

    df.to_csv(DASHBOARD_PATH, index=False)
    print(f"Dashboard-ready file saved to: {DASHBOARD_PATH}")

if __name__ == "__main__":
    export_dashboard_data()