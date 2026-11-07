digits= [9,5,7,3,5]
converter = ""

for num in digits:
    converter += str(num)

soma = int(converter) + 1

new_digits= []

for num in str(soma):
    new_digits.append(int(num))


print(new_digits)