n=int(input("enter a number:"))  
def dis(n):
    s=0
    while n>0:
        l=len(str(n))
        a=n%10
        s=s + pow(a,l)
        n=int(n//10)
        l-=1
    
    return s

b=dis(n) 
if b==n:
        print("number is dissarium")   
else:
    print("it is not a disarium")




def string(s):
    v="a,e,i,o,u,A,E,I,O,U"
    left=0
    right=len(s)-1
    s=list(s)
    while left<right:
        if s[left] not in v:
            left=left+1
            continue
        if s[right] not in v:
            right=right-1
            continue
        s[left],s[right]=s[right],s[left]
        left=left+1
        right=right-1
    return "".join(s)
s=input("Enter a string: ")
result=string(s)
print(result)

    