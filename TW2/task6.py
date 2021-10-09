count = 0 

print(count)

def increment(a):
	global count 
	count += a

increment(25)
print(count)