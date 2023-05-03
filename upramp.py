from autoroutine import AutoRoutine
from drivetrain import Drivetrain
from wpimath.controller import PIDController
import config

class UpRamp(AutoRoutine):

    def __init__(self, drivetrain: Drivetrain):
        self.drivetrain = drivetrain
        self.pid_controller = PIDController(1/200, 1/1000, 0)
        self.pid_controller.setSetpoint(0)
        self.pid_controller.setTolerance(3)

    def update_state(self):
        if self.drivetrain.get_gyro_y() < 0:  # going up ramp
            config.state = 1
        else:
            config.state = 0

    def run(self):
        self.update_state()

        if config.state == 0:
            pass
        print(f"State is {config.state}")
