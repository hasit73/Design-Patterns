"""
Strategy Pattern:

In Strategy pattern, a class behavior or its algorithm can be changed at run time.
This type of design pattern comes under behavior pattern.
"""


class SumNumbers:
    """ Class to sum two numbers """
    def sum_input(self, num1, num2):
        """ Add two numbers """
        return num1 + num2


class SumList:
    """ Class to sum numbers of list """

    def sum_input(self, *args):
        """ Add all list numbers. """
        return sum(args)


class SumString:
    """ Class to concate strings """
    def sum_input(self, *args):
        result = ""
        for s in args:
            result += s
        return result


class Context:
    """ Class that refer various class to perform similar operations. """

    def __init__(self, strategy):
        self.strategy = strategy

    def do_summation(self, *args):
        return self.strategy.sum_input(*args)


if __name__ == "__main__":

    c1 = Context(SumString())
    print(c1.do_summation("Happy ", "Coding"))

    c2 = Context(SumList())
    print(c2.do_summation(2, 5, 9, 87))
