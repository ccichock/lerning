
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

    with open("index.html", 'w') as file:
        file.write(generate())


if __name__ == "__main__":
    main();