from queue import Queue

from threading import Thread

import time
import random
# Crear cola

q = Queue(10)
maxbollos=random.randint(0,100)


def producer(name):
    prueba= True
    """Productor"""

    count = 1 #mostrador

    while prueba:

        q.join() # Espera a task_done () para enviar una señal

        q.put(count)

        print(f"{name} está produciendo el bollo {count}")

        count+=1

        if (count==maxbollos):
            prueba=False
 
def customer(name):
    prueba= True
    """consumidor"""

    count = 1

    while prueba:

        baozi = q.get()

        print(f"El consumidor- {name} está comiendo el bollo {count}")

        count+=1

        q.task_done() # Envía una señal después de comer

        time.sleep(1)

        if (count==maxbollos):
            prueba=False



if __name__ == '__main__':

    t1 = Thread(target=producer,args=("Maestro Zhang",))

    t2 = Thread(target=customer,args=("Xiaoming",))

    t1.start()

    t2.start()

