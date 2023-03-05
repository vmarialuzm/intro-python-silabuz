# Ejemplo de herencia múltiple

class A:
    def usoA(self):
        print("Uso de clase A")

class B:
    def usoB(self):
        print("Uso de clase B")

class AB(A,B):
    def usoAB(self):
        self.usoA()
        self.usoB()
        print("Uso de clase AB")

ab=AB()
ab.usoAB()