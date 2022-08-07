# sorting the string using sort() func *******************
# l=[2,5,7,43,23,87]
# l.sort(reverse=False)
# print(l)


#################find the max and min value from list without using any predefine function###########

l= [2,3,5,67,1,4,1]
maximum=l[0]
minimum=l[0]

for i in l:
    if i>maximum:
        maximum=i
    if i<minimum:
        minimum=i
print('maximum:',maximum)
print('minimum',minimum)





# using the max min function 
# o=min(l)
# o=max(l)
# print(o)