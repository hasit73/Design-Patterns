"""
Template Method:

In Template pattern, an abstract class exposes defined way(s)/template(s)
to execute its methods. Its subclasses can override the method implementation
as per need but the invocation is to be in the same way as defined by an abstract class.
This pattern comes under behavior pattern category
"""

from abc import abstractmethod, ABC


class BaseCookies(ABC):
    """ It is Base class
        Only contains definition of methods.
        Don't have internal implementation.
    """

    def create_base_for_cookies(self):
        print("Base created for cookies ...")

    @abstractmethod
    def add_materials(self):
        pass

    @abstractmethod
    def bake_cookies(self):
        pass

    def get_cookies(self):
        self.create_base_for_cookies()
        self.add_materials()
        self.bake_cookies()


class VanillaCookies(BaseCookies):
    """ It is Child class
        Contains internal implementation for Vanilla cookies.
    """

    def add_materials(self):
        print("Milk and Vanilla power added.")

    def bake_cookies(self):
        print("Bake cookies for 10 minutes.")


class ChocolateCookies(BaseCookies):
    """ It is Child class
        Contains internal implementation for Chocolate cookies.
    """

    def add_materials(self):
        print("Milk and Chocolate power and chips added.")

    def bake_cookies(self):
        print("Bake cookies for 15 minutes.")


if __name__ == "__main__":

    cookie_type = input(
        "Type of cookie you want to bake ('vanilla' or 'chocolate')?"
        ).strip()

    if cookie_type == "vanilla":
        cookie = VanillaCookies()
        cookie.get_cookies()
    elif cookie_type == "chocolate":
        cookie = ChocolateCookies()
        cookie.get_cookies()
    else:
        print("Invalid Type entered! :(")
