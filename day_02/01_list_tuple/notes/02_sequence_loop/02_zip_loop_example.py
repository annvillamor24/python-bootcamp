items = ('a', 'b', 'c')
others = (1, 2, 3)

for item, other in zip(items, others):
	print(item, other)

for item in zip(items,others):
	print(item, other)


names = zip(items, others)
for name, other in zip(names, others):
	print(name, other)