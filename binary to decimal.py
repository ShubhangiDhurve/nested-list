binary_number=[1,0,0,1,1,0,1,1]
# a=int(input("enter the number"))
# binary_number=list(a)
i=0
weight=0
while i<len(binary_number):
    decimal=binary_number[len(binary_number)-i-1]
    weight=weight+decimal*(2**i)
    i=i+1
    print(weight)


# a=2**0
# print(a)

# list1=[1,2,3,4,5,6]
# list2=[2,3,1,0,6,7]
# a=[]
# i=0
# while i<len(list1):
#     if list1[i] not in list2:
#         a.append(list1[i])
#     i+=1
# print(a)

# list=[1,2,3,4,5,6]
# list1=[2,3,1,0,6,7]
# a=[]
# i=0
# while i<len(list):
#     j=0
#     while j<len(list1):
#         if list[i] not in list1:
#             a.append(list[i])
#         j=j+1
#         break
#     i=i+1
# print(a)