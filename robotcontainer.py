import wpilib
from drivetrain import Drivetrain
from wpilib import Spark
from autoroutine import AutoRoutine

class RobotContainer:

    def __init__(self):
        self.controller = wpilib.Joystick(0)
        self.drivetrain = Drivetrain(Spark(0), Spark(1))
        self.chooser = wpilib.SendableChooser()
        self._configure()

    def _configure(self):
        wpilib.SmartDashboard.putData("Auto Chooser", self.chooser)

    def get_autonomous_routine(self) -> AutoRoutine:
        return self.chooser.getSelected()