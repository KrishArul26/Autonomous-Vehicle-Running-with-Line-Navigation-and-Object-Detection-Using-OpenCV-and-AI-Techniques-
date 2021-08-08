import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
Buzzer_Pin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(Buzzer_Pin, GPIO.OUT)


class Buzzer:
    def run(self, command):
        if command != "0":
            GPIO.output(Buzzer_Pin, True)
        else:
            GPIO.output(Buzzer_Pin, False)

    def backWarner(self):
        while True:
            B.run('1')
            time.sleep(0.5)
            B.run('0')
            time.sleep(0.5)


if __name__ == '__main__':
    B = Buzzer()
    B.run('1')
    time.sleep(0.5)
    B.run('0')
