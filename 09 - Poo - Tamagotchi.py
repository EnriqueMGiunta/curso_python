"""
Tamagotchi
<enriquemgiunta@gmail.com>
"""
class Tamagotchi():
    def __init__(self, nombre, n_energia, n_hambre, n_felicidad, humor, vivo):
        self.nombre = nombre
        self.n_energia = 100
        self.n_hambre = 0
        self.n_felicidad = 50
        self.humor
        self.vivo = True
    # METODOS        
    def mostrar_estado(self):
        # Muestra en consola el nombre del Tamagotchi y sus niveles actuales de energía, hambre y estado de humor.
        print(f"Tamagotchi: {self.nombre}")
        print(f"Nivel de energía: {self.n_energia}")
        print(f"Nivel de hambre: {self.n_hambre}")
        print(f"Nivel de felicidad: {self.n_felicidad}")
        print(f"Humor: {self.humor}")
    def alimentar(self):
        # Disminuye el nivel de hambre en 10 y disminuye el nivel de energía en 15.
        self.n_hambre -= 10
        self.n_energia -= 15
    def jugar(self):
        # Aumenta el nivel de felicidad en 20, disminuye el nivel de energía en 18 y aumenta el nivel de hambre en 10.
        self.n_felicidad += 20
        self.n_energia = -18
        self.n_hambre = +10
    def dormir(self):
        #  Aumenta el nivel de energía en 40 y aumenta el nivel de hambre en 5.
        self.n_energia = +40
        self.n_hambre = +5
    def verificar_estado(self):
        # Además, implementa un método llamado verificar_estado que revise si el Tamagotchi está vivo.
        # Un Tamagotchi está vivo mientras su nivel de energía sea mayor que cero.
        # Si el nivel de hambre llega a 20, cada vez que se realice una acción que no sea alimentar deberá reducir
        # los puntos de energía en 20 puntos y la felicidad perderá 30 puntos. Si el nivel de energía llega a cero,
        # el Tamagotchi muere y el atributo esta_vivo debe ser False.
        if self.n_energia <= 0:
            self.vivo = False
