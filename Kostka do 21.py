import random
import os

def roll_dice():
    return random.randint(1, 20)

def print_score(player_name, score):
    print(f"{player_name}, twoje aktualne punkty: {score}")

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def game():
    player_name = input("Podaj swoje imię: ")
    score = 0

    while score != 21:
        clear_terminal()
        print_score(player_name, score)

        print("Wybierz jedną z opcji:")
        print("1. Rzucić kostką")
        print("2. Odjąć 5 od punktów")
        print("3. Odjąć 10 od punktów")
        print("4. Podzielić punkty na pół")
        print("Aby WYGRAĆ musisz posiadać dokładnie 21 punktów.")

        choice = input("Wybierz opcję (1-4): ")

        if choice == "1":
            roll_result = roll_dice()
            print(f"Wynik rzutu: {roll_result}")
            score += roll_result
        elif choice == "2":
            score -= 5
        elif choice == "3":
            score -= 10
        elif choice == "4":
            score //= 2
        else:
            print("Nieprawidłowy wybór, spróbuj ponownie.")

    clear_terminal()
    print_score(player_name, score)
    print("Gratulacje, wygrałeś!")

game()
