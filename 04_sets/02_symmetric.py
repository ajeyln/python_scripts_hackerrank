a = set(map(int, input().split(" ")))
b = set(map(int, input().split(" ")))
result =  list(a.symmetric_difference(b))
result.sort()
for i in result:
	print(i)
	