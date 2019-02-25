# -*- coding:utf-8 -*-


"""
Module containing a simple class with low memory and runtime requirements.
"""


class Foo(object):
    """
    A simple class with low memory and runtime requirements.
    """

    def __init__(self, size=1000000):
        """
        The instance will contain 2 small objects: 2*O(1) memory.
        """
        assert size > 0, "size has to be a positive int!"
        self._x = range(size)
        self._result = 0

    def _computation(self):
        """
        A simple computation in O(1).
        """
        self._result += 1

    def loop(self, times):
        """
        Restart result and run computation a number of times.
        :param times: The number of times, expected non-negative int.
        """
        self._result = 0
        for i in range(times):
            self._computation()

    def get_result(self):
        """
        Basic getter.
        :returns: the field stored in ``self._result``
        """
        return self._result
