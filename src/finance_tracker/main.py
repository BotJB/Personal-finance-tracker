"""
This project analysis the money expenditure
"""
from finance_tracker.database.connection import test_connection
def main():
    print("we are in the main function")
    if test_connection():
        print('Data base succesfully connected')
    else:
        print('Database not connected')    

if __name__ =="__main__":
    main()    