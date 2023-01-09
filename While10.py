def main(s):
    """
    A string of numbers is given. Find and return the sum of all odd digits.
    Args:
        s: str
    Returns:
        int: return answer
    """
    a=0
    sum=0
    while a<len(s):
        if int(s[a])%2!=0:
            sum+= int(s[a])
        a+=1
    return sum
s="23546"
print(main(s))