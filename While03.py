def main(s):
    """
    A variable of type str is given. Find how many punctuations it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    a=0
    count=0
    while a<len(s):
        if s[a].isalpha()==False and s[a].isdigit()==False:
            count+=1
        a+=1
    return count
s="12%&,.:';gh76"
print(main(s))
    