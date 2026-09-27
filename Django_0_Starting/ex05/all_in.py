import sys


def all_in(user_input):
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

    # If there are two successive commas, print nothing
    if ",," in user_input:
        return

    # Split input by comma
    words = user_input.split(",")

    for word in words:
        # Remove extra spaces, including multiple spaces inside
        word = " ".join(word.split())

        found = False

        # Case 1: input is a state
        for state, state_code in states.items():
            if word.lower() == state.lower():
                city = capital_cities[state_code]
                print(f"{state} is a state of the USA. Its capital is {city}")
                found = True
                break

        if found:
            continue

        # Case 2: input is a capital city
        for state_code, city in capital_cities.items():
            if word.lower() == city.lower():
                for state, code in states.items():
                    if state_code == code:
                        print(f"{city} is the capital of {state}")
                        found = True
                        break

        # Case 3: neither a state nor a capital city
        if not found:
            print(f"{word} is neither a capital city nor a state")


if __name__ == '__main__':
    if len(sys.argv) == 2:
        all_in(sys.argv[1])