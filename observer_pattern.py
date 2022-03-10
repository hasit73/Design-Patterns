"""
Observer Design Pattern

Observer pattern is used when there is one-to-many relationship between objects
such as if one object is modified, its depenedent objects are to be notified automatically.
Observer pattern falls under behavioral pattern category.
"""


class Viewer:
    """ Simple Viewer class
        Each viewer works as Observer.
    """

    def __init__(self, name: str):
        self.name = name

    def recommends(self, video, author):
        print(
            f"Recommend-{self.name}: New video '{video}' added by '{author}'"
            )


class YoutubeChannel:
    """ YoutubeChannel class contains various functionalties
        And these features works as Subject.
        Ex: Get notification event is a Subject.
    """
    def __init__(self, author):
        # author of channel
        self.author = author
        # list of subscribers
        self.__subscribers = []
        # list of videos.
        self.__videos = []

    def subscribe(self, user: Viewer):
        """ Given user will be added in the list of subscribers """
        self.__subscribers.append(user)

    def unsubscribe(self, user: Viewer):
        """ Given user will be removed from the list of subscribers """
        self.__subscribers.remove(user)

    def upload_video(self, title):
        """ Upload new video """
        print(
            f"New video {title} uploaded!"
            )
        # append video in list of videos.
        self.__videos.append(title)
        # sent notification to the subscribers.
        self.notify_viewers(title)

    def notify_viewers(self, title):
        """ Send notification to each users who subscribered this channel"""
        for subscriber in self.__subscribers:
            subscriber.recommends(title, self.author)


if __name__ == "__main__":

    # create two viewers.
    bob = Viewer("Bob")
    joy = Viewer("joy")
    # create one youtube channel.
    python_programming = YoutubeChannel("Python-Programming")

    # subscribe youtube channel
    python_programming.subscribe(bob)
    python_programming.subscribe(joy)
    # upload new video
    python_programming.upload_video("Introduction to Design Patterns")
    # unsubscribe channel
    python_programming.unsubscribe(bob)
    # upload another video
    python_programming.upload_video("Factory Design Pattern")
    # add new user
    michel = Viewer("Michel")
    python_programming.subscribe(michel)
    python_programming.upload_video("Observer Design Pattern")
