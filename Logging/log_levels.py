"""
Importing the logging module
"""
import logging

LOG_LEVELS = {"NOTSET": 0, "DEBUG": 10, "INFO": 20, "WARNING": 30, "ERROR": 40, "CRITICAL": 50}

for key, value in LOG_LEVELS.items():
    print(f"Log level {key} has a value of {value} \n")