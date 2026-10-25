from datetime import datetime

def get_days_from_today(date):
    date = datetime.strptime(date, "%Y-%m-%d").date()
    today = datetime.today().date()
    delta = today - date
    return delta.days


birthday = input("Enter your birthday (YYYY-MM-DD): ")
print(f"Days from today to your birthday: {get_days_from_today(birthday)}")