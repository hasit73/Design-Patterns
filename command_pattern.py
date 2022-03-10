"""
Command Pattern:

Use to decouple communication between sender and receiver.

Provide one abstraction layer.

Command pattern is a data driven design pattern and falls under behavioral pattern category.
A request is wrapped under an object as command and passed to invoker object.
Invoker object looks for the appropriate object which can handle this command
and passes the command to the corresponding object which executes the command.
"""
from abc import ABC, abstractmethod


class Command(ABC):
    """ Abstract Command class"""

    def __init__(self, receiver):
        self.receiver = receiver

    @abstractmethod
    def process(self):
        """ Abstract method """
        pass


class NormalCommand(Command):
    """ NormalCommand class call normal processes of receiver
        Works at Intermediate level (Server or App level)
    """

    def __init__(self, receiver):
        self.receiver = receiver

    def process(self):
        """ Call normal processes of receiver. """
        self.receiver.normal_process()


class CriticalCommand(Command):
    """ CriticalCommand class call critical processes of receiver
        Works at Intermediate level (Server or App level)
    """

    def __init__(self, receiver):
        self.receiver = receiver

    def process(self):
        """ Call critical processes of receiver. """
        self.receiver.critical_process()


class ReceiverOne:
    """ Receiver class that perform some operations
        Works at Low level (Server or App level)
    """
    def __init__(self):
        self.name = "Receiver-1"

    def normal_process(self):
        """
        This function contains normal processes
        """
        print(f"Normal processes of {self.name} has been started ...")

    def critical_process(self):
        """
        This function contains critical processes
        """
        print(f"Critical processes of {self.name} has been started ...")


class ReceiverTwo:
    """ Receiver class that perform some operations
        Works at Low level (Server or App level)
    """
    def __init__(self):
        self.name = "Receiver-2"

    def normal_process(self):
        """
        This function contains normal processes
        """
        print(f"Normal processes of {self.name} has been started ...")

    def critical_process(self):
        """
        This function contains critical processes
        """
        print(f"Critical processes of {self.name} has been started ...")


class Invoker:
    """ Invoker class that invoke the commands
        Works at High level (Client-User level)
    """
    def __init__(self, command):
        self.command = command

    def execute(self):
        """ Call to the process method of command class"""
        self.command.process()


if __name__ == "__main__":

    # create object of both the receiver class.
    receiver1 = ReceiverOne()
    receiver2 = ReceiverTwo()

    # create object of command class
    normal_command_handler_for_r2 = NormalCommand(receiver2)
    critical_command_handler_for_r1 = CriticalCommand(receiver1)

    # create invoker to invoke method
    Invoker(normal_command_handler_for_r2).execute()
    Invoker(critical_command_handler_for_r1).execute()
