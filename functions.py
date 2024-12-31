from machine import Pin, PWM, ADC, UART

uart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))
led = Pin(25, Pin.OUT)
pwm_pin = PWM(Pin(26))
motor_pin1 = Pin(27, Pin.OUT)
motor_pin2 = Pin(28, Pin.OUT)

def enviar_datos(datos):
    uart.write(datos)

def recibir_datos():
    if uart.any():
        datos = uart.read().decode('utf-8').strip()
        return datos
    else:
        return None

def detener_motor():
    pwm_pin.duty_u16(int(0 * 655.35))
    motor_pin1.value(0)
    motor_pin2.value(0)

def giro_cw(rpm):
    motor_pin1.value(1) 
    motor_pin2.value(0)
    pwm_pin.duty_u16(int(rpm* 655.35))

def giro_ccw(rpm):
    motor_pin1.value(0) 
    motor_pin2.value(1)
    pwm_pin.duty_u16(int(rpm* 655.35))

