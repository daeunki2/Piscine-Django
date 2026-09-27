def read_make_html():
    elements = {}

    # Read and parse periodic_table.txt
    with open("periodic_table.txt", "r") as file:
        lines = file.read().splitlines()

    for line in lines:
        name, data = line.split(" = ")

        elements[name] = {}

        infos = data.split(", ")

        for info in infos:
            key, value = info.split(":", 1)
            elements[name][key] = value.strip()

    # Generate periodic_table.html
    with open("periodic_table.html", "w") as file:
        file.write("<!DOCTYPE html>\n")
        file.write('<html lang="en">\n')

        file.write("<head>\n")
        file.write('    <meta charset="UTF-8">\n')
        file.write("    <title>Periodic Table</title>\n")
        file.write("</head>\n")

        file.write("<body>\n")

        file.write("<h1>Periodic Table</h1>\n")
        file.write("<h2>42 Paris</h2>\n")
        file.write("<h3>daeunki2</h3>\n")

        file.write("<table>\n")

        current_position = 0
        first_element = True

        for name, data in elements.items():
            position = int(data["position"])

            # Start a new row when the position goes back
            if first_element:
                file.write("<tr>\n")
                first_element = False

            elif position < current_position:
                file.write("</tr>\n")
                file.write("<tr>\n")
                current_position = 0

            # Preserve empty cells
            while current_position < position:
                file.write("<td></td>\n")
                current_position += 1

            # Write one element in one table cell
            file.write(
                '<td style="border: 1px solid black; padding:10px">\n'
            )

            file.write(f"<h4>{name}</h4>\n")

            file.write("<ul>\n")
            file.write(f'<li>No {data["number"]}</li>\n')
            file.write(f'<li>{data["small"]}</li>\n')
            file.write(f'<li>{data["molar"]}</li>\n')
            file.write(f'<li>{data["electron"]} electron</li>\n')
            file.write("</ul>\n")

            file.write("</td>\n")

            current_position = position + 1

        file.write("</tr>\n")
        file.write("</table>\n")

        file.write("</body>\n")
        file.write("</html>\n")


if __name__ == '__main__':
    read_make_html()