
n=int(input())
data=[]
s=0
l=[]
hazfed=[]
for i in range (n):
	if i==0:
		hazfed.append(n-1)
	else:
		hazfed.append(hazfed[-1]+n)

	data+=[int(x)for x in input().split()]
start=(n*n)-n
end=n-1
def ax(start,end,s,data,):
	if start==end:

		l.append('*')
		return 
	else:
		if  start+1 <=(n*n)-1 and data[start+1]!=1 and start not in hazfed :
			
			
			ax(start+1,end,s,data)
		if  start-n>=0 and data[start-n]!=1 :
			
			
			ax(start-n,end,s,data)
s=ax(start,end,s,data)
print(len(l)+1)
