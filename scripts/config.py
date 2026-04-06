from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"
OUTPUTS_DIR = BASE_DIR / "outputs"
FIGURES_DIR = OUTPUTS_DIR / "figures"
TABLES_DIR = OUTPUTS_DIR / "tables"

RAW_DATA_PATH = RAW_DIR / "Canadian Community Health Survey, 2022 Annual Component.xlsx"
CLEAN_DATA_PATH = PROCESSED_DIR / "cchs_2022_clean.csv"
DB_PATH = DATA_DIR / "healthcare_data.db"

INVALID_CODES = [6, 7, 8, 9, 96, 97, 98, 99]

COLUMN_MAPPING = {
    "GEN_01": "Perceived_Health",
    "RHC_05": "Regular_Healthcare_Provider",
    "DHHGAGE": "Age",
    "DHH_SEX": "Sex_at_Birth",
    "GEOGPRV": "Province",
    "INCDGHH": "Household_Income",
    "EDDVH3": "Education_Level",
    "LBFDVPFT": "Working_Status"
}

VALUE_MAPPINGS = {
    "Perceived_Health": {
        1: "Excellent",
        2: "Very good",
        3: "Good",
        4: "Fair",
        5: "Poor",
        6: "Valid skip",
        7: "Don't know",
        8: "Refusal",
        9: "Not stated"
    },
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
        10: "Newfoundland and Labrador",
        11: "Prince Edward Island",
        12: "Nova Scotia",
        13: "New Brunswick",
        24: "Quebec",
        35: "Ontario",
        46: "Manitoba",
        47: "Saskatchewan",
        48: "Alberta",
        59: "British Columbia",
        60: "Yukon / Northwest Territories / Nunavut",
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