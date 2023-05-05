from autoroutine import AutoRoutine
from wpimath.controller import PIDController


class DriveStraight(AutoRoutine):

    def __init__(self, drivetrain, goal_in_meters):
        # PID controller for straight driving
        self.drivetrain = drivetrain
        self.goal = goal_in_meters
        self.pid_controller=PIDController(20, 0, 0)
        self.pid_controller.setSetpoint(0)
        self.pid_controller.setTolerance(.05)
        self.pid_controller.setContinuous()
        self.pid_controller.enable()

        # PID controller for distance traveled
        self.distance_pid = PIDController(Kp=0.5, Ki=0.0, Kd=0.0)
        self.distance_pid.setSetpoint(self.goal)
        self.distance_pid.setInputRange(0, 100)  # maximum 100 meters
        self.distance_pid.setOutputRange(-1, 1)
        self.distance_pid.setAbsoluteTolerance(0.1)
        self.distance_pid.enable()



    def run(self):

        difference = self.drivetrain.getLeftDistanceMeter() - self.drivetrain.getRightDistanceMeter()
        rotate = self.rotate_controller.calculate(difference)
        if self.rotate_controller.atSetpoint():
            rotate = 0

        distance_error = self.goal - self.drivetrain.averageDistanceMeter()
        forward = self.distance_controller.calculate(distance_error)
        if self.distance_controller.atSetpoint():
            forward = 0

        print(
            f"Fwd: {forward}, Rot: {rotate} distance:{self.drivetrain.averageDistanceMeter()} difference:{difference}")
        self.drivetrain.arcadeDrive(rotate, forward)