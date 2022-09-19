#PALINDROME NUMBER
"""
def pali(n):
    if len(n)==0:
        return True
    if n[0]!=n[-1]:
        return False
    return pali(n[1:-1])

print(pali("anna"))
print(pali("anma"))
"""
#BUBBLE SORT
"""
def bubble(l):
    for i in range(len(l)-1):
        for j in range(len(l)-i-1):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
    return l
l=[9,1,8,2,3,5,4,7]
print(bubble(l))
"""

#FACTORS OF A NUMBER and perfect
"""
l=[]
def factors(n):
    q=n
    s1=0
    s2=0
    for i in range(1,n+1//2):
        if n%i==0:
            p=i
            l.append(p)
            if p%2==0:
                s1+=p
            else:
                s2+=p
    s=s1+s2
    if s==q:
        print("perfect")

    else:
        print("not perfect")
    print(l)
    print(s1)
    print(s2)



factors(6)
"""
"""
def palindrome(n):
    rev=""
    revn=0
    q=n
    if type(n)==str:
        for i in n:
            rev=i+rev
   

    if type(n)==int:
        while n>0:
            rem=n%10
            revn=revn*10+rem
            n=n//10
    if q==rev or q==revn:
        print("palindrome")

    else:
        print("not palindrome")

palindrome("anna")
palindrome("anma")
palindrome(121)
palindrome(21)
"""
#FIBONACCI SERIES
"""
def fibo(n):
    assert n>=0 and int(n)==n,"THE FIBO NUMBERS cannot be negative"
    if n in [0,1]:
        return n
    else:
        return fibo(n-1)+fibo(n-2)
n=6
print(fibo(5))
for i in range(0,n+1):
    print(fibo(i),end=" ")

"""
#DIGIT EXTRACTION WITH SUM OF DIGITS
"""
def is_digit(n):
    s=0
    while n>0:
        r=n%10
        print(r,end=" ")
        s+=r
        n=n//10
    print("\n",s)

is_digit(123)
"""
"""
def check(n):
    s=0
    p=n
    while n>0:
        rem=n%10
        s+=rem
        n=n//10
    print(s)
    if p%s==0:
        print(int(p/s))
check(126)
"""
