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
        xv = self.x - xp
        yv = self.y - yp
        print("El vector resultante es (", xv, ",", yv, ")")
    
    def rectangulo(self, x1, y1, x2, y2):
        xd = x1 - x2
        yd = y1 - y2
        print("La diagonal del rectángulo es (", xd, ",", yd, ")")

        
punto(1,2).rectangulo()