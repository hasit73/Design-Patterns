"""
State Pattern

In State pattern a class behavior changes based on its state.
This type of design pattern comes under behavior pattern.
"""


class Fan:
    def __init__(self):
        self.current_state = None
        self.current_state_name = None

    def set_state(self, context):
        self.current_state = context

    def get_state(self):
        print(f"Current state is {self.current_state.state}")


class TurnON:
    """ Turn on Fan """
    def __init__(self):
        self.state = "ON"

    def act(self, fan):
        fan.set_state(self)    


class TurnOFF:
    """ Turn off Fan """
    def __init__(self):
        self.state = "OFF"

    def act(self, fan):
        fan.set_state(self)    


if __name__ == "__main__":
    fan = Fan()

    turn_on = TurnON()
    turn_on.act(fan)
    fan.get_state()

    turn_off = TurnOFF()
    turn_off.act(fan)
    fan.get_state()

    turn_on.act(fan)
    fan.get_state()
