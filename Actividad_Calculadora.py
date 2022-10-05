# Databricks notebook source
class calculadora:
    def __init__(self, variables):
        self.variables = variables
    
    def suma(self):
        suma=0
        for x in self.variables:
            suma += x
        return suma
    
    def resta(self):
        resta=0
        for x in self.variables:
            resta -= x
        return resta
    
    
    def multi(self):
        multi=1
        for x in self.variables:
            multi *= x
        return multi
    
    def div(self):
        divej=list(self.variables)
        divej.sort(reverse=True)
        div = divej[0]
        divej.pop(0)
        for x in divej:
            div /= x
        return div

# COMMAND ----------

lista1=calculadora(range(2,5))
lista2=calculadora(range(2,5))

for x in range(2,5):
    print(x)

# COMMAND ----------

lista1.suma() + lista2.suma()

# COMMAND ----------

calculadora.suma(lista1) - calculadora.suma(lista2)

# COMMAND ----------

lista2.resta()

# COMMAND ----------

lista1.multi()

# COMMAND ----------

lista2.div()*calculadora.multi(lista1)

# COMMAND ----------

ej1=list(range(2,30,3))
ej1.sort(reverse=True)
ej1
