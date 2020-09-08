import random

def main():

    days = 365
    not_sharing = 1
    i = random.randint(1,365)
    probability = i / days
    print ("{0} - {1:.16f}".format(i+1, probability))

if __name__== "__main__":
    main()