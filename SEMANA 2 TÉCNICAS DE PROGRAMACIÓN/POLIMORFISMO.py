
# Ejemplo de polimorfismo
class FiguraGeométrica:
    def __init__(self, nombre):
        self.nombre = nombre

    def area(self):
        pass

class Circulo(FiguraGeométrica):
    def __init__(self, nombre, radio):
        super().__init__(nombre)
        self.radio = radio

    def area(self):
        return 3.14 * (self.radio ** 2)

class Rectángulo(FiguraGeométrica):
    def __init__(self, nombre, ancho, alto):
        super().__init__(nombre)
        self.ancho = ancho
        self.alto = alto

    def area(self):
        return self.ancho * self.alto

circulo = Circulo("Circulo", 5)
rectángulo = Rectángulo("Rectángulo", 4, 6)
print(circulo.area())  # 78.5
print(rectángulo.area())  # 24

#En este ejemplo, la clase `FiguraGeometrica` define un método `area` que es
# implementado de manera diferente en las clases `Circulo` y `Rectangulo`.
# Esto es un ejemplo de polimorfismo, ya que la clase `FiguraGeometrica` puede
# tener diferentes formas de implementar el método `area`.
