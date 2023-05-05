import wpilib
from drivetrain import Drivetrain
from wpilib import Spark, Encoder
from autoroutine import AutoRoutine
from upramp import UpRamp

class RobotContainer:

    def __init__(self):
        self.controller = wpilib.Joystick(0)
        self.drivetrain = Drivetrain(Spark(0), Spark(1), Encoder(4, 5), Encoder(6, 7))
        self.chooser = wpilib.SendableChooser()
        self._configure()

    def _configure(self):
        self.chooser.addOption("Up Ramp", UpRamp(self.drivetrain))
        wpilib.SmartDashboard.putData("Auto Chooser", self.chooser)

    def get_autonomous_routine(self) -> AutoRoutine:
        print(self.chooser.getSelected())
        return self.chooser.getSelected()