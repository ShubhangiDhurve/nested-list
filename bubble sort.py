a=[5,9,4,8,3,2,1]
i=0
n=len(a)
while i<len(a):
    j=0
    while j<n-1:
        b=[]
        if a[j]>a[j+1]:
            p=a[j]
            a[j]=a[j+1]
            a[j+1]=p
        b.append(a)
        j=j+1
    i=i+1
print(b)
