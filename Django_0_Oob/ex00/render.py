import sys
import os
import settings


def read_store(filename):
    if not filename.endswith(".template"):
        print("Not good input file.")
        return None

    try:
        with open(filename, "r") as file:
            content = file.read()
    except FileNotFoundError:
        print("File does not exist.")
        return None

    return content


def main():
    if len(sys.argv) != 2:
        print("Wrong number of arguments.")
        return

    filename = sys.argv[1]

    template = read_store(filename)

    if template is None:
        return

    settings_dict = vars(settings)

    for key, value in settings_dict.items():
        template = template.replace(
            "{" + key + "}",
            str(value)
        )

    name, extension = os.path.splitext(filename)
    output_filename = name + ".html"

    with open(output_filename, "w") as file:
        file.write(template)


if __name__ == "__main__":
    main()