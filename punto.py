import math

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

    def distancia(self, xd, yd):
        x3 = xd - self.x
        y3 = yd - self.y
        d = math.sqrt(x3*x3 + y3*y3)
        return d

    def rectangulo(self, xr, yr):
        p1 = self.x
        p2 = yr
        q1 = xr
        q2 = self.y
        q = []
        q.append(q1)
        q.append(q2)
        return q
    
    def base(self):
        p = a.rectangulo(5,5)
        px = p[0]
        py = p[1]
        base = a.distancia(px, py)
        return base
    
    def altura(self):
        p = a.rectangulo(5,5)
        px = p[0]
        py = p[1]
        h = b.distancia(px, py)
        return h
    
    def area(self):
        b = a.base()
        h = a.altura()
        area = b * h
        return area

a = punto(2,3)
b = punto(5,5)
c = punto(-3,-1)
d = punto(0,0)