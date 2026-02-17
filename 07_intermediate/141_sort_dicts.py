"""
Program 141: Sort list of dictionaries by key value
This program sorts a list of dictionaries based on a specific key.
"""

def sort_dictionaries(lst, key):
    """Sort list of dictionaries by key"""
    return sorted(lst, key=lambda x: x[key])


# Main program
if __name__ == "__main__":
    students = [
        {'name': 'Alice', 'grade': 85},
        {'name': 'Bob', 'grade': 75},
        {'name': 'Charlie', 'grade': 95},
    ]
    
    print("Sort Dictionaries by Key Value")
    print("-" * 40)
    print(f"Original: {students}")
    
    sorted_by_grade = sort_dictionaries(students, 'grade')
    print(f"Sorted by grade: {sorted_by_grade}")
    
    sorted_by_name = sort_dictionaries(students, 'name')
    print(f"Sorted by name: {sorted_by_name}")

"""
OUTPUT:
Sort Dictionaries by Key Value
----------------------------------------
Original: [{'name': 'Alice', 'grade': 85}, {'name': 'Bob', 'grade': 75}, {'name': 'Charlie', 'grade': 95}]
Sorted by grade: [{'name': 'Bob', 'grade': 75}, {'name': 'Alice', 'grade': 85}, {'name': 'Charlie', 'grade': 95}]
Sorted by name: [{'name': 'Alice', 'grade': 85}, {'name': 'Bob', 'grade': 75}, {'name': 'Charlie', 'grade': 95}]
"""
