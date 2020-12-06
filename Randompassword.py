# Random Password Generator
# Mini one
import random
import string


def randomPswd(pswdlen=10):
    letter = string.ascii_lowercase
    return ''.join(random.choice(letter) for i in range(pswdlen))


print("Random password : \n", randomPswd())
