marks = [
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65],
    [95, 45, 78],
    [87, 67, 49, 68, 88]
]
i=0
avg=0
count=0
while i<len(marks):
    j=0
    sum=0
    total=0
    while j< len(marks[i]):
        total=total+marks[i][j]
        j=j+1
    sum=sum+total
    avg=sum//len(marks[i])
    i=i+1
    count=count+1
    print(count,"year avg=",avg)

