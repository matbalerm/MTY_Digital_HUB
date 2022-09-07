# Databricks notebook source
# MAGIC %md # 1.- Crea un vector con valores dentro del rango 3 a el número que representa tu edad.

# COMMAND ----------

pip install numpy

# COMMAND ----------

import numpy as np

# COMMAND ----------

x=np.arange(3,28)
x

# COMMAND ----------

# MAGIC %md # 2.- Crea un arreglo con los siguientes elementos: [0, 1, 2, 3, 4, 0, 1, 2, 3, 4]

# COMMAND ----------

y=np.arange(0,5)
y

# COMMAND ----------

y1=np.concatenate((y,y))
y1

# COMMAND ----------

# MAGIC %md # 3.- Ordena de forma ascendiente dicho arreglo.

# COMMAND ----------

y1=np.sort(y1)
y1
