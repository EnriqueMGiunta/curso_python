"""
Tamagotchi
<enriquemgiunta@gmail.com>
"""
class Tamagotchi():
    # ATRIBUTOS
    def __init__(self, nombre):
        self.nombre = nombre
        self.n_energia = 100
        self.n_hambre = randint(0, 100)
        self.n_felicidad = randint(0, 100)
        self.n_humor = randint(0, 100)
        self.vivo = True
        #Dibuja ventana
        pg.theme = "Topanga"
        self.layout = [
            [pg.Text(f"MASCOTA \"{self.nombre}\"")],
            [pg.ProgressBar(1, orientation='h', size=(20,10), key='Energia')],
            [pg.ProgressBar(2, orientation='h', size=(20,10), key='Hambre')],
            [pg.ProgressBar(3, orientation='h', size=(20,10), key='Humor')],
            [pg.ProgressBar(4, orientation='h', size=(20,10), key='Felicidad')],
            [pg.Button("Alimentar"), pg.Button("Jugar"), pg.Button("Dormir"), pg.Button("Hacer necesidades"), pg.Button("Salir")],
            [pg.Output(size=(40, 8))]
        ]
        self.ventana = pg.Window("TAMAGOTCHI", self.layout)
        self.boton = "."

    # METODOS        
    def mostrar_estado(self):
        # Muestra en consola el nombre del Tamagotchi y sus niveles actuales de energía, hambre y estado de humor.
#        cls()
        print(f"Tamagotchi: {self.nombre}")
        print(f"Nivel de energía:   {self.n_energia}%")
        print(f"Nivel de hambre:    {self.n_hambre}%")
        print(f"Nivel de felicidad: {self.n_felicidad}%")
        print(f"Nivel de Humor:     {self.n_humor}%")
        print(f"Está vivo?:         {self.vivo}")
 #       progress_bar = self.ventana.FindElement('Energia')
 #       progress_bar.UpdateBar(self.n_energia, 100)
    def verificar_estado(self):
        # Además, implementa un método llamado verificar_estado que revise si el Tamagotchi está vivo.
        # Un Tamagotchi está vivo mientras su nivel de energía sea mayor que cero.
        # Si el nivel de hambre llega a 20, cada vez que se realice una acción que no sea alimentar deberá reducir
        # los puntos de energía en 20 puntos y la felicidad perderá 30 puntos. Si el nivel de energía llega a cero,
        # el Tamagotchi muere y el atributo esta_vivo debe ser False.
        if self.n_energia <= 0:
            self.muerto()
        else:
            self.n_humor = int(self.n_felicidad - self.n_hambre/2)
            if self.n_energia < 0:
                self.n_energia = 0
            elif self.n_energia > 100:
                self.n_energia = 100
            if self.n_felicidad < 0:
                self.n_felicidad = 0
            elif self.n_felicidad > 100:
                self.n_felicidad = 100
            if self.n_hambre < 0:
                self.n_hambre = 0
            elif self.n_hambre > 100:
                self.n_hambre = 100
            if self.n_humor < 0:
                self.n_humor = 0
            elif self.n_humor > 100:
                self.n_humor = 100
    def alimentar(self):
        # Disminuye el nivel de hambre en 10 y disminuye el nivel de energía en 15.
        self.n_hambre -= 10
        self.n_energia -= 15
        self.n_humor += 5
    def jugar(self):
        # Aumenta el nivel de felicidad en 20, disminuye el nivel de energía en 18 y aumenta el nivel de hambre en 10.
        self.n_felicidad += 20
        self.n_energia -= 18
        self.n_hambre += 10
        self.n_humor += 10
    def dormir(self):
        #  Aumenta el nivel de energía en 40 y aumenta el nivel de hambre en 5.
        self.n_energia += 40
        self.n_hambre += 5
    def hacer_necesidades(self):
        #  Ir al baño. Disminuye el nivel de energía en 15, aumenta nivel de hambre en 15 y humor en 5.
        self.n_energia += 15
        self.n_hambre += 15
        self.n_humor += 5
    def desgaste(self):
        #  Genera un desgaste natural con el tiempo.
        while self.vivo:
            if self.n_energia > 0:
                self.n_energia -= 1
            if self.n_hambre >= 0 and self.n_hambre < 100:
                self.n_hambre += 1
            if self.n_hambre > 0:
                self.n_felicidad -= 1
            self.verificar_estado()
            self.mostrar_estado()
            print(f"Desgaste natural en segundo plano....")
            time.sleep(1)
    def muerto(self):
        #  Todos los niveles quedan en cero y el estado de vivo pasa a False.
        self.n_energia = 0
        self.n_hambre = 0
        self.n_felicidad = 0
        self.n_humor = 0
        self.vivo = False
    def interactuar(self):
        while self.boton not in ('EXIT', 'Salir', None):
            self.verificar_estado()
            self.mostrar_estado()
            self.boton, valor = self.ventana.read()
            if self.vivo:
                if self.boton == "Alimentar":
                    self.alimentar()
                if self.boton == "Jugar":
                    self.jugar()
                if self.boton == "Dormir":
                    self.dormir()
                if self.boton == "Hacer necesidades":
                    self.hacer_necesidades()
            self.verificar_estado()
            self.mostrar_estado()
        self.ventana.close()

def cls():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")
    return

# *********************** Bloque principal **************************
from random import randint
import os
import PySimpleGUI as pg
import threading
import time

mascota1 = Tamagotchi("Cuacho Pacho")
mascota1_hilo_desgaste = threading.Thread(target=mascota1.desgaste, args=())
mascota1_hilo_desgaste.start()
#mascota1_hilo_desgaste.join()
mascota1.interactuar()
