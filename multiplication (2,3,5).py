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

    # Removing occurences of, zeroes comming as the left most digit in a,b,c
    if i[0] == 0 or i[2] == 0 or i[5] == 0:
        continue

    # Checking condition and printing the result.
    if a*b==c:
        print(a,"X",b,"=",c)