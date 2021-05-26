 
from cgi import print_directory


elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43] 
i=0
count=0
while i<len(elements):
        if elements[i]%2==0:
            count=count+elements[i]
            print(elements[i],"it is even number")
        else:
            print(elements[i],"it is odd number ")
            count=count+elements[i]
        i=i+1
# print(elements[i],"it is even number")
# print(elements[i],"it is odd number ")