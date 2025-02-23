class FPLException(Exception):
    """Base exception for all FPL exceptions"""


class FPLUnauthenticatedException(FPLException):
    """FPLUnauthenticatedException raised whenever we recieve a 403 from the fpl api"""
