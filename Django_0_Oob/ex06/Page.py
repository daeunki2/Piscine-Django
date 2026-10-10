
import elem
import elements


class Page:
    def __init__(self, elem):
        self.root = elem

    def __str__(self):
        if isinstance(self.root, elements.Html):
            return "<!DOCTYPE html>\n" + str(self.root)
        else:
            return str(self.root)

    def write_to_file(self, filename):
        with open(filename, "w") as file:
            file.write(str(self))

    def is_valid(self):
        return self.check_node(self.root)

    def check_node(self, node):
        # Text는 자식이 없으므로 종료
        if type(node) is elem.Text:
            return True

        # 허용되는 클래스인지 검사
        allowed_types = (
            elements.Html,
            elements.Head,
            elements.Body,
            elements.Title,
            elements.Meta,
            elements.Img,
            elements.Table,
            elements.Th,
            elements.Tr,
            elements.Td,
            elements.Ul,
            elements.Ol,
            elements.Li,
            elements.H1,
            elements.H2,
            elements.P,
            elements.Div,
            elements.Span,
            elements.Hr,
            elements.Br
        )

        if type(node) not in allowed_types:
            return False

        # 1. Html: Head 다음 Body
        if isinstance(node, elements.Html):
            if len(node.content) != 2:
                return False

            if not isinstance(node.content[0], elements.Head):
                return False

            if not isinstance(node.content[1], elements.Body):
                return False

        # 2. Head: Title 정확히 하나
        elif isinstance(node, elements.Head):
            title_count = 0

            for child in node.content:
                if isinstance(child, elements.Title):
                    title_count += 1

            if title_count != 1:
                return False

        # 3. Body / Div: 허용된 자식만
        elif isinstance(node, (elements.Body, elements.Div)):
            allowed = (
                elements.H1,
                elements.H2,
                elements.Div,
                elements.Table,
                elements.Ul,
                elements.Ol,
                elements.Span,
                elem.Text
            )

            for child in node.content:
                if not isinstance(child, allowed):
                    return False

        # 4. Title / H1 / H2 / Li / Th / Td
        # 정확히 하나의 Text
        elif isinstance(node, (
            elements.Title,
            elements.H1,
            elements.H2,
            elements.Li,
            elements.Th,
            elements.Td
        )):
            if len(node.content) != 1:
                return False

            if not isinstance(node.content[0], elem.Text):
                return False

        # 5. P: Text만 허용
        elif isinstance(node, elements.P):
            for child in node.content:
                if not isinstance(child, elem.Text):
                    return False

        # 6. Span: Text 또는 P만 허용
        elif isinstance(node, elements.Span):
            for child in node.content:
                if not isinstance(child, (elem.Text, elements.P)):
                    return False

        # 7. Ul / Ol: 최소 하나의 Li
        elif isinstance(node, (elements.Ul, elements.Ol)):
            if len(node.content) < 1:
                return False

            for child in node.content:
                if not isinstance(child, elements.Li):
                    return False

        # 8. Tr: Th 또는 Td만, 혼합 불가
        elif isinstance(node, elements.Tr):
            if len(node.content) < 1:
                return False

            first_type = type(node.content[0])

            if first_type not in (elements.Th, elements.Td):
                return False

            for child in node.content:
                if type(child) is not first_type:
                    return False

        # 9. Table: 최소 하나의 Tr
        elif isinstance(node, elements.Table):
            if len(node.content) < 1:
                return False

            for child in node.content:
                if not isinstance(child, elements.Tr):
                    return False

        # 모든 자식 노드를 재귀적으로 검사
        for child in node.content:
            if not self.check_node(child):
                return False

        return True



if __name__ == "__main__":

    def run_test(name, root, expected):
        result = Page(root).is_valid()
        status = "PASS" if result == expected else "FAIL"
        print(f"[{status}] {name}: {result} (expected: {expected})")
        return result == expected

    tests = [
        # 1. Html
        ("Valid Html",
         elements.Html([
             elements.Head(elements.Title(elem.Text("Hello"))),
             elements.Body(elements.H1(elem.Text("World")))
         ]), True),

        ("Wrong Html order",
         elements.Html([
             elements.Body(),
             elements.Head(elements.Title(elem.Text("Hello")))
         ]), False),

        ("Missing Body",
         elements.Html([
             elements.Head(elements.Title(elem.Text("Hello")))
         ]), False),

        # 2. Head
        ("Valid Head",
         elements.Head([
             elements.Title(elem.Text("Hello")),
             elements.Meta()
         ]), True),

        ("Missing Title",
         elements.Head(elements.Meta()), False),

        ("Two Titles",
         elements.Head([
             elements.Title(elem.Text("A")),
             elements.Title(elem.Text("B"))
         ]), False),

        # 3. Body / Div
        ("Valid Body",
         elements.Body([
             elements.H1(elem.Text("Hello")),
             elements.Div(elem.Text("World"))
         ]), True),

        ("Invalid Body child",
         elements.Body(elements.Title(elem.Text("Wrong"))), False),

        # 4. Text restrictions
        ("Valid H1",
         elements.H1(elem.Text("Hello")), True),

        ("Two Text in H1",
         elements.H1([
             elem.Text("Hello"),
             elem.Text("World")
         ]), False),

        ("Invalid P",
         elements.P(elements.H1(elem.Text("Wrong"))), False),

        ("Valid Span",
         elements.Span([
             elem.Text("Hello"),
             elements.P(elem.Text("World"))
         ]), True),

        # 5. Lists
        ("Valid Ul",
         elements.Ul([
             elements.Li(elem.Text("Apple")),
             elements.Li(elem.Text("Banana"))
         ]), True),

        ("Empty Ul",
         elements.Ul(), False),

        ("Invalid Ol child",
         elements.Ol(elements.H1(elem.Text("Wrong"))), False),

        # 6. Tables
        ("Valid Table",
         elements.Table(
             elements.Tr([
                 elements.Td(elem.Text("A")),
                 elements.Td(elem.Text("B"))
             ])
         ), True),

        ("Mixed Th and Td",
         elements.Tr([
             elements.Th(elem.Text("Name")),
             elements.Td(elem.Text("Alice"))
         ]), False),

        ("Empty Tr",
         elements.Tr(), False),

        ("Empty Table",
         elements.Table(), False),

        # 7. Recursion
        ("Invalid nested Div",
         elements.Div(
             elements.Div(
                 elements.Title(elem.Text("Wrong"))
             )
         ), False),

        ("Valid nested Div",
         elements.Div(
             elements.Div(
                 elements.H1(elem.Text("Hello"))
             )
         ), True),

        # 8. Invalid types
        ("Invalid root type",
         elem.Elem("custom"), False)
    ]

    print("=== Page Validation Tests ===")

    passed = 0

    for name, root, expected in tests:
        if run_test(name, root, expected):
            passed += 1

    print(f"\nResult: {passed}/{len(tests)} tests passed")

    # 9. HTML rendering and file output
    page = Page(
        elements.Html([
            elements.Head(
                elements.Title(elem.Text("My Page"))
            ),
            elements.Body([
                elements.H1(elem.Text("Hello")),
                elements.Ul([
                    elements.Li(elem.Text("Apple")),
                    elements.Li(elem.Text("Banana"))
                ])
            ])
        ])
    )

    print("\n=== HTML Output ===")
    print(page)

    page.write_to_file("sample.html")
    print("HTML written to sample.html")
