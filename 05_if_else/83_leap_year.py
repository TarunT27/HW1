"""
Program 83: Check if a year is a leap year
This program validates leap year using conditions.
"""

def is_leap_year(year):
    """Check if year is a leap year"""
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


# Main program
if __name__ == "__main__":
    test_years = [2000, 1900, 2020, 2021, 2024, 2025]
    
    print("Leap Year Checker")
    print("-" * 40)
    for year in test_years:
        result = is_leap_year(year)
        print(f"{year} -> Leap Year: {result}")

"""
OUTPUT:
Leap Year Checker
----------------------------------------
2000 -> Leap Year: True
1900 -> Leap Year: False
2020 -> Leap Year: True
2021 -> Leap Year: False
2024 -> Leap Year: True
2025 -> Leap Year: False
"""
