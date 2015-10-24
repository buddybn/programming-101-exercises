def maximum(lst):
	max_value = lst[0]
	for n in lst:
		if n > max_value:
			max_value = n
	return max_value

r1 = maximum([2, 3])
r2 = maximum([10, 20, 10, 30, 501, 500])
r3 = maximum([6.0, 3.5, -5.6, 2.0])

print(r1, r2, r3)