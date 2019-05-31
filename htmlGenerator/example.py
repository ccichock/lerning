
import sys
sys.path.append('./src')

from templates.default_html import simple_html

def main():

    html = simple_html("Page Title")

    with open("index.html", 'w') as file:
        file.write(html.html())


if __name__ == "__main__":
    main();