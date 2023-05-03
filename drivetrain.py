from wpilib.drive import DifferentialDrive
from wpilib import Spark
class Drivetrain:
    def __init__(self):
        self.left_motor= Spark(0)
        self.right_motor=Spark(1)
        self.drivetrain = DifferentialDrive(self.left_motor, self.right_motor)

    def move(self, forward, rotate):
        self.drivetrain.arcadeDrive(forward, rotate)
