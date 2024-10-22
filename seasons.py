'''
Name: Phann Boon
Date: 10/22/24
Assignment: Unit 2 and 3 Project
'''
def start():
    try:
        month = input("Enter the name of the month: ")
        day = int(input("Enter the day (1-31): "))

        if month == "march" and 31 >= day >= 20 or month == "march" and 1 <= day <= 31 or month == "april" and 1 <= day <= 31 or month == "may" and 1 <= day <= 31 :
            season = "Spring"
        elif month == "march" and 1 <= day < 20:
            season = "Winter"
        elif month == "june" and 31 >= day >= 21 or month == "july" and 1 <= day <= 31 or month == "august" and 1 <= day <= 31 :
            season = "Summer"
        elif month == "june" and 1 <= day < 21:
            season = "Spring"
        elif month == "september" and 31 >= day >= 22 or month == "october" and 1 <= day <= 31 or month == "november" and 1 <= day <= 31 :
            season = "Fall"
        elif month == "september" and 1 <= day < 22:
            season = "Summer"
        elif month == "december" and 31 >= day >= 21 or month == "january" and 1 <= day <= 31 or month == "february" and 1 <= day <= 31 :
            season = "Winter"
        elif month == "december" and 1 <= day < 21:
            season = "Fall"
        #else:
            #if not month == "january" or "february" or "march" or "april" or "may" or "june" or "july" or "august" or "september" or "october" or "november" or "december":
                #print("Invalid month.")
            #elif not 1 <= day <= 31:
                #print("Invalid day.")
            #else:
                #print(f"{month.title()} {day} is in {season}.")
    except:
        print("Invalid response.")
        start()

start()

if month == "january" or "february" or "march" or "april" or "may" or "june" or "july" or "august" or "september" or "october" or "november" or "december":
    if 1 <= day <= 31:
        print(f"{month.title()} {day} is in {season}.")