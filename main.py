class Voxel:

  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z

  def imprimir(self):
    print(self.x, self.y, self.z)


class PVoxel:

  def __init__(self, x, y, z):
    self.existencia = False
    self.pared_superior = False
    self.pared_inferior = False
    self.pared_izquierda = False
    self.pared_derecha = False
    self.x = x
    self.y = y
    self.z = z

  def imprimir(self):
    print(self.x, self.y, self.z)


r = 10
s = 10
m = [[0 for _ in range(r)] for _ in range(s)]

vista = input()
nVox = input()
VList = []
ListaAPintar = []

for _ in range(int(nVox)):
  i = input()
  v = Voxel(int(i[0]), int(i[2]), int(i[4]))
  VList.append(v)

for i in VList:
  if i not in ListaAPintar:
    v = i
    for _ in VList:
      if i != _ and i.x == _.x and i.y == _.y and i.z < _.z:
        v = _
    ListaAPintar.append(v)

for i in ListaAPintar:
  i.imprimir()
