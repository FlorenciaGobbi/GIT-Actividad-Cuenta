class Cuenta:
  def __init__ (self, nombre, cantidad=0):
    self.nombre=nombre
    self.cantidad=cantidad

  def mostrar(self):
      print("Nombre: ",self.nombre, "\nSaldo actual: ", self.cantidad)

  def ingresar(self, ingreso=0):
    self.ingreso=ingreso    

    if ingreso >= 0:
      self.cantidad+=self.ingreso
      print("Ingresó: ", self.ingreso, "\nSaldo actual: ", self.cantidad)

  def retirar(self, retiro=0):
    self.retiro=retiro
    self.cantidad-=self.retiro
    print("Retiró: ", self.retiro, "\nSaldo actual: ", self.cantidad)

titular1 = Cuenta("Jorge", 1000)
titular1.mostrar()
titular1.ingresar(500)
titular1.retirar(8000)