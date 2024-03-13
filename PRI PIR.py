import machine
import utime

sensor_pir = machine.Pin(16, machine.Pin.IN)
led = machine.Pin(15, machine.Pin.OUT)
buzzer = machine.Pin(14, machine.Pin.OUT)

def pir_handler(pin):
  print("ALARM! Motion detected!")   #print the message.
  for i in range(50):
    led.toggle()
    for j in range(25):
      buzzer.toggle()
      utime.sleep_ms(3)


sensor_pir.irq(trigger = machine.Pin.IRQ_RISING, handler = pir_handler)

while True:
  led.toggle()   #toggle the led.
  buzzer.off()   #turn off buzzer.
  utime.sleep(5) #delay for 5 seconds.
