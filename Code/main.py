import cv2
import time
from Motor import *
from Servo import *
from lane_detection_final import *

PWM = Motor()
SRV = Servo()


def move2(ave_lines, frame):
    height, width, _ = frame.shape
    x_offset, y_offset = None, None

    try:
        if len(ave_lines) == 0:
            PWM.setMotorModel(0, 0)  # m 30, 30
            SRV.setServoPwm("4", 90)
            print("no lines within ave lines")
            return None

        # both lane lines

        elif average_line[1] is None and average_line[0] is not None:
            x1, _, x2, _ = average_line[0][0]
            x_offset = x2 - x1
            y_offset = int(height / 2)
            steering_angle = radian_to_degree(x_offset, y_offset)
            PWM.setMotormodel(40, 40)
            SRV.setServoPwm("4", steering_angle)
            print(" Moving under the left line detection condition")

        elif average_line[0] is None and average_line[1] is not None:
            x1, _, x2, _ = average_line[1][0]
            x_offset = x2 - x1
            y_offset = int(height / 2)
            steering_angle = radian_to_degree(x_offset, y_offset)
            PWM.setMotormodel(40, 40)
            SRV.setServoPwm("4", steering_angle)
            print(" Moving under the right line detection")

        else:
            _, _, left_x2, _ = average_line[0][0]
            _, _, right_x2, _ = average_line[1][0]
            camera_mid_offset_percentage = 0.00
            mid = int((width / 2) * (1 + camera_mid_offset_percentage))

            x_offset = (left_x2 + right_x2) / 2 - mid
            y_offset = int(height / 2)
            steering_angle = radian_to_degree(x_offset, y_offset)
            # left, right, reft correction, right correction
            PWM.setMotorModel(30, 30)
            SRV.setServoPwm("4", steering_angle)
            print("steering_angle", steering_angle, "Moving under the both line detection condition")

    except Exception as e:
        print("Error", e)


if __name__ == '__main__':

    SRV.setServoPwm("4", 90)
    time.sleep(1)
    frame_count = 0
    video = cv2.VideoCapture(-1)
    fps = video.get(cv2.CAP_PROP_FPS)
    print("Frames per second Camera:{0}".format(fps))
    angle = None

    try:
        if input("Command for starting  the motor :" + " ") == "start":

            while True:
                res, frame = video.read()
                if res is False:
                    continue
                frame_count += 1
                if frame_count % 1 != 0:
                    continue
                frame = cv2.rotate(frame, cv2.ROTATE_180)
                frame = cv2.resize(frame, (480, 320), interpolation=cv2.INTER_AREA)
                average_line = detect_lane2(frame)

                move2(average_line, frame)

                if cv2.waitKey(1) == ord('q'):
                    break

        else:
            print("Enter the correct passwords")

        # Clean up
        video.release()
        cv2.destroyAllWindows()

    except KeyboardInterrupt:
        destroy()
