import time
import random


def print_pause(message):
    print(message)
    time.sleep(2)


def intro():
    print_pause("You have just arrived at the club and ready to party")
    print_pause("You get out of your car and prepare for a night of fun")


def what_to_do(items, ladies_drink, name):
    print_pause("What are you gonna do now? (pick a number) ")
    action = input("1. go to your car\n"
                   "2. go to the club entrance\n"
                   "3. go to the bar\n")

    if action == "1":
        go_car(items, ladies_drink, name)
    elif action == "2":
        go_enter(items, ladies_drink, name)
    elif action == "3":
        go_bar(items, ladies_drink, name)


def go_car(items, ladies_drink, name):
    print_pause("You get back to your car and check /n"
                "if you have everything you need")
    if "money_ID" in items:
        print_pause("You got everything you need, ID, Money, Confidence\n"
                    "and Dance moves, time to rock the house! ")
    else:
        print_pause("ahhh there is still your money and ID, /n"
                    "can't survive the night "
                    "with just your dashing good looks right?")
        print_pause("you grab your stuff and check yourself out\n"
                    "on the side mirror one more time")
        items.append("money_ID")
    what_to_do(items, ladies_drink, name)


def go_enter(items, ladies_drink, name):
    print_pause("You get to the door and the bouncer looks at you")
    if "VIPass" in items:
        print_pause("then he tells you 'have a ballin time Chief'")
    else:
        print_pause("he asks 'got your ID???'")
        if "money_ID" in items:
            print_pause("bouncer checks your ID\n"
                        f"then he says ' oh man sorry, /n"
                        "I didn't know it was you Mr.{name}'")
            print_pause("then goes 'Here's your VIP Pass player'")
            print_pause("then he tells you 'have a ballin time Chief'")
            print_pause("you enter the club and it's lit")
            items.append("VIPass")
        else:
            print_pause("you check for your ID but you find out forgot it")
            print_pause("the bouncer says'you can't go in without an ID'")
    what_to_do(items, ladies_drink, name)


def go_bar(items, ladies_drink, name):
    print_pause("you manage to get to the bar")
    if "money_ID" in items:
        print_pause("you call the bar tender")
        print_pause("the bar tender comes")
        if "VIPass" in items:
            print_pause(f"welcome back Mr.{name} what /n"
                        "are you having tonight? ")
            print_pause("you see a pretty lady beside you and/n"
                        " ask 'what drink can I get you?'")
            print_pause(f"shes says 'i'll have {ladies_drink} ")
            print_pause("you signal to the bartender 'give us two of that'")
            print_pause("time to party with a hot lady! /n"
                        "CONGRATULATIONS BIG BALLER!!!!")

        else:
            print_pause(f"bar tender says ' sorry Mr.{name}/n"
                        "can't serve you without your VIPass")
            what_to_do(items, ladies_drink, name)
    else:
        print_pause("the bouncer sees you and asks for your ID or your pass")
        print_pause("but you do't have it")
        print_pause("bouncer kicks you out of the club")
        what_to_do(items, ladies_drink, name)


def play_again():
    while True:
        answers = input("do you wanna play again? (y/n) ")
        answer = answers.lower()
        if "y" == answer:
            print_pause("ok")
            party()
        elif "n" == answer:
            break
        else:
            print_pause("Sorry I don't understand, can you type y or n?")


def party():
    items = []
    drinks = ["martini", "wine", "tequila", "champagne"]
    ladies_drink = random.choice(drinks)
    name = input("please enter your name: ")
    intro()
    what_to_do(items, ladies_drink, name)
    play_again()


party()
