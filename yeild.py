




def read_file_line_by_line(file_name):
	with open(file_name, 'r') as f:
		r = 1
		while True:
			line = f.readline()
			assert line != '', f'list ending {r}'
			#assert line != '\n', f'list ending {r}'
			#assert line, f'list ending {r}'
			#if not line: break
			yield line, r
			#if r>3: return f'df {r}'
			#assert line, f'list ending {r}'
			r+=1


lines_generator = read_file_line_by_line("data.csv")
#print(type(lines_generator))
#print(dir(lines_generator))


for i in range(1,40):
	sv1 = lines_generator.__next__()
	print(f'sv{i}:{sv1}')

'''
sv1 = lines_generator.__next__()
print(f'sv1:{sv1}')
sv1 = lines_generator.__next__()
print(f'sv2:{sv1}')
sv1 = lines_generator.__next__()
print(f'sv3:{sv1}')
sv1 = lines_generator.__next__()
print(f'sv4:{sv1}')
sv1 = lines_generator.__next__()
print(f'sv5:{sv1}')
sv1 = lines_generator.__next__()
print(f'sv6:{sv1}')
sv1 = lines_generator.__next__()
print(f'sv7:{sv1}')
sv1 = lines_generator.__next__()
print(f'sv8:{sv1}')
'''

