def perm(n): # 主函數
	p = [] # p 代表已經排下去的，一開始還沒排，所以是空的
	return permNext(n, p) # 呼叫 permNext 遞迴下去排出所有可能

def permNext(n, p): 
	i = len(p)
	if i == n:  
		print(p)  
		return
	for x in range(n):
		if not x in p: 
			p.append(x)   
			permNext(n, p)  
			p.pop()      

n=int(input())
a=1
for i in range(n):
	a=a*(i+1)
perm(n)
print(a,"種排列組合")
