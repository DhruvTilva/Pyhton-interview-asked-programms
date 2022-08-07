#***********write a program to raise an exeception
l=[1,2,3,4]
sum=0
for i  in l:
    if i==1:
        raise Exception("Exception:1 is found")
    else:
        print("Run succesfully without exception ")
    break