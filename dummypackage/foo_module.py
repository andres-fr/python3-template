# -*- coding:utf-8 -*-


"""
Module containing a simple class with low memory and runtime requirements.
"""


from typing import Iterable


class Foo(object):
    """
    A simple class with low memory and runtime requirements.
    """

    def __init__(self, size: int = 1000000):
        """
        The instance will contain 2 small objects: 2*O(1) memory.
        """
        assert size > 0, "size has to be a positive int!"
        self._x: Iterable[int] = range(size)
        self._result: int = 0

    def _computation(self) -> None:
        """
        A simple computation in O(1).
        """
        self._result += 1

    def loop(self, times: int) -> None:
        """
        Restart result and run computation a number of times.

        :param times: non-negative number.
        :type times: int
        """
        self._result = 0
        for i in range(times):
            self._computation()

    def get_result(self) -> int:
        """
        This function does something.

        :returns: a number stored in ``self._result``
        :rtype: integer or float
        """
        # """
        # Basic getter.
        # :returns: the field stored in ``self._result``
        # """
        return self._result
