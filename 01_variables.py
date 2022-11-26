# Variables
my_string_variable = "My string" # Tipo "str"
print(my_string_variable)

my_int_variable = 3 # Tipo "int"
print(my_int_variable)

my_bool_variable = True # Tipo "bool"
print(my_bool_variable)

# Convierto int en str
int_to_str = str(my_int_variable)
print(int_to_str)
print(type(int_to_str))

# Concatenación de variables en un print
print(my_string_variable, "value is", my_int_variable, "and this is", my_bool_variable)

# Algunas funciones del sistema
print(len(my_string_variable)) # Longitud caracteres

# Variables en una línea
team, group = "España", "A"
print("El líder del grupo", group, "es", team, "\N{winking face}")

# Inputs
#your_team = input("¿Cuál es tu equipo favorito? ")
#print("Tu equipo favorito es",your_team)

# ¿Forzar el tipo de dato?
address:str = "Calle Real" #aunque se defina como str cambiará su tipo si se le asigna un valor int, por ejemplo
print(address)
