import pandas as pd
import os
from datetime import datetime
import shutil

# Constants
CSV_FILE = "file.csv"
EXCEL_FILE = "file.xlsx"
ARCHIVE_DIR = "archive"  # Directory to store old versions

data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 35, 40],
    "Salary": [50000, 60000, 70000, 80000],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"]
}


def archive_existing_file(file_path: str) -> None:
    """
    Archives an existing file by renaming it with a timestamp.

    Parameters:
        file_path (str): Path to the file to be archived.
    """
    if os.path.exists(file_path):
        # Create archive directory if not exists
        os.makedirs(ARCHIVE_DIR, exist_ok=True)

        # Generate timestamped filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = os.path.basename(file_path)
        base, ext = os.path.splitext(filename)  # 👈 Fixed here
        archived_name = f"{base}_{timestamp}{ext}"
        archived_path = os.path.join(ARCHIVE_DIR, archived_name)

        # Move and rename the old file
        shutil.move(file_path, archived_path)
        print(f"Archived old file to: {archived_path}")


def save_data(df: pd.DataFrame) -> None:
    """
    Saves DataFrame to CSV and Excel after archiving previous versions.

    Parameters:
        df (pd.DataFrame): The DataFrame to be saved.
    """
    try:
        # Archive existing files if any
        archive_existing_file(CSV_FILE)
        archive_existing_file(EXCEL_FILE)

        # Save new files
        df.to_csv(CSV_FILE, index=False)
        print(f"Saved CSV file at: {os.path.abspath(CSV_FILE)}")

        df.to_excel(EXCEL_FILE, sheet_name="Sheet1", index=False)
        print(f"Saved Excel file at: {os.path.abspath(EXCEL_FILE)}")

    except Exception as e:
        print(f"An error occurred while saving files: {e}")


if __name__ == "__main__":
    df = pd.DataFrame(data)
    save_data(df)