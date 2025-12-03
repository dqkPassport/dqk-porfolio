
import pandas as pd

def clean_excel(input_path, output_path):
    df = pd.read_excel(input_path)

    # Remove empty rows
    df = df.dropna(how="all")

    # Strip spaces from text columns
    for col in df.select_dtypes(include=["object"]):
        df[col] = df[col].str.strip()

    # Reset index
    df = df.reset_index(drop=True)

    df.to_excel(output_path, index=False)
    print("Cleaned file saved to:", output_path)

if __name__ == "__main__":
    clean_excel("input.xlsx", "cleaned.xlsx")
