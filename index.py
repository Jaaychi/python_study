# print 10
x = 10
print(x)

# print newPrice which is a discounted value
value = 15
discount = .20

newPrice = 15 * (1 - discount)
print(int(newPrice))

# You can add two names together for example

name = 'Jeffrey'

print(name + name)
print(name + " " + name)
print(name * 2)

# you can set values on top of values 
a = 25
b = a
# print a and b and both is 25

print(a)
print(b)
# if you change b to 17 THEN b will disregard previous variable

#string formatting,  f allows you to embed stuff into strings
name = "JP"
greeting = f"Hello {name}"

print(greeting)

# you can use .format in string formatting

greetings_with_names = f"Hello {} and {}"

new_var_with_all_names = greetings_with_name.format("Jeffrey", "Jean-Paul")
print(new_var_with_all_names)
