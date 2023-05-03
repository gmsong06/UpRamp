from wpilib import TimedRobot, Joystick, Spark
import os
import wpilib
from drivetrain import Drivetrain

class MyRobot(TimedRobot) :

    def robotInit(self):
        '''This method is called as the robot turns on and is often used to setup the
        joysticks and other presets.'''
        self.controller = Joystick(0)
        self.drivetrain= Drivetrain()



    def robotPeriodic(self):
        '''This is called every cycle of the code. In general the code is loop
        through every .02 seconds.'''


    pass

    def autonomousInit(self):
        '''This is called once when the robot enters autonomous mode.'''

    1
    pass

    def autonomousPeriodic(self):
        #self.linefollower.run()

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