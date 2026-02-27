import pandas as pd


def get_service_rate(file_path, customer):
    """Reads the excel file and returns the most recent service rate."""
    xl = pd.ExcelFile(file_path)
    sheet_name = next(s for s in xl.sheet_names if customer.lower() in s.lower())
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    service_rate_row = df[df["Service Period"] == "Service Rate"].iloc[-1]
    if "Service Rate" in service_rate_row.index:
        return service_rate_row["Service Rate"]
    else:
        return service_rate_row["Base Rate"]
if __name__ == "__main__":
    print(get_service_rate("month_to_month.xlsx", "kale me crazy"))