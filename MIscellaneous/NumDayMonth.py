def is_year_leap(year):
    if year % 4 == 0:
        if (year % 100 == 0) and (year % 400 == 0):
            return True
        if (year % 100 == 0) and (year % 400 > 0):
            return False
        else:
            return True
    else:
        return False

def days_in_month(year, month):
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return 31
    elif month == 2:
        if is_year_leap(year):
            return 28
        else:
            return 29
    elif month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    else:
        return 0

def day_of_year(year, month, day):
    key = [1,4,4,0,2,5,0,3,6,1,4,6]
    
    yy = abs(year) % 100
    print("yy = ", yy)
    total = yy + yy//4 + day + key[month-1]
    print("total = ", total)
    
    if year == is_year_leap and month <=2:
        total -= 1
        
    if year >= 2000 and year <=2999:
        total += 6
        print("year total = ", total, year)
    elif year >= 1900 and year <=1999:
        total += 0
    elif year >= 1800 and year <=1899:
        total += 2
    elif year >= 1700 and year <=1799:
        total += 4
    numday = total % 7
    
    if numday == 0:
        return "Saturday"
    elif numday == 1:
        return "Sunday"
    elif numday == 2:
        return "Monday"
    elif numday == 3:
        return "Tuesday"
    elif numday == 4:
        return "Wednesday"
    elif numday == 5:
        return "Thursday"
    elif numday == 6:
        return "Friday"
        
        
print(day_of_year(2009, 1, 5))

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")
