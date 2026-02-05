#!/usr/bin/python3
""" Mixins: SwimMixin + FlyMixin, then Dragon """


class SwimMixin:
    """Provide swimming ability."""
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """Provide flying ability."""
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon can swim and fly via mixins."""
    def roar(self):
        print("The dragon roars!")
