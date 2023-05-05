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
        self.drivetrain.left_encoder.reset()
        self.drivetrain.right_encoder.reset()

    def update_state(self):
        if self.drivetrain.get_gyro_y() < -1:  # going up ramp
            config.state = 1
        else:
            print(f"Distance is {self.drivetrain.get_average_distance()}")
            if self.drivetrain.get_average_distance() < -5000:
                config.state = 2
            else:
                config.state = 0

    def run(self):
        self.update_state()

        if config.state == 0:
            self.drivetrain.arcadeDrive(0, -1)
        elif config.state == 1:
            self.drivetrain.arcadeDrive(0, -0.5)
        else:
            self.drivetrain.arcadeDrive(0, 0)

        print(f"State is {config.state}")
