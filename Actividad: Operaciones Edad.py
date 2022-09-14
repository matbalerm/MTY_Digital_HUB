# Databricks notebook source
# MAGIC %md #### 1.-El doble de mi edad tiene 24 años, ¿cuántos años tengo?

# COMMAND ----------

#2x=24

# COMMAND ----------

x=24
x/=2
x

# COMMAND ----------

# MAGIC %md #### 2.- A un tercio de la edad de mi hermana la disminuyo en 15 años. Tengo 6 años. ¿Qué edad tiene?

# COMMAND ----------

#(1/3)(y-15)=6


# COMMAND ----------

y=6+(15/3)
y*=3
y

# COMMAND ----------

# MAGIC %md #### 3.-Determina quién es más grande

# COMMAND ----------

if x<y:
    print('Soy más chico yo.')
else:
    print('Soy más grande yo')
