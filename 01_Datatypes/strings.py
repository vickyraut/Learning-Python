string = "Masala Chai"
print(string[0:3])
print(string[:])
print(string[1:10:2])
print(string[::-1])

chai = "     Masala chai     "
print(chai.strip())

print(string.find('Chai'))

chai_type = 'Masala'
quantity = 2
order = "I ordered {} cups of {} chai"
print(order)
print(order.format(quantity, chai_type))