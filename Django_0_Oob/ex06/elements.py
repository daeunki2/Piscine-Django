
from elem import Elem, Text


# Represents the root element of an HTML document.
class Html(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__('html', attr or {}, content, 'double')


# Contains metadata and information about the HTML document.
class Head(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__('head', attr or {}, content, 'double')


# Contains the visible content of an HTML document.
class Body(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__('body', attr or {}, content, 'double')


# Defines the document title displayed in the browser tab.
class Title(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__('title', attr or {}, content, 'double')


# Defines a table for displaying data in rows and columns.
class Table(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__('table', attr or {}, content, 'double')


# Defines a header cell in a table.
class Th(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__('th', attr or {}, content, 'double')


# Defines a row in a table.
class Tr(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__('tr', attr or {}, content, 'double')


# Defines a standard data cell in a table.
class Td(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__('td', attr or {}, content, 'double')


# Defines an unordered (bulleted) list.
class Ul(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__('ul', attr or {}, content, 'double')


# Defines an ordered (numbered) list.
class Ol(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__('ol', attr or {}, content, 'double')


# Defines an item in an ordered or unordered list.
class Li(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__('li', attr or {}, content, 'double')


# Defines a top-level heading.
class H1(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__('h1', attr or {}, content, 'double')


# Defines a second-level heading.
class H2(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__('h2', attr or {}, content, 'double')


# Defines a paragraph of text.
class P(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__('p', attr or {}, content, 'double')


# Defines a block-level container for grouping HTML elements.
class Div(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__('div', attr or {}, content, 'double')


# Defines an inline container for grouping text or elements.
class Span(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__('span', attr or {}, content, 'double')


# Defines metadata such as character encoding or viewport settings.
class Meta(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__('meta', attr or {}, content, 'simple')


# Embeds an image into the HTML document.
class Img(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__('img', attr or {}, content, 'simple')


# Defines a thematic break between sections of content.
class Hr(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__('hr', attr or {}, content, 'simple')


# Inserts a line break within text.
class Br(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__('br', attr or {}, content, 'simple')


if __name__ == '__main__':
    page = Html([
        Head(Title(Text('"Hello ground!"'))),
        Body([
            H1(Text('"Oh no, not again!"')),
            Img(attr={'src': 'http://i.imgur.com/pfp3T.jpg'})
        ])
    ])

    print(page)
    print("-------------------------------------")
    print(Table(Tr(Td(Text("Hello")))))
    print(Ul([Li(Text("Apple")), Li(Text("Banana"))]))
    print(Span(Text("Hello")))
    print(Br())
