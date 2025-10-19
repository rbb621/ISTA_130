import random 

def find_month(exact_date):
    
    # Show the month part
    month_num = int(exact_date[:2])
    
    if month_num == 1:
        return "January"
    elif month_num == 2:
        return "February"
    elif month_num == 3:
        return "March"
    elif month_num == 4:
        return "April"
    elif month_num == 5:
        return "May"
    elif month_num == 6:
        return "June"
    elif month_num == 7:
        return "July"
    elif month_num == 8:
        return "August"
    elif month_num == 9:
        return "September"
    elif month_num == 10:
        return "October"
    elif month_num == 11:
        return "November"
    elif month_num == 12:
        return "December"
    
def find_day(exact_date):
    
    # Print out the exact date of the month
    day_num = int(exact_date[3:5])
    return day_num

def find_remaining_days(exact_dates):
    
    month_name = find_month(exact_dates)
    current_day = find_day(exact_dates)
    
    if month_name == "January" or month_name == "March" or month_name == "May" \
    or month_name == "July" or month_name == "August" or month_name == "October" \
    or month_name == "December":
        days_of_the_month = 31
    elif month_name == "April" or month_name == "June" or month_name == "September" \
        or month_name == "November":
        days_of_the_month = 30
    elif month_name == "February":
        days_of_the_month = 28

        
    remaining_days = days_of_the_month - current_day
    return remaining_days
    

def find_next_day(exact_date):
    month_name = find_month(exact_date)
    current_day = find_day(exact_date)
    
    if month_name == "January" or month_name == "March" or month_name == "May" \
    or month_name == "July" or month_name == "August" or month_name == "October" \
    or month_name == "December":
        days_of_the_month = 31
    elif month_name == "April" or month_name == "June" or month_name == "September" \
        or month_name == "November":
        days_of_the_month = 30
    elif month_name == "February":
        days_of_the_month = 28
        
    # Get month and year parts
    month_num = int(exact_date[:2])
    year_num = int(exact_date[6:])
    
    if current_day == days_of_the_month:
        current_day = 1
        month_num += 1
    if month_num > 12:
        month_num = 1
        year_num += 1
    else:
        current_day += 1
        
    new_month = str(month_num).zfill(2)
    new_day = str(current_day).zfill(2)
    next_day = new_month + "/" + new_day + "/" + str(year_num)
    
    return next_day


def split_date(exact_date):
    
    month = exact_date[:2]
    day = exact_date[3:5]
    year = exact_date[6:]
    
    

    print("Month: ", month)
    print("Day: ", day)
    print("Year: ", year)


def add_one_day(date):
    
    month = int(date[:2])
    next_day = int(date[3:5])
    year = int(date[6:])

    next_day += 1
    print("The next day is", str(month) + str("/") + str(next_day) + "/" + str(year))  

def main():
    exact_month = '06/10/2025'
    exact_day = '10/02/2025'
    print(find_month(exact_month))
    print(find_day(exact_day))
    print(find_remaining_days('05/14/2025'))
    print(find_next_day('01/10/2025'))
    split_date("05/14/2025")
    add_one_day("05/14/2025")
    
    

    

if __name__ == '__main__':
    main()