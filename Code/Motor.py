import time
from PCA9685 import PCA9685


class Motor:
    def __init__(self):
        self.pwm = PCA9685(0x40, debug=True)
        self.pwm.setPWMFreq(50)

    def duty_range(self, duty1, duty2):
        if duty1 > 4095:
            duty1 = 4095
        elif duty1 < -4095:
            duty1 = -4095

        if duty2 > 4095:
            duty2 = 4095
        elif duty2 < -4095:
            duty2 = -4095

        return duty1, duty2

    def easy_Speed_Val(self, val):
        r_min = -100
        r_max = 100
        t_min = -2000
        t_max = 2000
        return int(((val - r_min)/(r_max - r_min)) * (t_max - t_min) + t_min)

    def left_Upper_Wheel(self, duty):
        if duty < 0:
            self.pwm.setMotorPwm(0, 0)
            self.pwm.setMotorPwm(1, abs(duty))
        elif duty > 0:
            self.pwm.setMotorPwm(1, 0)
            self.pwm.setMotorPwm(0, abs(duty))
        else:
            self.pwm.setMotorPwm(0, 4095)
            self.pwm.setMotorPwm(1, 4095)

    def right_Upper_Wheel(self, duty):
        if duty < 0:
            self.pwm.setMotorPwm(6, 0)
            self.pwm.setMotorPwm(7, abs(duty))
        elif duty > 0:
            self.pwm.setMotorPwm(7, 0)
            self.pwm.setMotorPwm(6, abs(duty))
        else:
            self.pwm.setMotorPwm(6, 4095)
            self.pwm.setMotorPwm(7, 4095)

    def setMotorModel(self, duty1, duty2, cor1=0, cor2=0):
        duty1, duty2 = self.duty_range(
            int(self.easy_Speed_Val(duty1) + cor1), int(self.easy_Speed_Val(duty2) + cor2))
        self.left_Upper_Wheel(duty1)
        self.right_Upper_Wheel(duty2)


PWM = Motor()

def destroy():
    PWM.setMotorModel(0, 0)





def loop():
    print("Forward")
    PWM.setMotorModel(50, 50)  # Forward
    time.sleep(3)
    print("Backward")
    PWM.setMotorModel(-70, -70)  # Back
    time.sleep(3)
    print("Left")
    PWM.setMotorModel(-5, 70)  # Left
    time.sleep(3)
    print("Right")
    PWM.setMotorModel(70, -5)  # Right
    time.sleep(3)
    PWM.setMotorModel(0, 0)  # Stop





if __name__ == '__main__':
    try:
        
        #loop()
        PWM.setMotorModel(0, 0)
    # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
    except KeyboardInterrupt:
        destroy()
