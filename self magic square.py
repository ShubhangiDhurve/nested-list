magic_square = [
    [8, 3, 4],
    [1, 6, 9],
    [6, 7, 2]
]
i=0
while i<len(magic_square):
    j=0
    sum1=0
    while j< len(magic_square):
        sum1=sum1+magic_square[i][j]
        j=j+1
    print(sum1,end=" ")
    i=i+1
print()
d1=0
while d1<len(magic_square):
    d2=0
    sum2=0
    while d2<len(magic_square[d1]):
        sum2=sum2+magic_square[d2][d1]
        d2=d2+1
    print(sum2,end=" ")
    d1=d1+1
print()
r=0
s=r
sum3=0
while r<len(magic_square):
            sum3=sum3+magic_square[r][s]
            r=r+1
print(sum3,end=" ")
print()
r1=0
sum4=0
while r1<len(magic_square):
    p=len(magic_square[r1])-1
    while p>1:
        sum4=sum4+magic_square[r1][p]
        p=p-1
    r1=r1+1
print(sum4,end=" ")
print()
if sum1==sum2==sum3==sum4:
    print("it is magic square")
else:
    print("it is not magic square")






