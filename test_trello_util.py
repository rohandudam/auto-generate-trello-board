"""
Sample test to Create a board using trello util
"""
from trello_util import Trello_Util
from conf import key,token
import time
from data_conf import board_name,list_names,sample_board,sample_cards,member_ids,member_username
import pickle
import datetime
import pandas as pd

def test_trello_util(key,token):
    # Creating an object of Trello Util
    test_obj = Trello_Util(key,token)
    # Get the board names from conf
    board_names=board_name
    date = pd.to_datetime(startdate) + pd.DateOffset(days=7)
    new_board_name = str(board_number) + "." + str(board_names[0]) + "("+ str(date.strftime("%d-%b-%Y")) + ")"
    print (new_board_name)
    
    # Create a new board
    result_flag = test_obj.add_board(new_board_name)
    if result_flag == True:
        print ("Able to add card with name %s"% new_board_name)
    else :
        print ("Not able to add with name %s"% new_board_name)
    
    # Add list (swim lane) to board
    result_flag = test_obj.add_list(new_board_name,list_names)
    if result_flag == True:
        print ("Able to add list %s to board name %s"%(list_names,new_board_name))
    else :
        print ("Not able to add list %s to board name %s"%(list_names,new_board_name))

if __name__ == '__main__':
    test_trello_util(key=key,token=token)
