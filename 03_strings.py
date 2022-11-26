# Formateo
name, surname, age = "Pin", "Sho", 26
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}") # Método preferido

# Desempaquetado de variables
language = "Python"
a, b, c, d, e, f = language
print(language)
print(a)
print(f)

# Division
language_slice = language[2:5] # Result tho
print(language_slice)

language_slice = language[1:] # Result ython
print(language_slice)

language_slice = language[-2] # Result o
print(language_slice)

# Reverse
language_reverse = language[::-1] # Result nohtyP
print(language_reverse)