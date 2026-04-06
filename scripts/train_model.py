import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

from config import CLEAN_DATA_PATH, FIGURES_DIR, TABLES_DIR

FEATURES = ["Household_Income", "Age", "Sex_at_Birth", "Education_Level"]
TARGET = "No_Healthcare_Provider"

def train_model() -> None:
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    TABLES_DIR.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(CLEAN_DATA_PATH)

    X = df[FEATURES]
    y = df[TARGET]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
# 4. Machine Learning Classification Model
    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    metrics_df = pd.DataFrame(
        {
            "metric": ["r2", "mse"],
            "value": [r2_score(y_test, y_pred), mean_squared_error(y_test, y_pred)],
        }
    )
    metrics_df.to_csv(TABLES_DIR / "model_metrics.csv", index=False)

    coef_df = pd.DataFrame(
        {
            "feature": FEATURES,
            "coefficient": model.coef_,
            "coefficient_pct_points": model.coef_ * 100,
        }
    )
    coef_df.to_csv(TABLES_DIR / "combined_model_coefficients.csv", index=False)

    plt.figure(figsize=(9, 5))
    sns.barplot(data=coef_df, x="coefficient_pct_points", y="feature")
    plt.title("Impact on Risk of Not Having a Doctor")
    plt.xlabel("Change in Probability (%) per Unit Increase")
    plt.ylabel("Feature")
    plt.axvline(0, color="black", linewidth=1)
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "combined_model_coefficients.png")
    plt.close()

    print("Model training complete.")
    print(metrics_df)

if __name__ == "__main__":
    train_model()