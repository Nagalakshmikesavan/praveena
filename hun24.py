n,k=map(int,input().split())
a=input().split()
l=[]
lis=[]
for i in range(0,n):
	a[i]=int(a[i])
	l.append(a[i])
	
for i in range(0,n):
	for j in range(0,n):
		if l[i]+l[j]==k:
			lis.append(l[i])
if lis==[]:
	print('no')
else:
	print('yes')
