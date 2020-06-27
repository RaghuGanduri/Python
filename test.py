from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from com.myapp.loginscr import Login


class MyApp(App):

    message = ""

    def build(self):
        root = ScreenManager()
        root.add_widget(Login(name="login"))
        return root

if __name__ == '__main__':
    MyApp().run()
