# Databricks notebook source
import math
class calculadora:
    def __init__(self, variables, base = 0, exponente = 0):
        self.variables = variables
        self.base = base
        self.exponente = exponente
        
    
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
    
    def raiz(self, base = 0):
        self.base = base
        sqr = math.sqrt(self.variables[self.base])
        return sqr
    
    def potencia(self, base = 0, exponente = 1):
        self.base = base
        self.exponente = exponente
        potencia = self.variables[base] ** self.variables[exponente]
        return potencia

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

# COMMAND ----------

calculadora.raiz(lista1,2)

# COMMAND ----------

lista1.raiz(1)

# COMMAND ----------

calculadora.potencia(lista2)

# COMMAND ----------

lista1.potencia(2,0)
