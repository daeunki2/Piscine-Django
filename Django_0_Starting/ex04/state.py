import sys


def find_state(user_input):
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

    for c_key, c_value in capital_cities.items():
        if user_input == c_value:
            for s_key, s_value in states.items():
                if c_key == s_value:
                    print(f"{s_key}")
                    return True
    print("Unknown capital city")


if __name__ == '__main__':
    if len(sys.argv) == 2:
        find_state(sys.argv[1])