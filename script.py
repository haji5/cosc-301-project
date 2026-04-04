import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

    # 1. Data Cleaning
    cols_to_keep = [col for col in df.columns if col in COLUMN_MAPPING]
    df = df[cols_to_keep].rename(columns=COLUMN_MAPPING)
    df = df.loc[:, ~df.columns.duplicated()]

    df = df.drop_duplicates().dropna()

    # Remove extreme outliers / invalid survey responses
    invalid_codes = [6, 7, 8, 9, 96, 97, 98, 99]
    for col in df.columns:
        df = df[~df[col].isin(invalid_codes)]

    # Custom Requirement: Remove the lowest income bracket (dependents/youth noise)
    # Only keep Household Income categories 2, 3, 4, and 5.
    df = df[df["Household_Income"] > 1]

    print("\nCleaned Summary Statistics (Income Brackets 2-5):")
    print(df.describe())

    # 2. Target Setup
    # 1 = No healthcare provider, 0 = Has healthcare provider
    df["No_Healthcare_Provider"] = (df["Regular_Healthcare_Provider"] == 5).astype(int)

    # Visualization
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LinearRegression
    from sklearn.metrics import mean_squared_error, r2_score

    print("\nGenerating clean trend plot...")
    plt.figure(figsize=(8, 5))
    sns.pointplot(data=df, x="Household_Income", y="No_Healthcare_Provider", color="crimson")
    plt.title("Probability of NO Healthcare Provider by Income")
    plt.xlabel("Household Income Category (2=$20k+, 5=$80k+)")
    plt.ylabel("Probability of Lacking a Provider")
    plt.savefig("healthcare_vs_income_trend.png")
    plt.close()

    print("\nGenerating education trend plot...")
    plt.figure(figsize=(8, 5))
    sns.pointplot(data=df, x="Education_Level", y="No_Healthcare_Provider", color="royalblue")
    plt.title("Probability of NO Healthcare Provider by Education Level")
    plt.xlabel("Education Level (1=Less than secondary, 3=Post-secondary)")
    plt.ylabel("Probability of Lacking a Provider")
    plt.savefig("healthcare_vs_education_trend.png")
    plt.close()

    print("\nGenerating age/gender trend plot...")
    plt.figure(figsize=(8, 5))
    df["Sex"] = df["Sex_at_Birth"].map({1: "Male", 2: "Female"})
    sns.pointplot(data=df, x="Age", y="No_Healthcare_Provider", hue="Sex", palette="Set1")
    plt.title("Probability of NO Healthcare Provider by Age and Gender")
    plt.xlabel("Age Group (2=18-34, 3=35-49, 4=50-64)")
    plt.ylabel("Probability of Lacking a Provider")
    plt.savefig("healthcare_vs_age_sex_trend.png")
    plt.close()

    # 3. Regression Modeling (Linear Probability Model)
    X = df[["Household_Income"]]
    y = df["No_Healthcare_Provider"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    print("\nLinear Probability Model Results (Individual Level):")
    print(f"R-squared: {r2_score(y_test, y_pred):.4f}")
    print(f"MSE: {mean_squared_error(y_test, y_pred):.4f}")

    # Display Macro-Trend R-squared
    # Individual survey R-squares are always tiny. Grouping by income shows how perfectly income drives the AVERAGE access.
    grouped = df.groupby("Household_Income")["No_Healthcare_Provider"].mean().reset_index()
    X_macro = grouped[["Household_Income"]]
    y_macro = grouped["No_Healthcare_Provider"]
    macro_model = LinearRegression().fit(X_macro, y_macro)
    print(f"\nMacro-Trend R-squared (Grouped Income Averages): {r2_score(y_macro, macro_model.predict(X_macro)):.4f}")

    # Predict Risk
    print("\nCalculated Risk of NOT Having a Doctor:")
    for inc in range(2, 6):
        risk = model.predict(pd.DataFrame({"Household_Income": [inc]}))[0] * 100
        print(f"Income Bracket {inc}: {risk:.2f}% chance of NO doctor")

    print("\nCalculated Risk of NOT Having a Doctor by Education Level:")
    edu_grouped = df.groupby("Education_Level")["No_Healthcare_Provider"].agg(['mean', 'count'])
    for idx, row in edu_grouped.iterrows():
        print(f"Education Level {idx}: {row['mean']*100:.2f}% chance of NO doctor (n={int(row['count'])})")

    print("\nCalculated Risk of NOT Having a Doctor by Age & Gender:")
    age_sex_grouped = df.groupby(["Age", "Sex"])["No_Healthcare_Provider"].agg(['mean', 'count'])
    for idx, row in age_sex_grouped.iterrows():
        print(f"Age Group {idx[0]} | {idx[1]}: {row['mean']*100:.2f}% chance of NO doctor (n={int(row['count'])})")

    # 4. Machine Learning Classification Model
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.metrics import accuracy_score, classification_report

    print("\n--- Machine Learning Classification Model (Random Forest) ---")
    X_multi = df[["Household_Income", "Age", "Sex_at_Birth", "Education_Level"]]
    y_multi = df["No_Healthcare_Provider"]
    
    X_train_m, X_test_m, y_train_m, y_test_m = train_test_split(X_multi, y_multi, test_size=0.2, random_state=42)
    rf_model = RandomForestClassifier(n_estimators=100, random_state=42, class_weight="balanced")
    rf_model.fit(X_train_m, y_train_m)
    y_pred_m = rf_model.predict(X_test_m)

    print("\nModel Evaluation Metrics:")
    print(f"Accuracy: {accuracy_score(y_test_m, y_pred_m):.4f}")
    print("\nClassification Report:")
    print(classification_report(y_test_m, y_pred_m, target_names=["Has Doctor (0)", "No Doctor (1)"]))

    factors = ["Household Income", "Age Bracket", "Sex at Birth", "Education Level"]
    importances = rf_model.feature_importances_

    print("\nFeature Importances:")
    for factor, imp in zip(factors, importances):
        print(f"{factor}: {imp*100:.2f}%")

    print("\nGenerating feature importance plot...")
    plt.figure(figsize=(9, 5))
    sns.barplot(x=importances * 100, y=factors, hue=factors, legend=False, palette="viridis")
    plt.title("Feature Importance in Predicting Healthcare Access")
    plt.xlabel("Relative Importance (%)")
    plt.tight_layout()
    plt.savefig("ml_feature_importance.png", bbox_inches="tight", pad_inches=0.3, facecolor='white', dpi=300)
    plt.close()

    # Append continuous probability to Dataframe (using rf probabilities for target 1)
    df["Expected_No_Provider_Risk"] = rf_model.predict_proba(X_multi)[:, 1]

    # 5. Final Storage
    df = df.replace(VALUE_MAPPINGS)
    with sqlite3.connect("healthcare_data.db") as conn:
        df.to_sql("health_survey", conn, if_exists="replace", index=False)

    print("\nSuccessfully organized and saved to healthcare_data.db!")

if __name__ == "__main__":
    main()
