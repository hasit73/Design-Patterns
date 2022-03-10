"""
Mediator Pattern:
    Provide common interface to interact with other class objects.
    reduce coupling of system.

Mediator pattern is used to reduce communication complexity between multiple objects or classes.
This pattern provides a mediator class which normally handles all the communications
between different classes and supports easy maintenance of the code by loose coupling.
Mediator pattern falls under behavioral pattern category.
"""

import datetime


class User:
    """ User class maintain state of user.
    """

    def __init__(self, name):
        """ Initialize & store user information """
        self.name = name
        self.last_message = ""
        self.last_message_time = None
        self.last_message_sender_name = ""

    def print_received_message(self):
        """ Print lastly received message along
            with timestamp and sender name
        """
        print(f"[{self.last_message_time}] - Sent by - " +
              f"{self.last_message_sender_name}")
        print(f"Message : {self.last_message}")


class MessageMediator:
    """ Message Mediator that work as medium between users
        Users can share their messages with mediator and mediator
        share it with receiver.
    """
    def send_message(self, sender, message, receiver):
        """ Transfer message and other information
            from sender to receiver.
        """
        receiver.last_message = message
        receiver.last_message_sender_name = sender.name
        receiver.last_message_time = datetime.datetime.now()

        receiver.print_received_message()


if __name__ == "__main__":

    """ Demostrate classes and check its working """
    sanket = User("Sanket")
    govind = User("Govind")
    mediator = MessageMediator()
    mediator.send_message(sanket, "Hii Govind! How are you ?", govind)
    mediator.send_message(govind, "Hii, I am fine", sanket)
