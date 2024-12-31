from machine import Pin, PWM
from time import sleep

# Configuración de pines
led = Pin(25, Pin.OUT)
pwm_pin = PWM(Pin(26))
motor_pin1 = Pin(27, Pin.OUT)
motor_pin2 = Pin(28, Pin.OUT)

# Configuración del sensor de velocidad
sensor_pin = Pin(16, Pin.IN, Pin.PULL_UP)  # Conecta el sensor aquí

# Función de interrupción para detectar pulsos
def handle_pulse(pin):
    print("¡Interrupción detectada!")

# Configurar la interrupción en el sensor
sensor_pin.irq(trigger=Pin.IRQ_FALLING, handler=handle_pulse)

# Función para controlar el giro del motor
def giro(sentido, rpm):
    if sentido:
        motor_pin1.value(1) 
        motor_pin2.value(0)
        pwm_pin.duty_u16(int(rpm * 655.35))  # Escala de 0-100%
    else:
        motor_pin1.value(0) 
        motor_pin2.value(1)
        pwm_pin.duty_u16(int(rpm * 655.35))  # Escala de 0-100%

# Función para un ciclo continuo de giro
def ciclo_continuo():
    giro(True, 100)
    sleep(5)
            
    detener_motor()
    sleep(2)
    
    giro(False, 100)
    sleep(5)
    
    detener_motor()
    sleep(2)

# Función para detener el motor
def detener_motor():
    pwm_pin.duty_u16(int(0 * 655.35))
    motor_pin1.value(0)
    motor_pin2.value(0)

# Función principal
def main():
    pwm_pin.freq(20000)  # Frecuencia de PWM en Hz

    try:
        while True:
            led.on()
            #ciclo_continuo()
            giro(False, 100)
    
    except KeyboardInterrupt:
        led.off()
        detener_motor()
        print("Programa detenido.")

if __name__ == "__main__":
    main()