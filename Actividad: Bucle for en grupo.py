# Databricks notebook source
# MAGIC %md #### Actividad: Avanzada
# MAGIC 
# MAGIC Asigna un número aleatorio a tu compañero. Los guardarás en un diccionario, junto con el nombre de tu pareja.
# MAGIC Luego imprimirán los valores del diccionario (nombre de la persona y número que dijo) (Usando un bucle for)
# MAGIC  Al final imprimirán dos mensajes, mostrando el número más grande, y el número más pequeño que dijeron, sin el nombre del socio, sólo el número.

# COMMAND ----------

nombres=['César','Gabriela','Olivia','David','Adolfo','Adrián']

# COMMAND ----------

parejas=['Daniela','Martín','Santiago','María','Kim','Ana']

# COMMAND ----------

import random

# COMMAND ----------

diccionario={}

# COMMAND ----------

# MAGIC %md ##### Asigna un número aleatorio a tu compañero. Los guardarás en un diccionario, junto con el nombre de tu pareja.

# COMMAND ----------

for i in range(len(nombres)):
    diccionario[nombres[i]] = {'Pareja': parejas[i], 'NoRandom': random.randint(0,100)}
print(diccionario)

# COMMAND ----------

numeros = []
keys = list(diccionario.keys())
keys

# COMMAND ----------

for i in range(len(keys)):
    norandom = diccionario[keys[i]]['NoRandom']
    numeros.append(norandom)
    print(f'El nombre es {keys[i]} y su número aleatorio es {norandom}')

# COMMAND ----------

#Al final imprimirán dos mensajes, mostrando el número más grande, y el número más pequeño que dijeron, sin el nombre del socio, sólo el número.
print(f'El número más alto fue {max(numeros)} y el más pequeño {min(numeros)}')
