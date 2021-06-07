# Elnaz Dehkharghani
# Student Number: 11015404
# Excercise_3_Card_Game

import time
from enum import Enum
import random


class spells(Enum):
    GOD = "god"
    RESURRECT = "resurect"
#


class player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.currently_god_spell = False
        self.currently_resurrect_spell = False
        self.has_god_spell = True
        self.has_resurrect_spell = True
        self.points = 0
        self.is_computer = False

    def choose_characteristic(self, chosen_card):
        charac_tmp = " ".join([str(i)
                               for i in chosen_card.characteristics.items()])
        print(f"{self.name} pick {chosen_card} with {charac_tmp}")
        if self.is_computer == True:
            return random.choice(list(chosen_card.characteristics.keys()))

        human_input = input(f"{self.name},choose one characteristic:")
        while human_input not in chosen_card.characteristics.keys():
            print(f"{self.name} you chose the wrong characteristic, try again.")
            human_input = input(f"{self.name},choose one characteristic:")
        return human_input

    def give_card(self, card):
        self.hand.append(card)

    def won(self):
        self.points += 1

    def dice_throw(self):
        return random.randint(1, 6)

    def draw_card(self, index=-1):
        """index -1 means pop with no index"""
        if index == -1:
            return self.hand.pop()
        else:
            return self.hand.pop(index)

    def reset_spell(self):
        self.currently_god_spell = False
        self.currently_resurrect_spell = False

    def ask_play_god(self, opponent):
        #
        if self.has_god_spell == True and self.currently_resurrect_spell == False and opponent.currently_god_spell == False:
            if self.is_computer == True:
                if bool(random.randint(0, 1)) == True:
                    self.use_spell(spells.GOD)
                    print(f"{self.name} is GOD")
                    return random.randint(0, len(opponent.hand)-1)
                return
            if input(f"{self.name},would you like to play god spell? [yes,no]") == "yes":
                self.use_spell(spells.GOD)
                print(f"{self.name} is GOD")
                return int(input(f"{opponent.name} has {len(opponent.hand)} cards , which one would you like to be chosen? [enter numbers]"))

    def use_spell(self, spell: spells):
        if spell == spells.GOD and self.has_god_spell == True:
            self.has_god_spell = False
            self.currently_god_spell = True
        elif spell == spells.RESURRECT and self.has_resurrect_spell == True:
            self.has_resurrect_spell = False
            self.currently_resurrect_spell = True
            return True
        else:
            return False

    def ask_play_resurrect(self, outdated_deck):
        #
        if self.has_resurrect_spell == True and self.currently_god_spell == False and len(outdated_deck.cards) > 0:
            if self.is_computer == True:
                if bool(random.randint(0, 1)) == True:
                    self.use_spell(spells.RESURRECT)
                    self.give_card(outdated_deck.draw_rand())
                    print(f"player {self.name} using resurrect spell")
                    return
                return
            if input(f"{self.name},would you like to play resurrect spell? [yes,no]") == "yes":
                self.use_spell(spells.RESURRECT)
                self.give_card(outdated_deck.draw_rand())
                print(f"player {self.name} using resurrect spell")


class deck:
    def __init__(self, deck_name):
        self.name = deck_name
        self.cards = []

    def add_cards(self, cards):
        self.cards.extend(cards)

    def __repr__(self):
        return self.name

    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def distribute_cards(self, player1: player, player2: player):
        while len(self.cards) > 0:
            player1.give_card(self.cards.pop(
                random.randint(0, len(self.cards)-1)))
            player2.give_card(self.cards.pop(
                random.randint(0, len(self.cards)-1)))


class outdated_deck(deck):
    def __init__(self, deck_name):
        super().__init__(self)

    def add_shuffle(self, card):
        self.cards.append(card)
        self.shuffle()

    def draw_rand(self):
        return self.cards.pop(random.randint(0, len(self.cards)-1))


class character:
    def __init__(self, name, strengh: int, beauty: int, score: int):
        self.name = name
        self.characteristics = {"strengh": strengh,
                                "beauty": beauty, "score": score}


class play_card(character):
    def __init__(self, character_name, strength, beauty, score):
        super().__init__(character_name, strength, beauty, score)

    def __repr__(self):
        return f"{self.name}"

    def compare(self, opponent_chosen_card, ch):
        if self.characteristics[ch] > opponent_chosen_card.characteristics[ch]:
            return True
        else:
            return False


cards = [
    play_card("Edna Mode", 99, 44, 25),
    play_card("Randle McMurphy", 13, 45, 24),
    play_card("Optimus Prime", 98, 32, 90),
    play_card("Norman Bates", 97, 11, 31),
    play_card("The Minions", 96, 99, 33),
    play_card("Maximus", 95, 41, 55),
    play_card("Legolas", 94, 23, 34),
    play_card("Wednesday Addams", 93, 65, 61),
    play_card("Inspector Clouseau", 92, 37, 73),
    play_card("Inigo Montoya", 91, 29, 92),
    play_card("Hal", 90, 66, -1),
    play_card("Groot", 89, 67, -2),
    play_card("Gromit", 88, 68, -3),
    play_card("Ethan Hunt", 87, 69, -4),
    play_card("Red", 86, 70, -5),
    play_card("Walker", 85, 71, -6),
    play_card("Corporal Hicks", 84, 72, -7),
    play_card("Bane", 83, 73, -8),
    play_card("Woody", 82, 74, -9),
    play_card("Withnail", 81, 75, -10),
    play_card("V", 80, 76, -11),
    play_card("Martin Blank", 78, 77, -12),
    play_card("Samwise Gamgee", 77, 78, -13),
    play_card("Private William Hudson", 76, 79, -14),
]


outdated_deck = outdated_deck("outdated")

main_deck = deck("main")
main_deck.add_cards(cards)
main_deck.shuffle()

player_1 = player("Player 1")
computer_plays = input(
    f"{player_1.name},would you like to play with computer? [yes,no]")
if computer_plays == "yes":
    player_2 = player("Player 2")
    player_2.is_computer = True
    print(f"player {player_2.name} is computer!")
else:
    player_2 = player("Player 2")

main_deck.distribute_cards(player_1, player_2)

dice1_result = 0
dice2_result = 0
while dice1_result == dice2_result:
    dice1_result = player_1.dice_throw()
    print(f"dice throw result for {player_1.name} : {dice1_result}")
    dice2_result = player_2.dice_throw()
    print(f"dice throw result for {player_2.name} : {dice2_result}")
    if dice1_result == dice2_result:
        print("throw again...")

if dice1_result > dice2_result:
    print(f"{player_1.name} is starter")
    starter = player_1
    opponent = player_2
else:
    print(f"{player_2.name} is starter")
    starter = player_2
    opponent = player_1


#
#
#
round_count = 0
while len(starter.hand) > 0 and len(opponent.hand) > 0:
    round_count += 1
    print(f"Round : {round_count}")
    starter.ask_play_resurrect(outdated_deck)
    starter_chosen_card = starter.draw_card(-1)
    starter_chosen_characteristic = starter.choose_characteristic(
        starter_chosen_card)
    starter_god_choice = starter.ask_play_god(opponent)
    opponent.ask_play_resurrect(outdated_deck)
    if starter.currently_god_spell == True and opponent.currently_resurrect_spell == True:
        if starter.is_computer == True:
            if bool(random.randint(0, 1)) == True:
                print(f"{starter.name} let you to use resurrected card")
                opponent_chosen_card = opponent.draw_card(-1)
            else:
                print(f"{starter.name} force you to use {starter_god_choice} card")
                opponent_chosen_card = opponent.draw_card(starter_god_choice)
        else:
            if input(f"{starter.name},would you like to let {opponent.name} to use resurected card? [yes,no]") == "yes":
                opponent_chosen_card = opponent.draw_card(-1)
            else:
                opponent_chosen_card = opponent.draw_card(starter_god_choice)
    else:
        opponent_chosen_card = opponent.draw_card(-1)

    print(f"player {opponent.name} chose {opponent_chosen_card}")
    if starter_chosen_card.compare(opponent_chosen_card, starter_chosen_characteristic) == True:
        print(
            f"{starter.name} won this round with {starter_chosen_characteristic} -> {starter_chosen_card.characteristics[starter_chosen_characteristic]} versus {opponent_chosen_card.characteristics[starter_chosen_characteristic]} <- {opponent.name} ")
        starter.won()
    else:
        print(
            f"{opponent.name} won this round with {starter_chosen_characteristic} -> {opponent_chosen_card.characteristics[starter_chosen_characteristic]} versus {starter_chosen_card.characteristics[starter_chosen_characteristic]} <- {starter.name} ")
        opponent.won()
        starter, opponent = opponent, starter

    outdated_deck.add_shuffle(starter_chosen_card)
    outdated_deck.add_shuffle(opponent_chosen_card)

    starter.reset_spell()
    opponent.reset_spell()


if starter.points > opponent.points:
    print(f"{starter.name} is won with {starter.points} points")
else:
    print(f"{opponent.name} is won with {opponent.points} points")

time.sleep(100000)
