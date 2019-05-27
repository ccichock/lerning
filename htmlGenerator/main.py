

class HtmlTarget:
    def __init__(self):
        self.target = ''
        self.classNames = []
        self.html = ''
        self.parent = None
        self.child = None


    def create_html(self, target, className='', text=''):
        self.target = target
        self.classNames.append(className)
        self.html = '<{} class="{}">\n{}\n</{}>'.format(target, className, text, target)
        return self.html


    def add_child(self, htmlTarget):
        self.child = htmlTarget
        self.create_html(self.target, '', htmlTarget.html)



def generate():
    h1Tag = h1('Bubla Habla')
    h1Tag2 = h1('XAXAXAXA')
    htmlTag = html()
    htmlTag.add_child(h1Tag)

    print(htmlTag.html)
    return htmlTag.html
    # while htmlTag.child:
    #     print(htmlTag.child.html)
    #     htmlTag.child = htmlTag.child.child

def h1(text):
    h1 = HtmlTarget()
    h1.create_html('h1', 'bg-dark', text)
    return h1

def html(text = ''):
    html = HtmlTarget()
    html.create_html('html', '', text)
    return html


def defaultHTML():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title></title>
    </head>
    <body>
    
    </body>
    </html>'''

def main():
    # generate()

    with open("index.html", 'w') as file:
        # file.write(defaultHTML())
        file.write(generate())
        # file.write(h1('Bubla Habla'))


if __name__ == "__main__":
    main();