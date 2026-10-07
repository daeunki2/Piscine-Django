class HotBeverage:
    def __init__(self, price=0.30, name="hot beverage"):
        self.price = price
        self.name = name

    def description(self):
        return "Just some hot water in a cup."

    def __str__(self):
        return (
            f"name : {self.name}\n"
            f"price : {self.price:.2f}\n"
            f"description : {self.description()}"
        )

class Coffee(HotBeverage):
    def __init__(self):
        super().__init__(price=0.40, name="coffee")
    
    def description(self):
        return "A coffee, to stay awake."

class Tea(HotBeverage):
    def __init__(self):
        super().__init__(name="tea")
    
class Chocolate(HotBeverage):
    def __init__(self):
        super().__init__(price=0.50, name="chocolate")
    
    def description(self):
        return "Chocolate, sweet chocolate..."
    
class Cappuccino(HotBeverage):
    def __init__(self):
        super().__init__(price=0.45, name="cappuccino")
    
    def description(self):
        return "Un po’ di Italia nella sua tazza!"


def main():
    hot_beverage = HotBeverage()
    coffee = Coffee()
    tea = Tea()
    chocolate = Chocolate()
    cappuccino = Cappuccino()

    print(hot_beverage, coffee, tea, chocolate, cappuccino, sep="\n\n")



if __name__ == "__main__":
    main()