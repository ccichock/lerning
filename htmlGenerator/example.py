
import sys
sys.path.append('./src')

from templates.Default_Html import Default_Html
from templates.Search_Navbar import Search_Navbar_Html
from templates.Registration_Form import Registration_Form


class Simple_Html(Default_Html):

    def __init__(self, page_title):
        super().__init__(page_title)

        self.body().add_class('bg-secondary')
        self.body().add_child(Search_Navbar_Html())
        self.body().div().add_class('container p-1 bg-light')
        self.body().div().a('youtube' ,'https://www.youtube.com', id="yt").add_class('btn btn-danger')
        self.body().div().a('facebook' ,'https://www.facebook.com', id="fb").add_class('btn btn-primary')
        self.body().div().div().p('The following is a basic list of the most common CSS properties with the ...').add_class('p-2 text-justify')
        self.body().div().h2("Register Form").add_class("text-center")
        self.body().div().add_child(Registration_Form())


def main():

    html = Simple_Html('Page Title')

    with open('index.html', 'w') as file:
        file.write(html.format_html())


if __name__ == '__main__':
    main();