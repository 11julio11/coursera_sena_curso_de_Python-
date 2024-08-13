class Employees:
    def __init__(self, name, last) -> None:
        self.name = name 
        self.last = last
    
    def __str__(self) -> str:
        return f"{self.name} {self.last}"
    
class supervisor(Employees):
    def __init__(self, name, last, password) -> None:
        super().__init__(name, last)
        self.password = password

class chef(Employees):
    def leave_request(self, days):
        return f"May I take leave for {days} days"
    

adrian = supervisor("Adrian", "A", "apple")
emely = chef("Emely", "E")
juno = chef("Juno", "J")

print(emely.leave_request(3))
print(adrian.password)
print(emely.name)