# name=["n","i","t","i","n"]
# a=[]
# i=len(name)-1
# s=name
# while i>=0:
#     k=(name[i])
#     a.append(k)  
#     i=i-1
# print(a)
# if a==s:
#     print("palidrom")  
# else:
#     print("not palidrom")

# name=["n","i","t","i","n"]
name=["m","o","m"]
a=[]
i=1
while i<=len(name):
    a.append(name[-i])
    i=i+1
print(a)
if a==name:
    print("palidrom")
else:
    print("not palidrom")
