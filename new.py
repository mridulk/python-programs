inp=input()
l=inp.split()
for i in range(2):
    l[i]=int(l[i])
kk=l[1]
li =[]
for k in range(l[0]):
    strr = input()
    li.append(strr)
#print(li)
matrix = []; columns = []
# initialize the number of rows
for i in range(0,l[0]):
    matrix += [0]
# initialize the matrix
for i in range (0,l[0]):
    matrix[i] = [0]*2
count=0
t=0
for i in range(l[0]):
    s = li[i].split()
    t=0
    for j in range(2):
        matrix[i][j]=int(s[t])
        t=t+1
#print(matrix)
ans=[]
for i in range(l[0]):
    if(matrix[i][1]==1):
        count=count+1
#print(count)
sum=0
if(kk==count):
    for i in range(l[0]):
        sum=sum+matrix[i][0]
else:
    for i in range(l[0]):
        if(matrix[i][1]==1):
            ans.append(matrix[i][0])
    ans.sort()
    ans.reverse()
    n=count-kk
    for i in range(kk):
        sum=sum+ans[i]
    ans.sort()
    for i in range(n):
        sum=sum-ans[i]
for i in range(l[0]):
    if(matrix[i][1]==0):
        sum=sum+matrix[i][0]
print(sum)













