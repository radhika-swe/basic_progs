"""n=int(input())
if n%2==0:
    print("even")
elif n%2==1 or n==1:
    print("odd")
    """

"""Examples:

15  ->               1 1 1 1
                    &  0 0 0 1
                       -------
                       0 0 0 1 , so this we can say it is an odd number.

44 ->        1 0 1 1 0 0
            &  0 0 0 0 0 1
                 ----------
                0 0 0 0 0 0 , so this we can say it is an even number."""

def isEven(n):
    if(n&1)==0:
        return True
    else:
        return False
    
if __name__=="__main__":
    n=int(input())
    if isEven(n):
        print("True")
    else:
        print("false")