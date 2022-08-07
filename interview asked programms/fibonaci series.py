


n=int(input("enter value of n:"))
a=0
b=1
sum=0
count=1
print("fibonaci series:",end=' ')
while(count<=n):
    print(sum,end=' ')
    count +=1
    a=b
    b=sum
    sum=a+b



    #***********using recursion*******
def recur_fibo(n):
    if n<=1:
        return n
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2))
nterm= int(input("Enter number:"))

if nterm<=0:
    print("please enter a positive int")
else:
    for  i in range(nterm):
        print(recur_fibo())
