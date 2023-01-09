def main(s):
    """
    A string of numbers is given. Find how many odd digits there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    a=0
    count=0
    while a<len(s):
        if int(s[a])%2!=0 and s[a].isdigit()==True:
            count+=1
        a+=1
    return count
s="1234567"
print(main(s))