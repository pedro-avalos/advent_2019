# Directory of the data file
FILE_DIR = 'day_4/data/range.txt'

# Minimum and Maximum
GIVEN_RANGE = list(map(int, open(FILE_DIR).readline().split('-')))

class PasswordCracker():
    def __init__(self):
        # Min and Max constraints
        self.min = GIVEN_RANGE[0]
        self.max = GIVEN_RANGE[1]
        # Size constraint of password
        self.size = 6
        # Whether or not the 'twin' requirement is met
        self.twin = False
        # Whether or not the ascending requirement is met
        self.ascending = False
        # List of possible passwords (none when starting) - part 1
        self.passwords = []
        # List of real passwords (none when starting) - part 2
        self.real_passwords = []

    # Part 1
    def find_passwords(self):
        for guess in range(self.min, self.max):
            # Reset requirements
            self.twin = False
            self.ascending = False

            # List of digits of the current guess
            guess_digits = [int(digit) for digit in str(guess)]
            
            # Check if there is at least one pair of twins
            for i in range(len(guess_digits) - 1):
                if (guess_digits[i] == guess_digits[i + 1]):
                    self.twin = True
            # Check for the ascending requirement
            if sorted(guess_digits) == guess_digits:
                self.ascending = True
            # Save the guess in the paswords
            if self.twin and self.ascending:
                self.passwords.append(guess)

    # Part 2
    def find_real_passwords(self):
        for password in self.passwords:
            # Boolean whether to save the password or not
            is_real = False

            # Dictionary of all the twins iwht their position (of the first in the pair)
            twins_dict = {
                'pos': [],
                'twin': [],
            }

            # List of digits of the current password
            password_digits = [int(digit) for digit in str(password)]

            # Find all the pairs of twins
            for i in range(len(password_digits) - 1):
                if (password_digits[i] == password_digits[i + 1]):
                    twins_dict['pos'].append(i)
                    twins_dict['twin'].append(password_digits[i])

            # If there is only one twin, then it is real
            if len(twins_dict['twin']) == 1:
                is_real = True
            # Else cycle through the twins
            else:
                for i in range(len(twins_dict['pos'])):
                    # If the first twin pair is unique, then it is a real password
                    if twins_dict['twin'].count(twins_dict['twin'][i]) == 1:
                        is_real = True
                    # If the first pair is repeated, then check their positions
                    else:
                        # Iterate through the twins
                        for index in range(len(twins_dict['pos']) - 1):
                            # If there is are two twins of the same value 'next' to each other
                            if twins_dict['twin'][index] == twins_dict['twin'][index + 1]:
                                # If the position of them is not adjacent
                                if abs(twins_dict['pos'][index] - twins_dict['pos'][index + 1]) != 1:
                                    # You have a real password
                                    is_real = True
            
            # Save the password if it is real
            if is_real:
                self.real_passwords.append(password)

# Instance of the password cracker class
password_cracker = PasswordCracker()
# Find all the possible passwords
password_cracker.find_passwords()
# Get the length of the list of possible passwords
print(f"Possible Passwords for Part 1: {len(password_cracker.passwords)}")
password_cracker.find_real_passwords()
# Get the lengths of the list of real passwords
print(f"Possible Real Passwords for Part 2: {len(password_cracker.real_passwords)}")