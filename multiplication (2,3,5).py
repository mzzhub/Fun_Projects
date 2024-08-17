import itertools

# Creating a list containing all digits.
digits = [0,1,2,3,4,5,6,7,8,9]

# Creating a list named 'permutation'
# Containing all possible permutations of 'digits'
# Hence, contains (10! = 3628800) elements.
permutation = list(itertools.permutations(digits))


# Going through all elements of 'permutation'
for i in permutation:
    # Making two-gigit number from 0th to 1st index.
    a = i[0]*10 + i[1]
    # Making three-digit number from 2nd to 4th index.
    b = i[2]*100 + i[3]*10 + i[4]
    # Making five-digit number from 5th to 9th index.
    c = i[5]*10000 + i[6]*1000 + i[7]*100 + i[8]*10 + i[9]


    # Checking condition and printing the result.
    if a*b==c:
        if c < 10000:
            # If the product is a four-digit, this will add a leading zero to the output.
            print(a,"X",b,"=","0"+str(c))
        else:
            print(a,"X",b,"=",c)





#   Output
#       12 X 483 = 05796
#       18 X 297 = 05346
#       27 X 198 = 05346
#       27 X 594 = 16038
#       28 X 157 = 04396
#       36 X 495 = 17820
#       39 X 186 = 07254
#       39 X 402 = 15678
#       42 X 138 = 05796
#       45 X 396 = 17820
#       46 X 715 = 32890
#       48 X 159 = 07632
#       52 X 367 = 19084
#       54 X 297 = 16038
#       63 X 927 = 58401
#       78 X 345 = 26910