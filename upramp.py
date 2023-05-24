from autoroutine import AutoRoutine
from drivetrain import Drivetrain
from wpimath.controller import PIDController
import config

class UpRamp(AutoRoutine):

    def __init__(self, drivetrain: Drivetrain):
        self.drivetrain = drivetrain
        self.pid_controller = PIDController(21, 0, 0)
        self.pid_controller.setSetpoint(0)
        self.pid_controller.setTolerance(.05)
        self.drivetrain.left_encoder.reset()
        self.drivetrain.right_encoder.reset()

    def update_state(self):
        if self.drivetrain.get_gyro_y() < -5:  # going up ramp
            config.state = 1
        else:
            if config.state == 1:
                config.state = 2

    def run(self):
        encoder_error = self.drivetrain.get_left_distance() - self.drivetrain.get_right_distance()
        rotation = self.pid_controller.calculate(encoder_error)

        if self.pid_controller.atSetpoint():
            rotation = 0

        self.update_state()

        if config.state == 0:
            self.drivetrain.arcadeDrive(rotation, -1)
        elif config.state == 1:
            self.drivetrain.arcadeDrive(rotation, -.5)
        else:
            self.drivetrain.arcadeDrive(0, 0)

        print(f"State is {config.state}")
