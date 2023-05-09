#received help from Aniekan, Adam, Ann and Eric

from wpilib.drive import DifferentialDrive
import wpilib
from wpilib import TimedRobot, Joystick, Spark
from wpilib import Encoder

class Drivetrain(DifferentialDrive):
    def __init__(self):
        self.left_encoder = wpilib.Encoder(4,5)
        self.right_encoder = Encoder(6,7)
        self.left_motor = Spark(0)
        self.right_motor= Spark(1)
        self.drivetrain = DifferentialDrive(self.left_motor, self.right_motor)
        self.left_encoder.setDistancePerPulse(0.07 * math.pi/(12*120))
        self.right_encoder.setDistancePerPulse(0.07 * math.pi / (12 * 120))
        self.gyro= romi.RomiGyro()

    def move(self, forward, rotate):
        self.drivetrain.arcadeDrive(rotate,forward)

    def get_gyro_y(self):
        """
        Give the twist of the robot in degrees
        :return: current y in degrees
        """

        return self.gyro.getAngleY()

    def get_average_distance(self):
        return (self.left_encoder.getDistance() + self.right_encoder.getDistance())/2
    def reset_gyro(self):
        """
        Reset the gyro to 0 degrees
        """
        self.gyro.reset()

    def resetEncoders(self):
        self.left_encoders.reset()
        self.right_encoders.reset()
