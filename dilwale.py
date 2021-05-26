 
paisa_hai = [3000, 600000, 324990909, 90990900, 30000, 5600000, 
690909090, 31010101, 532010, 510, 4100] 
i=0
a=100000
count=0
count1=0
count2=0
while i<len(paisa_hai):
    if paisa_hai[i]>a:
        count=count+1
    elif paisa_hai[i]<a:
        count1=count1+1
    else:
        count2=count2+1
    i=i+1
print(count,"crorepati hai")
print(count1,"lakhpati hai")
print(count2,"dilwale hai")
