#find output
#input = the sky is blue
#output= blue is sky the

str="the sky is blue"
l=str.split() #first the split the string
l=l[::-1] #the reverse the string
l=' '.join(l) #join the reverse string
print(l)


# slicing important