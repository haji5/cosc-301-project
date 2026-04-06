import pandas as pd
from config import CLEAN_DATA_PATH, TABLES_DIR

def run_eda() -> None:
    TABLES_DIR.mkdir(parents=True, exist_ok=True)
    df = pd.read_csv(CLEAN_DATA_PATH)

    summary = df.describe(include="all")
    summary.to_csv(TABLES_DIR / "summary_statistics.csv")

    income_grouped = df.groupby("Household_Income")["No_Healthcare_Provider"].agg(["mean", "count"])
    income_grouped.to_csv(TABLES_DIR / "risk_by_income.csv")

    edu_grouped = df.groupby("Education_Level")["No_Healthcare_Provider"].agg(["mean", "count"])
    edu_grouped.to_csv(TABLES_DIR / "risk_by_education.csv")

    age_sex_grouped = df.groupby(["Age", "Sex"])["No_Healthcare_Provider"].agg(["mean", "count"])
    age_sex_grouped.to_csv(TABLES_DIR / "risk_by_age_and_sex.csv")

    province_grouped = df.groupby("Province")["No_Healthcare_Provider"].agg(["mean", "count"])
    province_grouped.to_csv(TABLES_DIR / "risk_by_province.csv")

    print("EDA tables exported to outputs/tables")

if __name__ == "__main__":
    run_eda()