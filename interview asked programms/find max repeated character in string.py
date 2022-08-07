#find the maximum repeated characeter in a string with optimal time complxity is less than O*2

from typing import Counter


s="itininiytnnhhn"
# ch={}
# for i in s:
#     if i in ch:
#      ch[i]+=1
#     else:
#         ch[i]=1

# max_char=max(ch,key=ch.get)
# print(max_char)


# **************another method********
print('the original string is:' + s)
res= Counter(s)
res= max(res,key=res.get)
print(f"max of all char in {s} is:" + str(res))
