from machine import Pin, time_pulse_us
from time import sleep

# Configuración de pines
trigger = Pin(12, Pin.OUT)
echo = Pin(13, Pin.IN)

# Prueba básica del sensor
def prueba_sensor():
    # Trigger bajo
    trigger.value(0)
    sleep(0.002)  # Pausa de 2 ms para estabilizar el sensor
    
    # Generar pulso de 10 µs en Trigger
    trigger.value(1)
    sleep(0.00001)  # Pausa de 10 µs
    trigger.value(0)
    
    print("Trigger activado")
    
    # Medir el tiempo en el Echo
    try:
        duracion = time_pulse_us(echo, 1, 30000)  # Esperar un pulso máximo 30 ms
        if duracion > 0:
            print(f"Pulso detectado: {duracion} µs")
        else:
            print("No se detectó eco")
    except OSError:
        print("Error: No se detectó pulso en el Echo")

# Ciclo principal
def main():
    while True:
        prueba_sensor()
        sleep(1)

if __name__ == "__main__":
    main()
