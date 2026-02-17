"""
Program 98: Print Fibonacci sequence up to n terms using a loop
This program generates Fibonacci series.
"""

def fibonacci(n):
    """Generate Fibonacci sequence up to n terms"""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    fib_seq = [0, 1]
    for i in range(2, n):
        fib_seq.append(fib_seq[i-1] + fib_seq[i-2])
    return fib_seq


# Main program
if __name__ == "__main__":
    test_terms = [0, 1, 5, 10, 7]
    
    print("Fibonacci Sequence Generator")
    print("-" * 40)
    for n in test_terms:
        fib = fibonacci(n)
        print(f"First {n} terms: {fib}")

"""
OUTPUT:
Fibonacci Sequence Generator
----------------------------------------
First 0 terms: []
First 1 terms: [0]
First 5 terms: [0, 1, 1, 2, 3]
First 10 terms: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
First 7 terms: [0, 1, 1, 2, 3, 5, 8]
"""
