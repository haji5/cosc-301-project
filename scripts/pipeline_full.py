from clean_data import main as clean_main
from build_database import build_database
from run_eda import run_eda
from generate_figures import generate_basic_figures
from train_model import train_model

def main() -> None:
    clean_main()
    build_database()
    run_eda()
    generate_basic_figures()
    train_model()
    print("Full pipeline completed successfully.")

if __name__ == "__main__":
    main()