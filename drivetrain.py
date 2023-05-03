from wpilib.drive import DifferentialDrive
from wpilib import Spark
from wpimath.controller import PIDController
class Drivetrain:
    def __init__(self):
        self.left_motor= Spark(0)
        self.right_motor=Spark(1)
        self.drivetrain = DifferentialDrive(self.left_motor, self.right_motor)
        self.ramp_sensor = wpilib.AnalogInput(0)
        self.ramp_threshold =2.0
        self.pid_controller = PIDController(0.1, 0.0, 0.0)  #I will adjust these values as needed
        self.pid_controller.setSetpoint(0.0)

    def move(self, forward, rotate):
        self.drivetrain.arcadeDrive(forward, rotate)


    def getLeftEncoderCount(self) -> int:
        return self.leftEncoder.get()

    def getRightEncoderCount(self) -> int:
        return self.rightEncoder.get()

    def getLeftDistanceMeter(self) -> float:
        return self.leftEncoder.getDistance()

    def getRightDistanceMeter(self) -> float:
        return self.rightEncoder.getDistance()




