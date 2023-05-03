from wpilib.drive import DifferentialDrive
import wpilib
import romi

class Drivetrain(DifferentialDrive):
    def __init__(self, left_motor, right_motor):
        super().__init__(left_motor, right_motor)
        self.left_motor = left_motor
        self.right_motor = right_motor
        self.gyro = romi.RomiGyro()
        self.accelerometer = wpilib.BuiltInAccelerometer()

    def move_forward(self, speed):
        self.arcadeDrive(0, speed)

    def get_gyro_y(self):
        """
        Give the twist of the robot in degrees
        :return: current y in degrees
        """

        return self.gyro.getAngleY()

    def reset_gyro(self):
        """
        Reset the gyro to 0 degrees
        """
        self.gyro.reset()
