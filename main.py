from Punto import punto, a, b, c, d

if __name__ == "__main__":
    #Crea los puntos A(2, 3), B(5,5), C(-3, -1) y D(0,0) e imprimelos por pantalla.
    a.string()
    b.string()
    c.string()
    d.string()
    #Consulta a que cuadrante pertenecen el punto A, C y D
    a.cuadrante()
    b.cuadrante()
    c.cuadrante()
    #Consulta los vectores AB y BA
    a.vector(5,5)
    b.vector(2,3)
    #Consulta la distancia entre los puntos 'A y B' y 'B y A'
    print("La distancia entre a y b es", a.distancia(5,5), "unidades")
    print("La distancia entre b y a es", b.distancia(2,3), "unidades")
    #Determina cual de los 3 puntos A, B o C, se encuentra más lejos del origen, punto (0,0)
    a.distancia_max()
    #Crea un rectángulo utilizando los puntos A y B.
    #Consulta la base, altura y área del rectángulo.
    print("La base del rectangulo es", a.base(), "unidades")
    print("La altura del rectangulo es", a.altura(), "unidades")
    print("El area del rectangulo es", a.area(), "unidades al cuadrado")