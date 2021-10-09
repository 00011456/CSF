i = int(input("Gimme a number - "))

bin_number = bin(i)
oct_number = oct(i)
hex_number = hex(i)

print(bin_number[2:]) 
print(oct_number[2:])
print(hex_number[2:])