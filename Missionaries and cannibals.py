# Name - Sudarshan Kakad
# Number - 9307421907


missionaries_on_right = 3   # missionaries on right side 
cannibals_on_right = 3   # cannibals on right side 
missionaries_on_left = 0   # missionaries on left side
cannibals_on_left = 0   # cannibals on left side

print("missionaries_on_left = ",missionaries_on_left," ","cannibals_on_left = ",cannibals_on_left," |........⛵| "+" missionaries_on_right = ",missionaries_on_right," cannibals_on_right = ",cannibals_on_right) # intial display

while True:  # main While loop for repeated input of missionaries and cannibals consecutively on right and left side 
    while True:  # sub while loop for right hand side
        missionaries_on_right_input = int(input('Select The missionaries On Right Side :-  '))     # input of missionaries on right
        if missionaries_on_right_input>missionaries_on_right or missionaries_on_right<0:           # conditions for missionaries input
            while(True):   # checking the condition until it is true
                print("\nPlease Select From Availabe No. Of Missionaries\n\n")
                missionaries_on_right_input = int(input('Select The missionaries On Right Side :-  ')) 
                if missionaries_on_right_input<=missionaries_on_right and missionaries_on_right_input>-1:
                    break # breaking the while loop condition if the condition is satisfied
                
        cannibals_on_right_input = int(input('Select The cannibals On Right Side :-  '))     # input of cannibals on right side
        if cannibals_on_right_input>cannibals_on_right or cannibals_on_right<0:              # conditions for cannibals input                                           
            while (True):    # checking the condition until it is true
                print("\nPlease Select From Availabe No. Of Cannibals\n")
                cannibals_on_right_input = int(input('Select The cannibals On Right Side :-  '))
                if cannibals_on_right_input<=cannibals_on_right and cannibals_on_right_input>-1:
                    break   # breaking the while loop condition if the condition is satisfied

        if missionaries_on_right_input>missionaries_on_right or missionaries_on_right<0:      
            while(True):  # checking the condition until it is true
                print("\nPlease Select From Availabe No. Of Missionaries\n\n")
                missionaries_on_right_input = int(input('Select The missionaries On Right Side :-  ')) 
                if missionaries_on_right_input<=missionaries_on_right and missionaries_on_right_input>-1:
                    break   # breaking the while loop condition if the condition is satisfied
    
        if missionaries_on_right==0 and missionaries_on_right_input>0:
            while missionaries_on_right == 0:   # checking the condition until it is true
                print("\nThe Selected No. Of Missionaries are not available\n")
                missionaries_on_right_input = int(input('Select The missionaries On Right Side :-  '))  
                if missionaries_on_right_input == 0:
                    break   # breaking the while loop condition if the condition is satisfied

        if cannibals_on_right_input>cannibals_on_right or cannibals_on_right<0:
            while (True):   # checking the condition until it is true
                print("\nPlease Select From Availabe No. Of Cannibals\n")
                cannibals_on_right_input = int(input('Select The cannibals On Right Side :-  '))
                if cannibals_on_right_input<=cannibals_on_right and cannibals_on_right_input>-1:
                    break   # breaking the while loop condition if the condition is satisfied
    
        if cannibals_on_right==0 and cannibals_on_right_input>0 :
            while (True):   # checking the condition until it is true
                print("\nThe Selected No. Of Cannibals are not available\n")
                cannibals_on_right_input = int(input('Select The cannibals On Right Side :-  '))
                if cannibals_on_right_input == 0:
                    break   # breaking the while loop condition if the condition is satisfied

        if missionaries_on_right_input == 0 and cannibals_on_right_input == 0:
            while(True):   # checking the condition until it is true
                print("\nZero Players Are Selecteds\n")
                missionaries_on_right_input = int(input('Select The missionaries On Right Side :-  '))
                cannibals_on_right_input = int(input('Select The cannibals On Right Side :-  '))
                if (missionaries_on_right_input + cannibals_on_right_input) > 0:
                    break   # breaking the while loop condition if the condition is satisfied

        if missionaries_on_right_input+cannibals_on_right_input>2:
             while (True):   # checking the condition until it is true
                print("\nOnly 2 Character Can Travel At A Time\n")
                missionaries_on_right_input = int(input('Select The missionaries On Right Side :-  '))
                cannibals_on_right_input = int(input('Select The cannibals On Right Side :-  '))
                if missionaries_on_right_input + cannibals_on_right_input <= 2:
                   break   # breaking the while loop condition if the condition is satisfied
        
        missionaries_on_right = missionaries_on_right - missionaries_on_right_input # some operations to be done on right side inputs
        cannibals_on_right = cannibals_on_right - cannibals_on_right_input
        missionaries_on_left = missionaries_on_left + missionaries_on_right_input
        cannibals_on_left = cannibals_on_left + cannibals_on_right_input
        print()
        print("missionaries_on_left = ",missionaries_on_left," ","cannibals_on_left = ",cannibals_on_left," |⛵........| "+" missionaries_on_right = ",missionaries_on_right," cannibals_on_right = ",cannibals_on_right)
        if (missionaries_on_right_input+cannibals_on_right_input)<3:
         break # breaking the sub-while loop condition if the conditions are satisfied
    if cannibals_on_right > missionaries_on_right and missionaries_on_right>0:  # loosing condition
        print("You Lost The Game")
        break  # breaking the main-while loop condition if the conditions are satisfied
    if cannibals_on_left>missionaries_on_left and missionaries_on_left>0:      # loosing condition
        print("You Lost The Game")
        break   # breaking the main-while loop condition if the conditions are satisfied
    if missionaries_on_right == 0 and cannibals_on_right == 0 and missionaries_on_left==3 and cannibals_on_left==3:  # winning condition
        print("You Won")
        break   # breaking the main-while loop condition if the conditions are satisfied
    

    while True:   # sub while loop for left hand side
        missionaries_on_left_input = int(input('Select The missionaries On Left Side :-  '))    # input of missionaries on left
        if missionaries_on_left_input>missionaries_on_left or missionaries_on_left<0:           # conditions for missionaries input
            while(True):   # checking the condition until it is true
                print("\nPlease Select From Availabe No. Of Missionaries\n")
                missionaries_on_left_input = int(input('Select The missionaries On Left Side :-  ')) 
                if missionaries_on_left_input<=missionaries_on_left and missionaries_on_left_input>-1:
                    break   # breaking the while loop condition if the condition is satisfied
    
        if missionaries_on_left==0 and missionaries_on_left_input>0:                      
            while(True):   # checking the condition until it is true
                print("\nThe Selected No. Of Missionaries are not available\n")
                missionaries_on_left_input = int(input('Select The missionaries On Left Side :-  '))  
                if missionaries_on_left_input == 0:
                    break   # breaking the while loop condition if the condition is satisfied
           
        cannibals_on_left_input = int(input('Select The cannibals On Left Side :-  '))

        if cannibals_on_left_input>cannibals_on_left or cannibals_on_left<0:
            while (True):  # checking the condition until it is true
                print("\nPlease Select From Availabe No. Of Cannibals\n")
                cannibals_on_left_input = int(input('Select The cannibals On Left Side :-  '))
                if cannibals_on_left_input<=cannibals_on_left and cannibals_on_left_input>-1:
                    break   # breaking the while loop condition if the condition is satisfied
    
        if cannibals_on_left==0 and cannibals_on_left_input>0 :
            while (True):  # checking the condition until it is true
                print("\nThe Selected No. Of Cannibals are not available\n")
                cannibals_on_left_input = int(input('Select The cannibals On Left Side :-  '))
                if cannibals_on_left_input == 0:
                    break   # breaking the while loop condition if the condition is satisfied
        if missionaries_on_left_input == 0 and cannibals_on_left_input == 0:
            while(True):  # checking the condition until it is true
                print("\nZero Players Are Selecteds\n")
                missionaries_on_left_input = int(input('Select The missionaries On Left Side :-  '))
                cannibals_on_left_input = int(input('Select The cannibals On Left Side :-  '))
                if (missionaries_on_left_input + cannibals_on_left_input) > 0:
                    break   # breaking the while loop condition if the condition is satisfied

        if missionaries_on_left_input+cannibals_on_left_input>2:
            while (True):  # checking the condition until it is true
                print("\nOnly 2 Character Can Travel At A Time\n")
                missionaries_on_left_input = int(input('Select The missionaries On Left Side :-  '))
                cannibals_on_left_input = int(input('Select The cannibals On Left Side :-  '))
                if missionaries_on_left_input + cannibals_on_left_input <= 2:
                    break    # breaking the while loop condition if the condition is satisfied
        
        missionaries_on_left=missionaries_on_left-missionaries_on_left_input # some operations to be done on left side input
        cannibals_on_left=cannibals_on_left-cannibals_on_left_input
        missionaries_on_right=missionaries_on_right+missionaries_on_left_input
        cannibals_on_right=cannibals_on_right+cannibals_on_left_input
        print()
        print("missionaries_on_left = ",missionaries_on_left," ","cannibals_on_left = ",cannibals_on_left," |........⛵| "+" missionaries_on_right = ",missionaries_on_right," cannibals_on_right = ",cannibals_on_right)
        print()
        if (missionaries_on_left_input + cannibals_on_left_input)<3 :
         break   # breaking the sub-while loop condition if the conditions are satisfied
    if cannibals_on_right > missionaries_on_right and missionaries_on_right>0:  # loosing condition
        print("You Lost The Game")
        break  # breaking the main-while loop condition if the conditions are satisfied
    if cannibals_on_left>missionaries_on_left and missionaries_on_left>0:      # loosing condition
        print("You Lost The Game")
        break   # breaking the main-while loop condition if the conditions are satisfied
    if missionaries_on_right == 0 and cannibals_on_right == 0 and missionaries_on_left==3 and cannibals_on_left==3:  # winning condition
        print("You Won")
        break   # breaking the main-while loop condition if the conditions are satisfied
