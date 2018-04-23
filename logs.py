""" This module contains convenience methods for logging output from
Caladrius."""

import logging

from sys import stdout

def set_up_logging(logfile: str = None, debug: bool = False) -> None:
    """ This will set up the root Python logger instance and by default will
    attach a stream handler piping all output to stdout. However an optional
    output filename can be specified to preserve the logs. The dubug argument
    will set the log level to DEBUG and will included line numbers and function
    name information in the log output.

    Arguments:
        logfile (str):  Optional path to the output file for the logs.
        debug (bool):   Optional flag (default False) to include debug level
                        output.
    """

    top_log: logging.Logger = logging.getLogger()

    if debug:
        top_log.setLevel(logging.DEBUG)
        formatter = logging.Formatter(("{levelname} | {name} | "
                                       "function: {funcName} "
                                       "| line: {lineno} | {message}"),
                                      style='{')
    else:
        top_log.setLevel(logging.INFO)
        formatter = logging.Formatter(("{asctime} | {name} | {levelname} "
                                       "| {message}"), style='{')

    console_handler: logging.StreamHandler = logging.StreamHandler(stdout)
    console_handler.setFormatter(formatter)
    top_log.addHandler(console_handler)

    if logfile:
        file_handler: logging.FileHandler = logging.FileHandler(logfile)
        file_handler.setFormatter(formatter)
        top_log.addHandler(file_handler)
