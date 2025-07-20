def leap_year(year):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_months(years,months):
    month_days=[31,28,31,30,31,30,31,31,30,31,30,31]
    # if months<1 or months>12:
    #     return "Invalid input"
    # if leap_year(year) and months == 2:
    #         return 29
    # return month_days[months-1]
    
    for days in month_days:
        if leap_year(year):
            month_days[1]=29
    return month_days[months-1]                               



year=int(input("Enter a year: "))
month=int(input("Enter a month: "))
days= days_in_months(years=year,months=month)
print(days)
