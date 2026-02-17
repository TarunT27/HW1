"""
Program 122: Split a string by delimiter and join it back
This program demonstrates splitting and joining.
"""

def split_and_rejoin(s, delimiter, new_delimiter):
    """Split by one delimiter and rejoin with another"""
    parts = s.split(delimiter)
    return new_delimiter.join(parts)


# Main program
if __name__ == "__main__":
    test_cases = [
        ("a,b,c", ",", "-"),
        ("hello world python", " ", "|"),
        ("1:2:3:4", ":", "-"),
    ]
    
    print("Split and Rejoin Converter")
    print("-" * 40)
    for s, delim, new_delim in test_cases:
        result = split_and_rejoin(s, delim, new_delim)
        print(f"'{s}' (delim='{delim}', new='{new_delim}')")
        print(f"  -> '{result}'\n")

"""
OUTPUT:
Split and Rejoin Converter
----------------------------------------
'a,b,c' (delim=',', new='-')
  -> 'a-b-c'

'hello world python' (delim=' ', new='|')
  -> 'hello|world|python'

'1:2:3:4' (delim=':', new='-')
  -> '1-2-3-4'
"""
