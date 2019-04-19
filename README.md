-----------------
Our test will automate the creation of a Trello board, along with other provided details like trello card, members with a duration set to 1 week.
-----------------

--------
A Python Trello API utility script to create Trello Boards, Cards, add members and many other things.
--------
You can use this script to :

1. Create Trello Boards

2. Assign people to Board

3. Create Trello Cards

4. Assign people to card

5. Copy cards 

6. Add list items to a board

7. Change preference or visibility

You can refer to blog(https://qxf2.com/blog/python-trello-api-utility-script/) for more details. We have used Python Request module to make the API calls.

------
Setup 
------
a) Install the requirements
pip install -r requirements.txt
b) Generate the API key and token by following this link https://trello.com/app-key
c) Update the Trello API Key and Token in the conf.py file
d) Update the required data like board names, list names, date, card name, member names in the data_conf.py

If you ran into some problems on step (d), please report them as an issue or email Avinash(avinash@qxf2.com)

This script will run only on Python3.
---------------------------
COMMANDS FOR RUNNING SCRIPT
---------------------------

python test_auto_generate_trello_board.py


--------
ISSUES?
--------

a) If Python complains about an "Import" exception, please 'pip install $module_name'
