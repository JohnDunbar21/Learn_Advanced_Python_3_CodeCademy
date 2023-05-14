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
Create a file handler
"""
file_handler = logging.FileHandler("Logging\output.log")

"""
Create formatter objects for file and console logs
"""
file_formatter = logging.Formatter("[%(asctime)s] {%(levelname)s} %(name)s: #%(lineno)d - %(message)s")
console_formatter = logging.Formatter("[%(asctime)s] {%(levelname)s} - %(message)s")

"""
Set the formats of each handler
"""
file_handler.setFormatter(file_formatter)
stream_handler.setFormatter(console_formatter)

"""
Add the stream handler to the logger object
"""
logger.addHandler(stream_handler)

"""
Add the file handler to the logger object
"""
logger.addHandler(file_handler)

"""
Sets the default level of the logger object
"""
logger.setLevel(logging.DEBUG)

"""
Division function
"""        
def division():
  try:
    dividend = float(input("Enter the dividend: "))
    logger.info(f"The dividend entered is: {dividend}")
    divisor = float(input("Enter the divisor: "))
    logger.info(f"The divisor entered is: {divisor}")
  except ValueError:
    logger.log(logging.CRITICAL, "No dividend or divisor value entered!")
    return None
  if divisor == 0:
    logger.error("Attempting to divide by 0!")
    return None
  else:
    return dividend/divisor

result = division()

if result == None:
  logger.warning("The result value is None!")
else:
    print(result)