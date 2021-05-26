marks = [
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65, 76],
    [95, 45, 78, 52, 49]
] 
i=0
sum=0
while i<len(marks):
    j=0
    total=0
    while j<len(marks[i]):
        total=total+marks[i][j]
        j=j+1
    sum=sum+total
    i=i+1
print(sum)
avg=sum/15
print(avg)



    