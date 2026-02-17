"""
Program 14: Check if a string starts with a specific prefix
This program validates if a string begins with given prefix.
"""

def starts_with_prefix(s, prefix):
    """Check if string starts with prefix"""
    return s.startswith(prefix)


def starts_with_prefix_manual(s, prefix):
    """Check prefix manually"""
    if len(prefix) > len(s):
        return False
    for i in range(len(prefix)):
        if s[i] != prefix[i]:
            return False
    return True


# Main program
if __name__ == "__main__":
    test_cases = [
        ("hello world", "hello"),
        ("python", "java"),
        ("programming", "pro"),
        ("test", "test"),
        ("abc", "abcd")
    ]
    
    print("Prefix Checker")
    print("-" * 40)
    for string, prefix in test_cases:
        result = starts_with_prefix(string, prefix)
        print(f"'{string}' starts with '{prefix}' -> {result}")

"""
OUTPUT:
Prefix Checker
----------------------------------------
'hello world' starts with 'hello' -> True
'python' starts with 'java' -> False
'programming' starts with 'pro' -> True
'test' starts with 'test' -> True
'abc' starts with 'abcd' -> False
"""
