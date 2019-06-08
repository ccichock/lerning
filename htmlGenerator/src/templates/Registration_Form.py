from Html_Tags import title, h1, body, script, head
from Html_Tag import Html_Tag


class Registration_Form(Html_Tag):

    def __init__(self):
        super().__init__('form')

        self.add_class('p-2')

        self.div(id='name').label('Name:')
        self.div(id='name').input().placeholder('Type your name')
        self.div(id='name').input().add_class('form-control')
        self.div(id='name').add_class('form-group')

        self.div(id='surname').label('Surname:')
        self.div(id='surname').input().placeholder('Type your surname')
        self.div(id='surname').input().add_class('form-control')
        self.div(id='surname').add_class('form-group')

        self.div(id='email').label('Email:')
        self.div(id='email').input().placeholder('Type your email')
        self.div(id='email').input().add_class('form-control')
        self.div(id='email').add_class('form-group')

        self.div(id='pasword').label('Password:')
        self.div(id='pasword').input(id='pasword').placeholder('Type your pasword')
        self.div(id='pasword').input(id='pasword').add_class('form-control mb-1')
        self.div(id='pasword').input(id='pasword_repet').placeholder('Repeat pasword')
        self.div(id='pasword').input(id='pasword_repet').add_class('form-control mt-1')
        self.div(id='pasword').add_class('form-group')

        self.button('Register').add_class('btn btn-dark')