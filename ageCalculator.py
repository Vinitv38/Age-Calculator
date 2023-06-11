from datetime import datetime
current_time=datetime.now().time()
current_date=datetime.now()

day = current_date.day
month = current_date.month
year = current_date.year

hour = current_time.hour
minute = current_time.minute
secs = current_time.second
print(month)

birth_year = int(input("Enter the birth year: "))
birth_month = int(input("Enter birth month: "))
birth_date = int(input("Enter birth date: "))


if(month>=birth_month):
    age_year=year-birth_year
    if(day>=birth_date):
        if((month-birth_month)>=0):
            age_month=month-birth_month
            age_day= day-birth_date
            
            
        else:
            age_month=12 +(month-birth_month)
            age_day= day-birth_date
            
    else:
        if((month-birth_month)>=0):
            age_month=month-birth_month
            if((day-birth_date)>=0):
                age_day= day-birth_date
            else:
                age_day=30+(day-birth_date)
        else:
            age_month=11 +(month-birth_month)
            if((day-birth_date)>=0):
                age_day= day-birth_date
            else:
                age_day=30+(day-birth_date)
else:
    age_year=year-birth_year-1
    if(day>=birth_date):
        if((month-birth_month)>=0):
            age_month=month-birth_month
            if((day-birth_date)>=0):
                age_day= day-birth_date
            else:
                age_day=30+(day-birth_date)
        else:
            age_month=12 +(month-birth_month)
            if((day-birth_date)>=0):
                age_day= day-birth_date
            else:
                age_day=30+(day-birth_date)
    else:
        if((month-birth_month)>=0):
            age_month=month-birth_month
            if((day-birth_date)>=0):
                age_day= day-birth_date
            else:
                age_day=30+(day-birth_date)
        else:
            age_month=11 +(month-birth_month) 
            if((day-birth_date)>=0):
                age_day= day-birth_date
            else:
                age_day=30+(day-birth_date)
print(f"Your age is {age_year} years, {age_month} months, {age_day} days")
