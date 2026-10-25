from datetime import datetime

def get_days_from_today(date):
    """
    Calculate the number of days between the given date and today.
    Date format: YYYY-MM-DD.
    """
    try:
        date = datetime.strptime(date, "%Y-%m-%d").date()
        today = datetime.today().date()
        delta = today - date
        return delta.days
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return None


date = input("Enter a date (YYYY-MM-DD): ")
result = get_days_from_today(date)

if result is not None:

    print(f"Days from the given date to today: {result}")