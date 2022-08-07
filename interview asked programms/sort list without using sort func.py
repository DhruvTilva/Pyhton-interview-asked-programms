l1=[1,54,221,1,324,34]
l2=[]
while l1:
    minimum= l1[0]
    for i in l1:
        if i > minimum:
            minimum=i
    l2.append(minimum)
    l1.remove(minimum)
    
print(l2)