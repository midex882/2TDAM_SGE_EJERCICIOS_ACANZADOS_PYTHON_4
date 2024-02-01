import os
from functools import reduce

# EJERCICIO 1
# input = input("Qué tipo de comida quieres?: ")
# dic = {
#     "fruta": "Manzana, platano o pera",
#     "verdura": "Lechuga, pepino, mi abuela",
#     "kebab": "pollo, ternera, mixto",
#     "pescado": "lubina, acedía, boquerón"
# }
#
# print(dic.get(input.lower(), "No está disponible"))


# EJERCICIO 2

# def mostrar(lista):
#     for i in range(0, len(lista)):
#         print("Posicion",i,":",lista[i])
#
# def modificar(lista):
#     for i in range(0, len(lista)):
#         lista[i] *= lista[i]
#     print(lista)
# def longitud(lista):
#     print(len(lista))
#
# opcion = input("Quieres mostrar, modificar o longitud?")
# lista = [4,8,14,22]
#
#
# operaciones = {
#     "mostrar" : mostrar,
#     "modificar": modificar,
#     "longitud": longitud,
# }
#
#
# accion = operaciones.get(opcion, lambda lista: "Acción no disponible")
#
# accion(lista)

# EJERCICIO 3

# palabras = ["amor", "paz", "guerra", "dolor", "felicidad"]
#
# # Fran, yo he entendido que lo que querías era conseguir una lista con las palabras de
# # menos o igual de tres letras, porque si no, no se filtraría nada. Si querías lo opuesto,
# # gira el <
#
# palabras_filtradas = filter(lambda x: len(x) <= 3, palabras)
#
# print(list(palabras_filtradas))

# EJERCICIO 4
# def converter(keys,row):
#     ret = {}
#     arr = row.split(";")
#     for i in range(len(keys)):
#         print(f"{keys[i]} : {arr[i]}")
#         ret[keys[i]] = arr[i]
#     print("==================")
#     return ret
#
#
# file = open("juegos.csv", "r")
# file_contents = file.read()
# file.close()
#
#
# file_contents_array = file_contents.split("\n")
# keys = file_contents_array[0]
# keys = keys.split(";")
#
# file_contents_array.pop(0)
#
# results = []
#
# for row in file_contents_array:
#     results.append(converter(keys,row))
#
# print(list(results))

# EJERCICIO 5

# def converter(keys,arr):
#     ret = {}
#     for i in range(len(keys)):
#         ret[keys[i]] = arr[i]
#     return ret
#
#
# file = open("juegos.csv", "r")
# file_contents = file.read()
# file.close()
#
#
# file_contents_array = file_contents.split("\n")
# keys = file_contents_array[0]
# keys_arr = keys.split(";")
#
# file_contents_array.pop(0)
#
# results = {}
#
# for row in file_contents_array:
#     arr = row.split(";")
#     results[arr[0]] = converter(keys_arr, arr)
#
# print(results)
#
# # EJERCICIO 6
#
# file_name = "juegos2.csv"
#
#
#
# file = open(f"./{file_name}", "w")
#
# new_content = keys.replace(";",",")+"\n"
#
#
# for v in results.values():
#     row = ""
#     values = list(v.values())
#     for i in range(len(values)):
#         if(i < len(values)-1):
#             row+= f"{values[i]},"
#         else:
#             row += f"{values[i]}"
#     new_content += row+"\n"
#
# file.write(new_content)


# EJERCICIO 7


# lista = [5,3,1,6,2,5,3,6]
#
# def multiplicar(n1,n2):
#     return n1*n2
#
# print(reduce(multiplicar,lista))

# EJERCICIO 8
#
# notas = {
#  "Carmen": 5,
#  "Antonio": 4,
#  "Juan": 8,
#  "Mónica": 9,
#  "María": 6,
#  "Pablo": 3,
#  "Pedro": 7,
#  "Ana": 10,
#  "Luis": 2,
#  "Julia": 1,
#  "Jorge": 6,
#  "Daniel": 9,
#  "Elena": 5,
# }
#
# aprobados = {nombre:nota for nombre, nota in notas.items() if nota >= 5}
#
# print(aprobados)
#
# suspensos = {nombre:nota for nombre, nota in notas.items() if nota < 5}
#
# print(suspensos)

# EJERCICIO 9
#
#
# file_aprobados = open("aprobados.csv", "w")
# file_suspensos = open("suspensos.csv", "w")
#
# string_aprobados = ""
# string_suspensos = ""
#
# for k,v in aprobados.items():
#  string_aprobados += f"{k},{v}\n"
#
# string_aprobados = string_aprobados[:len(string_aprobados)-1]
#
# file_aprobados.write(string_aprobados)
#
# for k, v in suspensos.items():
#  string_suspensos += f"{k},{v}\n"
#
# string_suspensos = string_suspensos[:len(string_suspensos)-1]
#
# file_suspensos.write(string_suspensos)
#
# file_aprobados.close()
# file_suspensos.close()
#

