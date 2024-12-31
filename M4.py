from machine import Pin, PWM, ADC
from time import sleep
import functions

led = Pin(25, Pin.OUT)
pwm_pin = PWM(Pin(26))
motor_pin1 = Pin(27, Pin.OUT)
motor_pin2 = Pin(28, Pin.OUT)
sensor_pin = Pin(16, Pin.IN, Pin.PULL_UP)

def modo_manual():
    pass

def modo_diagnostico():
    pass

def main():
    pwm_pin.freq(20000)  # Frecuencia de PWM en Hz

    try:
        while True:
            datos = functions.recibir_datos()

            if datos:
                if datos == "manual": #Codigo a ejecutar en el modo "manual"
                    modo_manual()

                elif datos == "diagnostico": #Codigo a ejecutar en el modo "diagnostico"
                    modo_diagnostico()

                else:
                    print(f"Comando no reconocido: {datos}")
            else:
                pass
            
            sleep(0.5)
            
    
    except KeyboardInterrupt:
        led.off()
        pwm_pin.duty_u16(0)
        motor_pin1.value(0)
        motor_pin2.value(0)

if __name__ == "__main__":
    main()

