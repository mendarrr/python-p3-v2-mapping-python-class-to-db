# lib/config.py
import sqlite3

CONN = sqlite3.connect('company.db') #Constant equal to a hash that contains  a connection to the database
CURSOR = CONN.cursor() # A constant that allows one to interact with the database and execute SQL statements
