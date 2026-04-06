import sqlite3
import pandas as pd
from config import CLEAN_DATA_PATH, DB_PATH

TABLE_NAME = "health_survey"

def build_database() -> None:
    df = pd.read_csv(CLEAN_DATA_PATH)

    with sqlite3.connect(DB_PATH) as conn:
        df.to_sql(TABLE_NAME, conn, if_exists="replace", index=False)

    print(f"Database updated: {DB_PATH}")
    print(f"Table written: {TABLE_NAME}")

if __name__ == "__main__":
    build_database()