from machine import Pin, PWM, ADC
from time import sleep

led = Pin(25, Pin.OUT)
pwm_pin = PWM(Pin(26))
motor_pin1 = Pin(27, Pin.OUT)
motor_pin2 = Pin(28, Pin.OUT)

def giro(sentido,rpm):
    if sentido:
        motor_pin1.value(1) 
        motor_pin2.value(0)
        pwm_pin.duty_u16(int(rpm* 655.35))
    
    else:
        motor_pin1.value(0) 
        motor_pin2.value(1)
        pwm_pin.duty_u16(int(rpm* 655.35))
        
def ciclo_continuo():
    giro(True,100)
    sleep(25)
            
    detener_motor()
    sleep(5)
    
    giro(False,100)
    sleep(25)
    
    detener_motor()
    sleep(5)
        
def detener_motor():
    pwm_pin.duty_u16(int(0* 655.35))

def main():
    pwm_pin.freq(20000)  # Frecuencia de PWM en Hz
    
    try:
        while True:
            led.on()
            ciclo_continuo()
    
    except KeyboardInterrupt:
        led.off()
        pwm_pin.duty_u16(0)
        motor_pin1.value(0)
        motor_pin2.value(0)

if __name__ == "__main__":
    main()

