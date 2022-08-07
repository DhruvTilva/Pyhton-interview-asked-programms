# for num in range(100,200):
#     if all(num%i!=0 for i in range(2,num)):
#         print(num)








#************prime or not number*******

num=11
if num>1:
    for i in range(2,num):
        if (num%2)==0:
            print("not a prime")
            break
        else:
            print("prime it is")
            break
else:
    print("not a prime numberrrrrrrrrrrrrrrr")