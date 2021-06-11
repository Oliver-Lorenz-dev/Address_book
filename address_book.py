# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 15:01:55 2020

@author: Oliver Lorenz
"""
import re
match_pattern = "[A-Za-z]+\s+[a-zA-Z]+\s+[0-9]+\s+[A-Za-z\_]+\s+[0-9]+\s+[0-9\-]"
class Address:
    def __init__(self, file):
        '''constructor for Address class'''
        self.__file = file
        self.__address_list = []
        self.__search_list =[]
        self.__advanced_search_list=[]
        
    def get_address_list(self):
        '''function returns address_list variable'''
        return self.__address_list
    
    
    def get_search_list(self):
        '''function returns search_list variable'''
        return self.__search_list
    
    
    def get_advanced_search_list(self):
        '''function returns advanced_search_list variable'''
        return self.__advanced_search_list
    
    
    def read_file(self):
        '''function which reads in a file'''
        self.__address_list = []
        with open(self.__file,'r+') as f:
            data = f.readlines()
            for line in data:
                self.__address_list.append(line.strip()) 
                # output file contents to list
            return self.__address_list
        
        
    def view_all(self): 
        '''allows user to view all entries in the address list'''
        with open(self.__file,'r+') as f:
            # read file in again incase any modifications have been made
            data = f.readlines() 
            for line in data:
                n=line.strip()# remove spaces and newline characters
                print(n)
             
                
    def add_address(self):
        '''function which allows the user to add an entry to the address file'''
        correct_input = False
        with open(self.__file,'a') as f:
            # open file with append, so file not overwritten
            while not correct_input:
                print('Input example: Oliver Lorenz 1 Park_Drive 0755555555 06-04') 
                address_input = input('Please input your chosen address in the format shown above: ')
                if not re.match(match_pattern,address_input):
                    print('Please follow correct input example')
                    correct_input = False
                    continue
                else:
                    f.write(address_input + '\n') 
                # add new line to make sure all inputs are on separate lines
                    correct_input = True # break while loop on correct input
                  
                    
    def search_address(self):
        '''function that searches for any addresses containing 
        the users search input'''
        self.__search_list =[]
        with open(self.__file,'r+') as f: 
            # read file in again incase any modifications have been made
            data = f.readlines()
            address_found = False #set variable as false
            print('Input example: Oliver Lorenz 1 Park_Drive 0755555555 06-04') 
            # tells user how the file is formatted
            search = input('Please search for an address: ')
            for line in data:
                n=line.strip()
                if search.lower() in line.lower(): 
                    # use .lower to ignore case sensitivity
                    address_found = True
                    print(n)
                    self.__search_list.append(n)
                    continue 
        # go to next iteration of the for loop, ie the next line of the file
            if not address_found:
                print('No address found')
                # tell the user their search was unsuccessful
        return self.__search_list
    
    
    def delete_address(self): 
        '''function that deletes an address of the user's choice'''
        with open(self.__file,'r+') as f:
            data = f.readlines()
            address_found = False
            index=-1 # variable to keep track of the line number
            print('Input example: Oliver Lorenz 1 Park_Drive 0755555555 06-04') 
            # tells user how the file is formatted
            search = input('Please search for an address: ')
            for line in data:
                index+=1
                n=line.strip()
                if search.lower() in line.lower():
                    # use .lower to avoid case sensitivity
                    address_found = True
                    print(n)
                if address_found: #ask user if they want to delete address
                    del_choice = input('Address found, do you want to delete this address? Input Yes or No: ')
                    if del_choice.lower() == 'yes':
                        del data[index] #delete address
                        print('Address Deleted')
                    with open(self.__file,'w') as f: 
                # write all addresses except the deleted address to the file
                        for line in data:
                            f.write(line) 
                else: 
                # if address not found continue to next iteration of for loop
                    continue
                
                break
            if not address_found:
                print('No address found') 
                # tell the user their search was unsuccessful
                
                
    def change_address(self): 
        '''function allows user to change an address entry'''
        correct_input = False
        with open(self.__file,'r') as f: 
            # open file with append, so file not overwritten
            data = f.readlines()
            address_found = False
            index=-1 # variable to keep track of the line number
            print('Input example: Oliver Lorenz 1 Park_Drive 0755555555 06-04') 
            search = input('Please search for an address: ')
            for line in data:
                index+=1
                n=line.strip()
                if search.lower() in line.lower():
                    # use .lower to avoid case sensitivity
                    address_found = True
                    print(n)
                if address_found: # ask user if they want to delete address
                    change_choice = input('Address found, do you want to change this address? Input Yes or No: ')
                    if change_choice.lower() == 'yes':
                        while not correct_input:
                            address_input = input('Please input your changed address here: ')
                            if not re.match(match_pattern,address_input):
                                print('Please follow correct input example')
                                correct_input = False
                                continue
                            else:
                                data[index] = str(address_input + '\n')
                                print('Changed')
                                with open(self.__file,'w') as f: 
                                    for line in data:
                                        f.write(line) 
                                correct_input = True 
                                # break while loop if input is correct
                else: 
                # if address not found continue to next iteration of for loop
                    continue
                
                break
            if not address_found:
                print('No address found')
                
                
    def advanced_search(self):
        '''function allows user to make a more advanced search'''
        self.__advanced_search_list = []
        address_found = False
        while True:
            with open(self.__file,'r+') as f: 
                data = f.readlines()
                print('Search choices:')
                print('1: Forename')
                print('2: Surname')
                print('3: House number')
                print('4: Street name')
                print('5: Phone number')
                print('6: Birthday')
                try:
                    search_choice = int(input('Please input your search choice: '))
                except ValueError: # exception if input not integer
                    print('Incorrect input detected! Please input a number between 1 and 6!')
                    continue
                if search_choice == 1:
                    forename_search = input('Please search for a first name: ')
                    for line in data:
                        n=line.split() 
                        # to access each individual element in a line
                        if forename_search.lower() in n[0].lower():
                            address_found = True
                            # change address_found to True
                            print(line.strip())
                            self.__advanced_search_list.append(line.strip()) 
                            # put all matches in a list
                        else:
                            continue
                elif search_choice == 2:
                    surname_search = input('Please search for a surname: ')
                    for line in data:
                        n=line.split()
                        if surname_search.lower() in n[1].lower():
                              address_found = True
                              print(line.strip())
                              self.__advanced_search_list.append(line.strip())
                        else:
                            continue
                elif search_choice == 3:
                    house_number_search = input('Please search for a house number: ')
                    for line in data:
                        n=line.split()
                        if house_number_search.lower() in n[2].lower():
                              address_found = True
                              print(line.strip())
                              self.__advanced_search_list.append(line.strip())
                        else:
                            continue
                elif search_choice == 4:
                    street_search = input('Please search for a street: ')
                    for line in data:
                        n=line.split()
                        if street_search.lower() in n[3].lower():
                              address_found = True
                              print(line.strip())
                              self.__advanced_search_list.append(line.strip())
                        else:
                            continue
                elif search_choice == 5:
                    phone_search = input('Please search for a phone number: ')
                    for line in data:
                        n=line.split()
                        if phone_search.lower() in n[4].lower():
                              address_found = True
                              print(line.strip())
                              self.__advanced_search_list.append(line.strip())
                        else:
                            continue
                elif search_choice == 6:
                    birthday_search = input('Please search for a birthday: ')
                    for line in data:
                        n=line.split()
                        if birthday_search.lower() in n[5].lower():
                              address_found = True
                              print(line.strip())
                              self.__advanced_search_list.append(line.strip())
                        else:
                            continue
                else:
                    print('Input not recognised, please choose a number between 1 and 6!')
                    continue
                break
        if not address_found:
            print('No address found')
        return self.__advanced_search_list # return list of matching addresses
    
    
def print_menu(): 
    '''function that prints out an instruction menu for the user'''
    print('\nPlease choose a number between 1 and 7')
    print('1: Basic address search')
    print('2: View all addresses')
    print('3: Delete an address')
    print('4: Change an address')
    print('5: Add an address')
    print('6: Advanced address search')
    print('7: Close the address book')
    
    
A = Address('Addresses.txt') # class instance on address file.


while True:
    A.read_file()
    print_menu()
    try:
        choice = int(input('Please Choose a number: ')) 
        # ask user for integer input to choose action
    except ValueError:
        print('Incorrect input detected! Please input an integer.') 
        # exception if input not integer
        continue
    if choice == 1:
        A.search_address()
    elif choice == 2:
        A.view_all()
    elif choice == 3:
        A.delete_address()
    elif choice == 4:
        A.change_address()
    elif choice == 5:
        A.add_address()
    elif choice == 6:
        A.advanced_search()
    elif choice == 7:
        print('Address book closed')
        break
    else:
        print('Input not recognised, please choose a number between 1 and 7!')
        continue # ask user for input again
        


        
            
