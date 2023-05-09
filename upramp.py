#received help from Aniekan, Adam, Ann and Eric

from autoroutine import AutoRoutine
from drivetrain import Drivetrain
from wpimath.controller import PIDController
import config
import romi
class UpRamp(AutoRoutine):

    def __init__(self, drivetrain: Drivetrain):
        self.drivetrain = drivetrain
        self.rampState = 0
        self.flatSurfaceSpeed= 0.6
        self.rampSpeed= 0.8
        self.pid_controller = PIDController(20, 0, 0)
        self.pid_controller.setSetpoint(0)
        self.pid_controller.setTolerance(0.05)
        self.gyroAngleYThreshold = 5

    def run(self):
        difference = self.drivetrain.left_encoder.getDistance() - self.drivetrain.right_encoder.getDistance()
        rotate = self.pid_controller.calculate(difference)
        if self.rampState == 0:
            self.drivetrain.move(self.flatSurfaceSpeed, rotate)
            if self.drivetrain.getGyroAngleY()> self.gyroAngleYThreshold:
                self.rampState = 1
                self.pid_controller.setTolerance(0.2)
        elif self.rampState == 1:
            self.drivetrain.move(self.rampSpeed, rotate)
            if self.drivetrain.getGyroAngleY() < self.gyroAngleYThreshold:
                self.rampState = 2
        else:
            self.drivetrain.move(0,0)

        print(f"State is {config.state}")