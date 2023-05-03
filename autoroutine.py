from typing import Protocol

class AutoRoutine(Protocol):
    def run(self):
        pass

    def reset(self):
        pass