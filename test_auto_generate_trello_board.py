"""
Sample test to create a multiple board using trello util
"""
from trello_util import Trello_Util
from conf import key,token
import time
from data_conf import board_names,list_names,sample_board,sample_cards,member_ids,member_username,board_number,year,mm,dd
import pickle
import datetime
import pandas as pd

def test_trello_util(key,token):
    "Run api test to generate the boards"
    # Creating an object of Trello Util
    test_obj = Trello_Util(key,token)
    startdate = datetime.datetime(year,mm,dd)
    startdate = pd.to_datetime(startdate) - pd.DateOffset(days=7)   
    # Get the board names from conf
    new_board_number = board_number - 1    
    for board_name in board_names:        
        new_board_number = new_board_number + 1
        current_board_date = pd.to_datetime(startdate) + pd.DateOffset(days=7)
        new_board_name = str(new_board_number) + "." + str(board_name) + "("+ str(current_board_date.strftime("%d-%b-%Y")) + ")"
        startdate = current_board_date
        print (new_board_name)
    
        # Create a new board
        result_flag = test_obj.add_board(new_board_name)
        if result_flag == True:
            print ("Able to add card with name %s"% new_board_name)
        else :
            print ("Unable to add with name %s"% new_board_name)

        # Add list (swim lane) to board
        result_flag = test_obj.add_list(new_board_name,list_names)
        if result_flag == True:
            print ("Able to add list %s to board name %s"%(list_names,new_board_name))
        else :
            print ("Unable to add list %s to board name %s"%(list_names,new_board_name))

# Start of script:-
if __name__ == '__main__':
    test_trello_util(key=key,token=token)