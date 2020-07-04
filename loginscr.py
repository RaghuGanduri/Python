from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import requests
from kivy.app import App


class Login(Screen):
    def __init__(self, **kwargs):
        super(Login, self).__init__(**kwargs)
        self.name = "login"
        self.main = GridLayout(rows=3, row_force_default=True, row_default_height=100, spacing=10, padding=10)
        self.errormesg = GridLayout(rows=1, row_force_default=True, row_default_height=40, spacing=10, padding=10)
        self.inside = GridLayout(cols=2, row_force_default=True, row_default_height=40,spacing=10)
        self.mesg = Label(text="")
        l1 = Label(text='Username', id='lbl_username', size_hint_x=None, width=100)
        l2 = Label(text='Password', id='lbl_password', size_hint_x=None, width=100)
        self.username = TextInput(id='txt_username', multiline=False)
        self.password = TextInput(id='txt_password', password=True, multiline=False)
        self.errormesg.add_widget(self.mesg)
        self.inside.add_widget(l1)
        self.inside.add_widget(self.username)
        self.inside.add_widget(l2)
        self.inside.add_widget(self.password)
        self.main.add_widget(self.errormesg)
        self.main.add_widget(self.inside)
        self.signIn = BoxLayout()

        signuplb = Label(text='[ref=Signup][b][color=0000ff]Signup[/color][/b][/ref]', markup=True)
        signuplb.bind(on_ref_press=self.print_it)
        self.signIn.add_widget(signuplb)
        btn = Button(
                text="Login",
                size_hint=(.5, .25),
                pos_hint ={'x':.2, 'y':.2}
                )
        btn.bind(on_press=self.btn_pressed)
        self.signIn.add_widget(btn)
        self.main.add_widget(self.signIn)
        self.add_widget(self.main)

    def print_it(instance, event, value):
        print(value)
        
    def authresult(req, result):
        print("in auth result")
        

    def btn_pressed(self, event):
        self.mesg.text = ""
        print("user name ", self.username.text)
        