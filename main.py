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
    print(a.distancia(5,5))
    print(b.distancia(2,3))
    #Consulta la base, altura y área del rectángulo.
    print(a.base())
    print(a.altura())
    print(a.area())