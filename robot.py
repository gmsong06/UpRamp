from wpilib import TimedRobot, Joystick, Spark
import os
import wpilib
from robotcontainer import RobotContainer
from upramp import UpRamp
class MyRobot(TimedRobot):

    def robotInit(self,):
        self.container = RobotContainer()
        #self.auto = UpRamp(self.container.drivetrain)



    def robotPeriodic(self):
        pass

    def autonomousInit(self):
        self.auto = self.container.get_autonomous_routine()
        pass

    def autonomousPeriodic(self):
        self.auto.run()


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
