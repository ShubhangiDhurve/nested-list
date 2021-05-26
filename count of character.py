
char_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
i=0
# count=0
b=[]
while i<len(char_list):
    j=0
    s=[]
    count=0
    while j<len(char_list):
        if char_list[i]==char_list[j]:
            count=count+1
        j=j+1
    s.append(char_list[i])
    s.append(count)
    if s not in b:
        b.append(s)
    i=i+1
print(b)