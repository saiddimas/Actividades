class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def suma(self, vector2):
        return Vector3D(self.x + vector2.x, self.y + vector2.y, self.z + vector2.z)
    def resta(self, vector2):
        return Vector3D(self.x - vector2.x, self.y - vector2.y, self.z - vector2.z)
    def producto_escalar(self, vector2):
        return (self.x * vector2.x + self.y * vector2.y + self.z * vector2.z)
    def modulo(self):
        return ((self.x **2 + self.y ** 2 + self.z **2)**0.5)
    def normalizar(self):
        return Vector3D(self.x / self.modulo(), self.y / self.modulo(), self.z / self.modulo())
