# my project!!

import requests 

def main():
    print('Welcome to AllerHins')
    while True:
        choice = displayMenu()
        if choice == 1:
            printAllergens()
        elif choice == 2:
            new = input('Enter your new allergen: ')
            newAllergen(new)
        elif choice == 3:
            allergenDect()
        elif choice <= 0:
            print('Exiting program...')
            break   
        else:
            print('\nPlease enter a number in range.')

def displayMenu():
    print('1. See your allegerns')
    print('2. Enter a new allegern')
    print('3. Check for allergens')
    choice = input('What operation would you like to complete(0< to exit): ')
    return int(choice)

def printAllergens():
    pass

def newAllergen(allergen):
    pass

def allergenDect():
    pass
 

#function call
main()