# Name - Sudarshan kakad
# Mobile -9307421907

contacts = [{'Name':'Police', 'Number':'100', 'Email':'police@gmail.com'},
            {'Name':'Ambulance', 'Number':'108', 'Email':'Ambulance@gmail.com'},
            {'Name':'FireSaftey', 'Number':'104', 'Email':'Fire@gmail.com'}]    # list of default contacts

def show_contacts():                                                            # programmer defined function to show contacts
    for ele in contacts:                                                        # selecting elements in contact 
     print(ele)                                                                 # printing the selected contact

def find_contacts():                                                            # programmer defined function to find contacts
    f = input('search name: ')                                                  # taking input of a name to be searched by users
    count = 0
    for i in range(len(contacts)):                                              # applying the condition to check whether the searched contact exists or not
        if contacts[i]['Name'] == f:
            print(contacts[i])
            count = count+1
    if count == 0:
        print("contact doesnt exist")

def add_contacts():                                                             # programmer defined function to add contacts
   print("Enter the contact details to add\n")
   d = {'Name':input('Enter Name: - '), 'Number':int(input('Enter Phone No:- ')), 'Email':input('Enter Email:') } # input from user to add contact details
   contacts.append(d)                                                           # taken input is appended to contacts
   print("\nContact Added Succesfully\n")

def delete_contacts(contacts, name):                                            # programmer defined function to delete contacts
    for i in range(len(contacts)):                                              # checking the name by indexing to delete it
        if contacts[i]['Name'] == name:
            del contacts[i]                                                     # del function is used to delete the contact 
            break
    print("\nContact " + name + " Deleted succesfully\n")

def update_contacts(contacts, name):                                            # programmer defined function to update contacts
    for i in range(len(contacts)):                                              # indexing the contacts
        if contacts[i]['Name'] == name:                                         # checking the contact name is matching with user input or not
             update_key = input('Which key??')                                  # ask for the key to be updated 
             contacts[i][update_key] = input('Enter value ')                    # updating the key using key and value
    print("\nContact Updated Successfully\n")

def directory():                                                                # creating the file to store the contacts
 contacts_string = ''                                                         # converting the contacts into the string to add into txt file
 for i in contacts:
    contacts_string = contacts_string + str(i) + '\n'                         # assigning the contacts_string a new value
    import os
    f = open('C:\\Users\\HP\\Desktop\\Python Projects\\My contacts.txt','w')  # opening file
    f.write(contacts_string)                                                  # writing the file
    f.close                                                                   # closing the file

print("\nSelect the No. of the action you want to perform \n")                  # displaying the features of the contact app
print("1.Show contacts\n2.Find contacts\n3.Add contacts\n4.Delete contacts\n5.Updatecontacts\n") 
n = int(input('Select the No :-'))                                              # taking input for the action to be perform
while exit != 'yes':                                                            # exit condition

    while n<1 or n>5:                                                           # input should exist between 1 to 5 as per the features list
        print("\nInvalid Input\nSelect the No. of the action you want to perform \n")
        print("1.Show contacts\n2.Find contacts\n3.Add contacts\n4.Delete contacts\n5.Updatecontacts\n")
        n = int(input('Select the No :-'))                                      # input will be taken again and again until it exists
    
    if n == 1:                                                                  # feature 1 shows contacts
     show_contacts()
     directory()
     exit = input('Do you want to exit :- ')        # asking user to exit or not
     if exit == 'yes':                              # if exit == yes it will stop otherwise it will ask for selecting the feature again
      break
     else: 
        n = int(input('Select the No :-'))


    elif n == 2:                                                       # feature 2 find contacts 
     find_contacts()
     directory()
     exit = input('Do you want to exit :- ')        # asking user to exit or not
     if exit == 'yes':                              # if exit == yes it will stop otherwise it will ask for selecting the feature again
      break
     else: 
        n = int(input('Select the No :-'))

    elif n == 3:                                                      # feature 3 add contacts and make changes in directory
        add_contacts()
        show_contacts()
        directory()
        exit = input('Do you want to exit :- ')     # asking user to exit or not
        if exit == 'yes':                           # if exit == yes it will stop otherwise it will ask for selecting the feature again
         break
        else: 
          n = int(input('Select the No :-'))

    elif n == 4:                                                      # feature 4 delete contacts, show contacts and make changes in directory
        name = input('Enter the name you want to delete :- ')
        delete_contacts(contacts,name)
        show_contacts()
        directory()
        exit = input('Do you want to exit :- ')    # asking user to exit or not 
        if exit == 'yes':                          # if exit == yes it will stop otherwise it will ask for selecting the feature again
         break
        else: 
          n = int(input('Select the No :-'))

    elif n == 5:                                                     # feature 5 update contacts, show contacts and make changes in directory
        name = input('Enter the name you want to update :- ')
        update_contacts(contacts, name)
        show_contacts()
        directory()
        exit = input('Do you want to exit :- ')    # asking user to exit or not
        if exit == 'yes':                          # if exit == yes it will stop otherwise it will ask for selecting the feature again
         break
        else: 
         n = int(input('Select the No :-'))
