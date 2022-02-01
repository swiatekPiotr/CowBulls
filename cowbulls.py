import random


def compare(number, user):
    cowbull = [0, 0]  # cows, then bulls
    for c in range(len(number)):
        if number[c] == user[c]:
            cowbull[0] += 1
        if any(a == number[c] for a in user):  # lub elif user[c] in number:
            cowbull[1] += 1
    cowbull[1] -= cowbull[0]
    return cowbull

def main():
    print("Welcome to game 'cows and bulls'! \ntry divine 4 digit number")
    print("for every digit in the right place you get a cow, and bull in the wrong place.")
    rand_int = str("%04d" % random.randint(0, 9999)) # or "".join(random.sample(string.digits, 4))

    i = 0
    while True:
        guess = input("Give me your best guess! >")
        cowbullcount = compare(rand_int,guess)
        i += 1
        print("You have {} cows, and {} bulls.".format(cowbullcount[0], cowbullcount[1]))
        if cowbullcount[0] == 4:
            print("You win the game after " + str(i) + " shoot")
            break
        else: print("Your guess isn't quite right, try again.")


if __name__ == "__main__":
    main()