#约瑟夫环
persons=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
k=3
m=0
while len(persons)>1:
    m=(m+k-1)%len(persons)
    print(persons[m])
    del persons[m]
print("剩余",persons[0])
