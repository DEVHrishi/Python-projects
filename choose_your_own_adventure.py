name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. which way would you like to go? ").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around or swim accross ? Type walk to walk around and swim to swim accross: ").lower()

    if answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game!")
    elif answer == "swim":
        print("you swim accross andware eaten by an alligator.")
    else:
        print("Not a valid option.You lose!!")

elif answer == "right":
    answer = input("You come to bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ").lower()

    if answer == "cross":
        answer = input("You cross the bridge and meet a stranger, do you want to talk to him or run away (talk/run)? ").lower()

        if answer == "talk":
            print("You talk to the stranger and he tells you that you are a wizard and he is a wizard too. You win!!")

        elif answer == "run":
            print("You run away and lose!!")

        else:
            print("Not a valid option.You lose!!")
    elif answer == "back":
        print("You go back and lose!!")
    
    else:
        print("Not a valid option.You lose!!")
else : 
    print("Not a valid option. You lose!!")

print("Thanks for playing!", name)