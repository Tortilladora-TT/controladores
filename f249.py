from machine import Pin
import time

# Configurar el pin GPIO 16 como entrada
sensor_pin = Pin(16, Pin.IN)

# Contador de objetos detectados
contador = 0

# Función para manejar la interrupción del sensor
def sensor_callback(pin):
    global contador
    contador += 1
    print(f"Objeto #{contador}")

# Configurar la interrupción en el pin del sensor
sensor_pin.irq(trigger=Pin.IRQ_RISING, handler=sensor_callback)

# Bucle principal
while True:
    time.sleep(1)  # Esperar 1 segundo antes de verificar nuevamente