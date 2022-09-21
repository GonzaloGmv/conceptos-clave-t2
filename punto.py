class punto():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def string(self):
        print("(", self.x, ",", self.y, ")")

    def cuadrante(self):
        if self.x == 0 and self.y == 0:
            print("Esta en el origen")
        elif self.x == 0 and self.y != 0:
            print("Esta en el eje Y")
        elif self.y == 0 and self.x != 0:
            print("Esta en el eje X")
        elif self.y > 0 and self.x > 0:
            print("Está en el primer cuadrante")
        elif self.y > 0 and self.x < 0:
            print("Está en el segundo cuadrante")
        elif self.y < 0 and self.x < 0:
            print("Está en el tercer cuadrante")
        elif self.y < 0 and self.x > 0:
            print("Está en el cuarto cuadrante")

    def vector(self, xp, yp):
        xv = xp - self.x 
        yv = yp - self.y
        print("El vector resultante es (", xv, ",", yv, ")")
    

a = punto(2,3)
b = punto(5,5)
c = punto(-3,-1)
d = punto(0,0)

a.cuadrante()
b.cuadrante()
c.cuadrante()
a.vector(5,5)