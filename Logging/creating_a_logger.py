"""
Importing the logging and sys modules
"""
import logging
import sys

"""
Create a logger object and a stream handler
"""
logger = logging.getLogger(__name__)
stream_handler = logging.StreamHandler(sys.stdout)

"""
Add the stream handler to the logger object
"""
logger.addHandler(stream_handler)