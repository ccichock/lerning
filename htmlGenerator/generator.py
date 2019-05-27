
from HtmlTag import HtmlTarget


def h1(text):
    h1 = HtmlTarget()
    h1.create_html('h1', 'bg-dark', text)
    return h1