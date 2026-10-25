from datetime import datetime, timedelta

def get_upcoming_birthdays(users: list):
    """Return users with birthdays in the next 7 days, moving weekend greetings to Monday."""
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday_date = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday_date.replace(year=today.year)
        
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        
        days_until_birthday = (birthday_this_year - today).days
        if 0 <= days_until_birthday <= 7:
            congratulation_date = birthday_this_year
            if congratulation_date.weekday() == 5:
                congratulation_date += timedelta(days=2)
            elif congratulation_date.weekday() == 6:
                congratulation_date += timedelta(days=1)
            upcoming_birthdays.append({"name": user["name"], "congratulation_date": congratulation_date.strftime("%Y.%m.%d")})

    return upcoming_birthdays




users = [
    {"name": "Anna", "birthday": "1998.10.25"},
    {"name": "John", "birthday": "1985.10.26"},
    {"name": "Jane", "birthday": "1990.10.27"},
    {"name": "Kate", "birthday": "1995.10.30"},
    {"name": "Mike", "birthday": "2000.10.31"},
    {"name": "Alex", "birthday": "1992.11.01"},
    {"name": "Emma", "birthday": "1999.11.02"},
    {"name": "Max", "birthday": "1988.12.15"},
]
upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
