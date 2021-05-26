
elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
sum=0
sum2=0
avg=0
avg2=0
count=0
count1=0
while i<len(elements):
    if  elements[i]%2==0:
        sum=sum+elements[i]
        count1=count1+1
    else:
        sum2=sum2+elements[i]
        count=count+1
    i=i+1
    # count=count+1
avg=sum//11
avg2=sum2//11
print(count1,"even",avg)
print(count,"odd",avg2)

