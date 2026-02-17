"""
Program 91: Determine grade based on student's score
This program converts scores to letter grades.
"""

def get_grade(score):
    """Determine grade from score"""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


# Main program
if __name__ == "__main__":
    test_scores = [95, 85, 75, 65, 55, 100, 50]
    
    print("Grade Determiner")
    print("-" * 40)
    for score in test_scores:
        grade = get_grade(score)
        print(f"Score {score} -> Grade: {grade}")

"""
OUTPUT:
Grade Determiner
----------------------------------------
Score 95 -> Grade: A
Score 85 -> Grade: B
Score 75 -> Grade: C
Score 65 -> Grade: D
Score 55 -> Grade: F
Score 100 -> Grade: A
Score 50 -> Grade: F
"""
