### Tuples ###

# Los valores de las tuplas son constantes, no se pueden modificar

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (46, 1.76, "Fernando", "Pina", "Fernando")
my_other_tuple = (30, 45, 60)

print(my_tuple)
print(type(my_tuple))
print (my_tuple[0])
print(my_tuple[-1])
#print(my_tuple[4]) # IndexError: list index out of range
#print(my_tuple[-5]) # IndexError: list index out of range

print(my_tuple.count("Fernando"))
print(len(my_tuple))
print(my_tuple.index("Pina"))
print(my_tuple.index("Fernando")) # Índice del primer elemento coincidente

#my_tuple[1] = 1.80 # TypeError: 'tuple' object does not support item assignment
print(my_tuple)

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)
print(my_sum_tuple[2:6]) # Slice

my_tuple = list(my_tuple) # Cambiar tupla a lista
print(type(my_tuple))
my_tuple.insert(5,"Pinsho.com")
my_tuple[0] = "KIA"

my_tuple = tuple(my_tuple) # Cambiar lista a tupla
print(my_tuple)
print(type(my_tuple))

#del my_tuple # NameError: name 'my_tuple' is not defined
#del my_tuple[2] # TypeError: 'tuple' object doesn't support item deletion
print(my_tuple)