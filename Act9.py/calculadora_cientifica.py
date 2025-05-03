import math
class Calculadora_Cientifica:
    def raiz_cuadrada(self, numero):
        return math.sqrt(numero)
    def logaritmo(self, numero, base = 10):
        return math.log(numero, base)
    def potencia(self, numero, exponente):
        return (numero ** exponente)
    def sen(self, angulo_grados):
        radianes = math.radians(angulo_grados)
        return math.sin(radianes)
    def cos(self, angulo_grados):
        radianes = math.radians(angulo_grados)
        return math.cos(radianes)
    def tan(self, angulo_grados):
        radianes = math.radians(angulo_grados)
        return math.tan(radianes)