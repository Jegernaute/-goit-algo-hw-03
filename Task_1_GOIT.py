from datetime import datetime


def string_to_date(date): 
    date = datetime.strptime(date, "%Y-%m-%d")
    return date.date()


def get_days_from_today(date):
    try :
        date = string_to_date(date)
        current_date = datetime.today()
        difference_date = current_date.toordinal() - date.toordinal()
        return difference_date
    except ValueError:
        print("Please enter valid format date, for example : 2024-09-27")
    



print(get_days_from_today('2021-10-09'))