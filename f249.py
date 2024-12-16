from machine import Pin, PWM, Timer
from time import sleep

# Configuración de pines
led = Pin(25, Pin.OUT)
pwm_pin = PWM(Pin(26))
motor_pin1 = Pin(27, Pin.OUT)
motor_pin2 = Pin(28, Pin.OUT)

# Configuración del sensor de velocidad
sensor_pin = Pin(16, Pin.IN, Pin.PULL_UP)  # Conecta el sensor aquí
pulse_count = 0  # Contador de pulsos
magnets = 1  # Ajusta según el número de imanes en el eje

# Función de interrupción para contar pulsos
def handle_pulse(pin):
    global pulse_count
    pulse_count += 1

# Configurar la interrupción
sensor_pin.irq(trigger=Pin.IRQ_FALLING, handler=handle_pulse)

# Función para calcular RPM
def calcular_rpms():
    global pulse_count
    rpm = (pulse_count / magnets) * 60  # Convierte pulsos por segundo a RPM
    pulse_count = 0  # Reinicia el contador
    return rpm

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
    sleep(25)
            
    detener_motor()
    sleep(5)
    
    giro(False, 100)
    sleep(25)
    
    detener_motor()
    sleep(5)

# Función para detener el motor
def detener_motor():
    pwm_pin.duty_u16(int(0 * 655.35))
    motor_pin1.value(0)
    motor_pin2.value(0)

# Función principal
def main():
    pwm_pin.freq(20000)  # Frecuencia de PWM en Hz
    timer = Timer()  # Temporizador para medir las RPMs

    # Muestra las RPM cada segundo
    def medir_rpms(t):
        rpm_actual = calcular_rpms()
        print(f"Velocidad: {rpm_actual:.2f} RPM")

    # Inicia el temporizador para medir las RPM cada segundo
    timer.init(period=1000, mode=Timer.PERIODIC, callback=medir_rpms)

    try:
        while True:
            led.on()
            #ciclo_continuo()
            giro(False, 60)
    
    except KeyboardInterrupt:
        led.off()
        detener_motor()
        timer.deinit()  # Detiene el temporizador

if __name__ == "__main__":
    main()
