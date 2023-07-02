n=int(input())
a=[]
for i in range (n):
    b=input()
    c=[int(x) for x in b.split()]
    a.append(c)

f=0
for i in range (len(a)):
    for j in range (1,len(a)):
        if a[i][0] < a[j][0] :
            if a[i][1] > a[j][1] :
                f+=1
               
if f>=1:
  print('happy irsa')
else:
  print('poor irsa')