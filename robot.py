from wpilib import TimedRobot, Joystick, Spark
import os
import wpilib
from robotcontainer import RobotContainer
from upramp import UpRamp
class MyRobot(TimedRobot):

    def robotInit(self,):
        self.container = RobotContainer()
        self.auto = UpRamp(self.container.drivetrain)
        self.pid_controller = PIDController(0.1, 0.0, 0.0)  # I will adjust these values as needed
        self.pid_controller.setSetpoint(0.0)


    def robotPeriodic(self):
        pass

    def autonomousInit(self):
        # self.auto = self.container.get_autonomous_routine()
        pass

    def autonomousPeriodic(self):
        self.auto.run()
        error = self.container.ramp_sensor.getVoltage() - self.container.ramp_threshold
        correction = self.pid_controller.calculate(error)
        self.container.drivetrain.driveDistance(10, 0.5 + correction)

    def teleopInit(self):
        pass

    def teleopPeriodic(self):
        forward = self.container.controller.getRawAxis(0)
        rotate = self.container.controller.getRawAxis(1)
        self.container.drivetrain.arcadeDrive(forward, rotate)


if __name__ == "__main__":
    os.environ["HALSIMWS_HOST"] = "10.0.0.2"
    os.environ["HALSIMWS_PORT"] = "3300"
    wpilib.run(MyRobot)
