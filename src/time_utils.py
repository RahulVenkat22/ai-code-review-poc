from datetime import datetime, timedelta
import pytz

def format_to_ist(datetime_str: str) -> str:
    """
    Converts input UTC time to IST
    """
    utc = pytz.utc
    ist = pytz.timezone("Asia/Kolkata")

    dt = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")
    dt = utc.localize(dt)
    ist_time = dt.astimezone(ist)

    return ist_time.strftime("%Y-%m-%d %H:%M:%S")

if __name__ == "__main__":
    print(format_to_ist("2025-01-01 10:00:00"))
