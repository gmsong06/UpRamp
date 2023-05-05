from wpilib import TimedRobot, Joystick, Spark, AnalogInput, PIDController
import os
import wpilib
from drivetrain import Drivetrain
from gyroturn import GyroTurn

class MyRobot(TimedRobot) :

    def robotInit(self):
        '''This method is called as the robot turns on and is often used to setup the
        joysticks and other presets.'''
        self.controller = Joystick(0)
        self.drivetrain= Drivetrain()
        self.ramp_sensor = wpilib.AnalogInput(0)
        self.ramp_threshold = 2.0
        self.pid_controller = PIDController(0.1, 0.0, 0.0)  # I will adjust these values as needed
        self.pid_controller.setSetpoint(0.0)
        self.on_ramp = False

    def robotPeriodic(self):
        '''This is called every cycle of the code. In general the code is loop
        through every .02 seconds.'''
        if self.on_ramp:
            error = self.ramp_sensor.getVoltage() - self.ramp_threshold
            correction = self.pid_controller.calculate(error)
            self.drivetrain.arcadeDrive(0.5, correction)

    pass

    def autonomousInit(self):
        '''This is called once when the robot enters autonomous mode.'''
        self.drive.setSafetyEnabled(False)
    pass

    def autonomousPeriodic(self):
        if not self.on_ramp:
            # Drive up the ramp until the threshold is crossed
            if self.ramp_sensor.getVoltage() >= self.ramp_threshold:
                self.on_ramp = True
        else:
            # Stop the robot once it reaches the top of the ramp
            self.drivetrain.stop()

        '''This is called every cycle while the robot is in autonomous.'''

    def teleopInit(self):
        pass

    def teleopPeriodic(self):
        forward = self.controller.getRawAxis(0)
        rotate = self.controller.getRawAxis(1)
        self.drivetrain.arcadeDrive(forward, rotate)
        self.drivetrain.move(forward,rotate)
        print(forward)
        print(rotate)



if __name__ == "__main__":
    os.environ["HALSIMWS_HOST"] = "10.0.0.2"
    os.environ["HALSIMWS_PORT"] = "3300"
    wpilib.run(MyRobot)