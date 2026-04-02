class Ordinateur:
    def __init__(self):
        pass

    def afficher_ip(self):
        print("L'ordinateur n'a pas d'adresse IP définie.")

class Server(Ordinateur):
    def __init__(self, ip):
        super().__init__()
        self.ip = ip

    def afficher_ip(self):
        super().afficher_ip()
        print(f"IP  : {self.ip}")

    def __str__(self):
        return f"L'adresse IP du serveur est : {self.ip}"

p = Ordinateur()

s = Server("192.168.1.2")
s.afficher_ip()
print(s)
