from wpilib.drive import DifferentialDrive
import wpilib
import romi
import math
class Drivetrain(DifferentialDrive):
    def __init__(self, left_motor, right_motor, left_encoder, right_encoder):
        super().__init__(left_motor, right_motor)
        self.left_motor = left_motor
        self.right_motor = right_motor

        self.left_encoder = left_encoder
        self.right_encoder = right_encoder

        self.left_encoder.setDistancePerPulse(0.07 * math.pi / (12 * 120))
        self.right_encoder.setDistancePerPulse(0.07 * math.pi / (12 * 120))

        self.left_encoder.reset()
        self.right_encoder.reset()

        self.gyro = romi.RomiGyro()

    def get_gyro_y(self):
        """
        Give the twist of the robot in degrees
        :return: current y in degrees
        """

        return self.gyro.getAngleY()

    def get_left_distance(self):
        return self.left_encoder.getDistance()

    def get_right_distance(self):
        return self.right_encoder.getDistance()

    def get_average_distance(self):
        return (self.left_encoder.getDistance() + self.right_encoder.getDistance())/2
    def reset_gyro(self):
        """
        Reset the gyro to 0 degrees
        """
        self.gyro.reset()
