# a = 2 

# def fnumber(number):
		
# 		fib_number = fnumber(number-1) + fnumber(number-2)
	
# 	return fib_number

# print(fnumber(a))

n= 1

res = {}
i = 0
for i in range(1,7):
	n = 10**i
	for a in range(1,n+1):
		l = list(str(a))
		if l == l[::-1]:
			i+=1

	res[a] = [ i*100/a]

print(res.values())
last = 1
list1 = []
for a in res.values():
	a = a[0]
	print(a," --a" , last , " --last")
	print(int(a)/int(last))
	list1.append(int(a)/int(last))
	last = a 

print(list1)