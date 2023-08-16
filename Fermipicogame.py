# Name - Sudarshan kakad
# Div - B 
# Mobile - 9307421907

print()
print("Welcome to Number Guessing Game")                                    # introduction
print("Lets start")  
while True:                                                                 # while loop for clear input from user until it is satisfied 
    n = int(input('Select How Many Digit No. You Want To guess :-  '))
    while True:                                                             # if the input is greater than 6 it will ask for the input again until input <7
       print('Input Valid Only For Upto 6 Digits Only\n')
       n = int(input('Select How Many Digit No. You Want To guess :-  '))
       if n<=6:
          break
    Zero = input('Do You Want To Include Zero :- ')                         #asking the user whether to include the zero or not
    print("A random " + str(n) + " digit No. is generated and you have to guess it in 10 chances")     # instruction
    if n<=6:
        break
print()

if Zero =='yes':                                     # if zero == yes then the further random no. will be generated including zero
 import random
 a = random.sample('1234567890', n) 
 if len(a) == 1:                                        # generating a random 1 digit number
    a = (a[0])                                          # integrating the generated number together
 if len(a) == 2:                                        # generating a random 2 digit number
    a = (a[0] + a[1])                                   # integrating the generated number together
 if len(a) == 3:                                        # generating a random 3 digit number
    a = (a[0] + a[1] + a[2])                            # integrating the generated number together
 if len(a) == 4:                                        # generating a random 4 digit number
    a = (a[0] + a[1] + a[2] + a[3])                     # integrating the generated number together
 if len(a) == 5:                                        # generating a random 5 digit number
    a = (a[0] + a[1] + a[2] + a[3] + a[4])              # integrating the generated number together
 if len(a) == 6:                                        # generating a random 6 digit number
    a = (a[0] + a[1] + a[2] + a[3] + a[4] + a[5])       # integrating the generated number together
 print(a)                                               # printing the generated number 
 print()            

else:                                                   # if zero != yes then the further random no. will be generated excluding zero
 import random
 a = random.sample('123456789', n)
 if len(a) == 1:                                        # generating a random 1 digit number
    a = (a[0])                                          # integrating the generated number together
 if len(a) == 2:                                        # generating a random 2 digit number
    a = (a[0] + a[1])                                   # integrating the generated number together
 if len(a) == 3:                                        # generating a random 3 digit number
    a = (a[0] + a[1] + a[2])                            # integrating the generated number together
 if len(a) == 4:                                        # generating a random 4 digit number
    a = (a[0] + a[1] + a[2] + a[3])                     # integrating the generated number together
 if len(a) == 5:                                        # generating a random 5 digit number
    a = (a[0] + a[1] + a[2] + a[3] + a[4])              # integrating the generated number together
 if len(a) == 6:                                        # generating a random 6 digit number
    a = (a[0] + a[1] + a[2] + a[3] + a[4] + a[5])       # integrating the generated number together
 print(a)                                               # printing the generated no
print()

for i in range(1,11):                                                     # selecting a range for 10 attempts
    c = input('Chance ' + str(i) + ' :  Enter Four Digit no:-')           # taking input from user
    while len(set(a)) != len(set(c)):
     if len(a) != len(c):                                                 # checking the length of generated No. And user input No.
        while len(a) != len(c):
            print('Enter ' + str(n) + ' Digit No plz')
            c = input('Chance ' + str(i) + ' :  Enter Four Digit no:-')
     if len(a) != len(set(c)):                                            # checking the repeated digits using set(collects unique elements excludes repeated)
        while len(a) != len(set(c)):
            print("Repeated digits")
            c = input('Chance ' + str(i) + ' :  Enter Four Digit no:-')   # asking again for input if digits are repeated
    output = []
    for j in range(len(set(a))):                                          # selecting index 
      for k in range(len(set(c))):                                        # selecting index 
        if a[j] == c[k]:                                                  # checking element match
            if j == k:
                output.append('fermi ')                                   # if index & No. matches then appending fermi
            else :                                                        # if index not matching but no. is included then appending pico
                output.append('pico ')
    if (len(output)) == 0:                                                # if no element matches then output should be bagels
        output = "bagels"
    main_output = ''                                                      # creating a main output
    for item in output:
        main_output = main_output+ '' + item
    print(main_output)
    if int(a)-int(c) == 0:                                               # winning condition
        print('You won')
        break                                                            # breaking the loop if user wins before than 10th attempt
if int(a)!= int(c):                                                      # after 9th attempt if user not detect the NO. then he/she loose.
 print("You lost It")
