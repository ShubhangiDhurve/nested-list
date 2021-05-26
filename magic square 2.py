magic_square = [
    [8, 6, 4],
    [1, 5, 9],
    [6, 7, 2]
]


p=0
i=0
a=len(magic_square)
while i<a:
    sum=0
    j=0
    while j<len(magic_square[i]):
        sum=sum+magic_square[i][j]
        j=j+1
    i=i+1
    print(sum)

k=0
while k<a:
    sum1=0
    l=0
    while l<len(magic_square[k]):
        sum1=sum1+magic_square[l][k]
        l+=1
    k+=1
    print(sum1)

m=0
c=m
sum2=0
while m<a:
    sum2=sum2+magic_square[m][c]
    m+=1
print(sum2)

p=0
sum3=0
while p<a:
    q=a-1
    while q>1:
        sum3=sum3+magic_square[p][q]
        q=q-1
    p+=1
if sum==sum1==sum2==sum3:
    print("it is magic square")
else:
    print("not")