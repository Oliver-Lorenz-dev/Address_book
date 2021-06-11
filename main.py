# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 15:44:44 2020

@author: Oliver Lorenz
"""
import sys

sys.path.append(".")
from address_book import Address
T=Address('address_test_file.txt')

# Test read_file function:
'''input 7 into the command prompt to stop the address book running
then the following tests will be carried out in order'''
address_list_test=['Oliver Lorenz 1 Park_Terrace 0755555555 06-04']
# this list is the contents of the test file used
T.read_file()
if T.get_address_list() == address_list_test:
    print('Read_file Test Successful')
else:
    print('Read_file Test Failed')

#test add_address function:
'''This test was done by inputting the following address into the 
prompt Oliver Lorenz 1 Park_Drive 077777777 06-06'''
address_list_test_2 = ['Oliver Lorenz 1 Park_Terrace 0755555555 06-04','Oliver Lorenz 1 Park_Drive 077777777 06-06']
T.add_address()
T.read_file()
if T.get_address_list() == address_list_test_2:
    print('add_address test successful')
else:
    print('add_address test failed')

#test delete_address function:
'''this delete address function searches for and deletes the
Oliver Lorenz 1 Park_Terrace 0755555555 06-04 address to do this
input this address into the search then input yes to delete it'''
address_list_test_3 =['Oliver Lorenz 1 Park_Drive 077777777 06-06']
T.delete_address()
T.read_file()
if T.get_address_list() == address_list_test_3:
    print('Delete_address test Successful')
else:
    print('Delete_address test Failed')

#test search_address function:
'''search input is Oliver, output should be 
Oliver Lorenz 1 Park_Drive 077777777 06-06'''
T.search_address()
if T.get_search_list() == address_list_test_3:
    print('search_address test successful')
else:
    print('search_address test failed')

#test advanced_search function:
'''input number 2 and search input is Lorenz'''
T.advanced_search()
if T.get_advanced_search_list() == address_list_test_3:
    print('advanced_search test successful')
else:
    print('advanced_search test failed')

#change_address test:
'''at the search input prompt, input Oliver, then input yes when asked to
change address. 
Then input the following: Oliver Lorenz 1 Park_Terrace 0755555555 06-04'''

T.change_address()
T.read_file()
if T.get_address_list() == address_list_test:
    print('change_address test successful')
else:
    print('change_address test failed')
