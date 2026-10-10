import random
import beverages


class CoffeeMachine:
    def __init__(self):
        self.count = 0

    class EmptyCup(beverages.HotBeverage):
        def __init__(self):
            super().__init__(price=0.90, name="empty cup")

        def description(self):
            return "An empty cup?! Gimme my money back!"

    class BrokenMachineException(Exception):
        def __init__(self):
            super().__init__("This coffee machine has to be repaired.")

    def serve(self, beverage_class):
        if self.count >= 10:
            raise self.BrokenMachineException()

        self.count += 1

        return random.choice([
            beverage_class(),
            self.EmptyCup()
        ])

    def repair(self):
        self.count = 0


def main():
    machine = CoffeeMachine()

    beverages_list = [
        beverages.Coffee,
        beverages.Tea,
        beverages.Chocolate,
        beverages.Cappuccino
    ]

    for round_number in range(2):
        print(f"\n=== Round {round_number + 1} ===")

        try:
            for i in range(12):
                beverage_class = random.choice(beverages_list)

                print(f"\nOrder {i + 1}: {beverage_class.__name__}")

                drink = machine.serve(beverage_class)
                print(drink)

        except CoffeeMachine.BrokenMachineException as error:
            print(f"\nERROR: {error}")

        if round_number == 0:
            print("\nRepairing the machine...")
            machine.repair()


if __name__ == "__main__":
    main()