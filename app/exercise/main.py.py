'''
En este desafío, se te presenta una lista de objetos que representan órdenes de compra con los siguientes atributos:

customer_name: string
total: number
delivered: boolean
Tu reto es utilizar el concepto de módulos de Python para retornar la suma total de todas las órdenes de compra. Para resolver el ejercicio, debes trabajar en el archivo main.py, donde se encuentra la función get_total. Esta función recibe como parámetro la lista de órdenes de compra.

Debes retornar la suma total de todas las órdenes haciendo uso de las funciones definidas en el archivo my_functions.py.my_functions.py.
'''

import my_functions

def get_total(orders):
  ordenes = my_functions.get_totals(orders)
  suma_ordenes = my_functions.calc_total(ordenes)
  return suma_ordenes

orders = [
  {
    "customer_name": "Nicolas",
    "total": 100,
    "delivered": True,
  },
  {
    "customer_name": "Zulema",
    "total": 120,
    "delivered": False,
  },
  {
    "customer_name": "Santiago",
    "total": 20,
    "delivered": False,
  }
]

total = get_total(orders)
print(total)