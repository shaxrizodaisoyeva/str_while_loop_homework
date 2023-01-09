def main(s):
    """
    A string of numbers is given. Find the sum of all the digits and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    b=int(s)
    a=b%10
    while b!=0:
        b//=10
        a+=b%10
    return a 
s="23546"
print(main(s))