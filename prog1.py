list=[]
a=int(input("enter the no."))
for i in range(a):
    num=int(input("enter the number"))
    list.append(num)
print(list)
sum=0
for i in list:
    if i%2==0:
        sum=sum+i
print(sum)


