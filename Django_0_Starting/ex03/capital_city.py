import sys


def find_capital(user_input):
    states = {
        "Oregon": "OR",
        "Alabama": "AL",
        "New Jersey": "NJ",
        "Colorado": "CO"
    }

    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }

    state_code = states.get(user_input)

    if state_code is None:
        print("Unknown state")
    else:
        print(capital_cities[state_code])


if __name__ == '__main__':
    if len(sys.argv) == 2:
        find_capital(sys.argv[1])