"""
Program 130: Check if a string is a valid email address
This program validates email format.
"""

def is_valid_email(email):
    """Check if string is valid email"""
    if not email or '@' not in email or '.' not in email:
        return False
    
    parts = email.split('@')
    if len(parts) != 2:
        return False
    
    username, domain = parts
    if not username or not domain:
        return False
    
    if '.' not in domain:
        return False
    
    return True


# Main program
if __name__ == "__main__":
    test_emails = [
        "user@example.com",
        "invalid.email",
        "@example.com",
        "user@",
        "user@example",
        "user.name@sub.example.com"
    ]
    
    print("Email Validator")
    print("-" * 40)
    for email in test_emails:
        result = is_valid_email(email)
        print(f"'{email}' -> {result}")

"""
OUTPUT:
Email Validator
----------------------------------------
'user@example.com' -> True
'invalid.email' -> False
'@example.com' -> False
'user@' -> False
'user@example' -> False
'user.name@sub.example.com' -> True
"""
