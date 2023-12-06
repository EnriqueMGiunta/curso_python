import threading
import time

def subproceso(condicion):
    while not condicion.is_set():
        time.sleep(2)
        print(f"\nProceso en segundo plano..")

condicion = threading.Event()


while True:
    print("""
1) Iniciar proceso en segundo plano.
2) Salir
        """)
    entrada = input("-->")
    if entrada == "1":
        hilo = threading.Thread(target=subproceso, args=(condicion,))
        hilo.start()
    if entrada == "2":        
        condicion.set()
        hilo.join()
        break