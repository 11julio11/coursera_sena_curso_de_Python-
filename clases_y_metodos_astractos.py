from abc import ABC, abstractmethod

# Clase Banco
class Banco(ABC):
    """ Una clase de banco abstracta """
    
    def basicinfo(self):
        print("Este es un banco genérico")
        return "Banco genérico: 0"
    
    @abstractmethod
    def withdraw(self, amount):
        pass

# Clase Suizo
class Suizo(Banco):
    """ Un tipo específico de banco que deriva de la clase Banco """
    
    def __init__(self):
        self.bal = 1000

    def basicinfo(self):
        print("Este es el Banco Suizo")
        return f"Banco Suizo: {self.bal}"

    def withdraw(self, amount):
        if amount > self.bal:
            print("Fondos insuficientes")
            return self.bal
        else:
            self.bal -= amount
            print(f"Monto retirado: {amount}")
            print(f"Nuevo saldo: {self.bal}")
            return self.bal

# Código Principal
def main():
    assert issubclass(Banco, ABC), "Banco debe derivar de la clase ABC"
    s = Suizo()
    print(s.basicinfo())
    s.withdraw(30)
    s.withdraw(1000)

if __name__ == "__main__":
    main()
