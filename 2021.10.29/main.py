from crud import MyCrud

myCrud = MyCrud('cliente2.db')

myCrud.createTable()

clientes = myCrud.getAllClientes()

print(clientes)

myCrud.closeConnection()
