number=[50,40,23,70,58,12,10,66,5,7]
i=0
max=0
while i < len(number):
    if (number[i]>max):
        max=number[i]
        number.remove(max)
    i+=1
# print(max)
max_1=0
j=0
while j<len(number):
    if (number[j]>max_1):
        max_1=number[j]
    j+=1
print(max_1)