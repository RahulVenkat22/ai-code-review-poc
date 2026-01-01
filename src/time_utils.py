from datetime import datetime

def format_to_ist(datetime_str: str) -> str:
    """
    Expected to return IST time
    but actually returns UTC (bug)
    """
    dt = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")
    return dt.isoformat(sep=" ")

if __name__ == "__main__":
    print(format_to_ist("2025-01-01 10:00:00"))
