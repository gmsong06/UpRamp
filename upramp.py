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
        elif self.drivetrain.get_average_distance() > 5000:  # reached top of ramp
            config.state = 2
        else:
            config.state = 0

    def run(self):
        self.update_state()

        if config.state == 0:
            # calculate the correction using the PID controller
            error = self.drivetrain.left_encoder.getDistance() - self.drivetrain.right_encoder.getDistance()
            correction = self.pid_controller.calculate(error)
            # drive straight with correction
            self.drivetrain.arcadeDrive(0.25, 0.5 + correction)
        elif config.state == 1:
            # lower the speed but still drive straight (adjust the speed as needed)
            self.drivetrain.arcadeDrive(0.5, -0.2)
        else:
            # stop the robot
            self.drivetrain.arcadeDrive(0, 0)

        print(f"State is {config.state}")