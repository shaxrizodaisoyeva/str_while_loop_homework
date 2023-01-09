def main(s):
    """
    A variable of type str is given. Find how many digits it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    a=0
    count=0
    while a<len(s):
        if s[a].isdigit()==True:
            count+=1
        a+=1
    return count
s="1234mny567"
print(main(s))