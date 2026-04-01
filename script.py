import sqlite3
import pandas as pd

COLUMN_MAPPING = {
    "RHC_05": "Regular_Healthcare_Provider",
    "DHHGAGE": "Age",
    "DHH_SEX": "Sex_at_Birth",
    "GEOPRV": "Province",
    "GEOGPRV": "Province",
    "GEO_PRV": "Province",
    "INCDGHH": "Household_Income",
    "EDDVH3": "Education_Level",
    "LBFDVPFT": "Working_Status"
}

VALUE_MAPPINGS = {
    "Regular_Healthcare_Provider": {
        1: "Family doctor or general practitioner",
        2: "Medical specialist",
        3: "Nurse practitioner",
        4: "Other",
        5: "Don’t have a regular health care provider",
        6: "Valid skip",
        7: "Don't know",
        8: "Refusal",
        9: "Not stated"
    },
    "Age": {
        1: "12 to 17 years",
        2: "18 to 34 years",
        3: "35 to 49 years",
        4: "50 to 64 years",
        5: "65 and older",
        6: "Valid skip",
        7: "Don't know",
        8: "Refusal",
        9: "Not stated"
    },
    "Sex_at_Birth": {
        1: "Male",
        2: "Female",
        6: "Valid skip",
        7: "Don't know",
        8: "Refusal",
        9: "Not stated"
    },
    "Province": {
        10: "Newfoundland and labrador",
        11: "Prince Edward Island",
        12: "Nova Scotia",
        13: "New Brunswick",
        24: "Quebec",
        35: "Ontario",
        46: "Manitoba",
        47: "Saskatchewan",
        48: "Alberta",
        59: "British Columbia",
        60: "Yukon /Northwest Territories/ Nunavut",
        96: "Valid skip",
        97: "Don't know",
        98: "Refusal",
        99: "Not stated"
    },
    "Household_Income": {
        1: "No income or less than $20,000",
        2: "$20,000 to $39,999",
        3: "$40,000 to $59,999",
        4: "$60,000 to $79,999",
        5: "$80,000 or more",
        6: "Valid skip",
        7: "Don't know",
        8: "Refusal",
        9: "Not stated"
    },
    "Education_Level": {
        1: "Less than secondary school graduation",
        2: "Secondary school graduation, no post-secondary education",
        3: "Post-secondary certificate/diploma / university degree",
        6: "Valid skip",
        7: "Don't know",
        8: "Refusal",
        9: "Not stated"
    },
    "Working_Status": {
        1: "Full-time",
        2: "Part-time",
        6: "Valid skip",
        7: "Don't know",
        8: "Refusal",
        9: "Not stated"
    }
}

def main():
    print("Processing data... this may take a moment.")

    df = pd.read_excel("Canadian Community Health Survey, 2022 Annual Component.xlsx")

    cols_to_keep = [col for col in df.columns if col in COLUMN_MAPPING]
    df = df[cols_to_keep].rename(columns=COLUMN_MAPPING)

    df = df.replace(VALUE_MAPPINGS)

    with sqlite3.connect("healthcare_data.db") as conn:
        df.to_sql("health_survey", conn, if_exists="replace", index=False)

    print("Successfully created healthcare_data.db!")

if __name__ == "__main__":
    main()
