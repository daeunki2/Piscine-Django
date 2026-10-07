class Intern:
    def __init__(self, name="My name? I’m nobody, an intern, I have no name."):
        self.name = name

    def __str__(self):
        return self.name

    def make_coffee(self):
        return self.Coffee()

    def work(self):
        raise Exception("I’m just an intern, I can’t do that...")

    class Coffee:
        def __str__(self):
            return "This is the worst coffee you ever tasted."


def main():
    nobody = Intern()
    mark = Intern("Mark")

    print(nobody)
    print(mark)

    coffee = mark.make_coffee()
    print(coffee)

    try:
        nobody.work()
    except Exception as error:
        print(error)


if __name__ == "__main__":
    main()