### Lists ###

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [46, 24, 62 ,52, 30, 30, 17]
print(my_list)
print(len(my_list)) # Longitud de lista

my_other_list = [46, 1.76, "Fernando", "Pina"]
print(my_other_list)
print(type(my_other_list))

my_age = my_other_list[0]
print(my_age)

my_age = my_other_list[-1]
print(my_age)

#my_age = my_other_list[4] # IndexError: list index out of range
#my_age = my_other_list[-5] # IndexError: list index out of range

print(my_list.count(30)) # Devuelve 2 concurrencias del valor 30

age, height, name, surname = my_other_list # Necesita tener definidos todos los elementos de la lista
print(age)
print(surname)

print(my_list + my_other_list)

my_other_list.append("Pinsho.com")
print(my_other_list)

my_other_list.insert(0, "KIA")
print(my_other_list)

my_other_list[0] = "Seat"
print(my_other_list)

my_list.remove(30) # Solo elimina el primer objeto coincidente
print(my_list)

print(my_list.pop()) # Extrae de la lista el índice indicado, por defecto el último
print(my_list)

my_pop_element = my_list.pop(2)
print(my_pop_element)

del my_list[1] # Elimina objeto indicando el índice
print(my_list)

my_new_list = my_list.copy()

my_list.clear()
print(my_list)
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print(my_new_list)

