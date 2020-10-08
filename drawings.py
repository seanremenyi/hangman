from termcolor import colored, cprint


def image(count):
    if count <= 0:
        print("""+---+
  |   |
      |
      |
      |
      |
=========""")
    elif count == 1:
        print('''
  +---+
  |   |
  O   |
      |
      |
      |
=========''')
    elif count == 2:
        print('''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''')
    elif count == 3:
        print('''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''')
    elif count == 4:
        print('''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''')
    elif count ==5:
        print('''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''')
    elif count ==6:
        cprint('''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', 'white', 'on_red')
    else:
        return ""
    return ""
