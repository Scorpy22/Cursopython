#son inmutables -> no se pueden editar

mi_tupla = (1,2,(10,20),4)
print(type(mi_tupla))
print(mi_tupla[2][0])

#conversion a una lista
mi_tupla = list(mi_tupla)
print(type(mi_tupla))

#asignar a diferentes variables (el mismo tamaño de datos, en la tupla y en la lista)
t = (1,2,3)
x,y,z = t
print(x,y,z)

#aplicando metodo en tuplas count () e index()
t=(1,2,3,1)
print(t.count(1))
print(t.index(3))