import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from config import CLEAN_DATA_PATH, FIGURES_DIR

def generate_basic_figures() -> None:
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    df = pd.read_csv(CLEAN_DATA_PATH)

    plt.figure(figsize=(8, 5))
    sns.pointplot(data=df, x="Household_Income", y="No_Healthcare_Provider")
    plt.title("Probability of No Healthcare Provider by Income")
    plt.xlabel("Household Income Category")
    plt.ylabel("Probability of Lacking a Provider")
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "healthcare_vs_income_trend.png")
    plt.close()

    plt.figure(figsize=(8, 5))
    sns.pointplot(data=df, x="Education_Level", y="No_Healthcare_Provider")
    plt.title("Probability of No Healthcare Provider by Education Level")
    plt.xlabel("Education Level")
    plt.ylabel("Probability of Lacking a Provider")
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "healthcare_vs_education_trend.png")
    plt.close()

    plt.figure(figsize=(8, 5))
    sns.pointplot(data=df, x="Age", y="No_Healthcare_Provider", hue="Sex")
    plt.title("Probability of No Healthcare Provider by Age and Sex")
    plt.xlabel("Age Group")
    plt.ylabel("Probability of Lacking a Provider")
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "healthcare_vs_age_sex_trend.png")
    plt.close()

    print("Basic figures saved.")

if __name__ == "__main__":
    generate_basic_figures()