import random
import logging
import sys
from datetime import datetime

logger = logging.getLogger(__name__)
stream_handler = logging.StreamHandler(sys.stdout)
file_handler = logging.FileHandler("Logging\ATM_Logger_Project\output.log")

"""
Create formatter objects for file and console logs
"""
file_formatter = logging.Formatter("[%(asctime)s] {%(levelname)s} %(name)s: #%(lineno)d - %(message)s")
console_formatter = logging.Formatter("[%(asctime)s] {%(levelname)s} - %(message)s")

file_handler.setFormatter(file_formatter)
stream_handler.setFormatter(console_formatter)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)

logger.setLevel(logging.INFO)

class BankAccount:
  def __init__(self):
    self.balance=100
    print("Hello! Welcome to the ATM Depot!")
    
  def authenticate(self):
    while True:
      pin = int(input("Enter account pin: "))
      logger.info(f"Attempting to access account...")
      if pin != 1234:
        logger.log(logging.ERROR, "Error! Invalid pin. Try again.")
      else:
        return None
 
  def deposit(self):
    try:
      amount=float(input("Enter amount to be deposited: "))
      logger.info(f"Amount to be deposited into account: ${amount}")
      if amount < 0:
        logger.log(logging.WARNING, "Warning! You entered a negative number to deposit.")
      self.balance += amount
      logger.info(f"Amount Deposited: ${amount}")

      number=random.randint(10000, 1000000)


      logger.info(f"Transaction Info:\nStatus: Successful\nTransaction #{number}")
    except ValueError:
      logger.warning("Error! You entered a non-number value to deposit.")

      number=random.randint(10000, 1000000)

      logger.info(f"Transaction Info:\nStatus: Failed\nTransaction #{number}")
 
  def withdraw(self):
    try:
      amount = float(input("Enter amount to be withdrawn: "))
      if self.balance >= amount:
        self.balance -= amount
        number=random.randint(10000, 1000000)
        logger.info(f"You withdrew: ${amount}")

        logger.info(f"Transaction Info:\nStatus: Successful\nTransaction #{number}")
      else:
        
        logger.warning("Error! Insufficient balance to complete withdraw.")
        number=random.randint(10000, 1000000)
        logger.info(f"Transaction Info:\nStatus: Failed\nTransaction #{number}")
    except ValueError:
      logger.warning("Error! You entered a non-number value to withdraw.")

      number=random.randint(10000, 1000000)
      logger.info(f"Transaction Info:\nStatus: Failed\nTransaction #{number}")
 
  def display(self):
    logger.info(f"Available Balance = ${self.balance}")
 
acct = BankAccount()
acct.authenticate()
acct.deposit()
acct.withdraw()
acct.display()