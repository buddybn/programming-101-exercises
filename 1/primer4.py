def count(lst, el):
	povt = 0
	element = el
	for n in lst:
		if n == element:
			povt = povt + 1
	return povt

r1 = count([1, 2, 3], 2)
r2 = count([1, 1, 1, 1, 1], 1)
r3 = count(["A", "B", "C", "A", "C"], "D")

print(r1, r2, r3)