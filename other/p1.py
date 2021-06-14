n = 4
i = 0
while i < n:
	j = 0
	while j < n:
		print(f'{i} * {j} = {i * j}', end = ' | ') 
		j += 1
	i += 1
	print('')
	