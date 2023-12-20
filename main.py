from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.card import MDCard
from kivymd.uix.anchorlayout import MDAnchorLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.textfield import MDTextField
import json


class Login(Screen):
    def __init__(self, **kwargs):
        super(Login, self).__init__(**kwargs)
        self.anchor_layout = MDAnchorLayout()
        self.main_card = MDCard(size_hint=(None, None), size=('500dp', '500dp'), padding='10dp', spacing='10dp',
                                orientation='vertical')
        self.anchor_layout.add_widget(self.main_card)
        self.username = MDTextField(icon_left="account",
                                    hint_text='Username',
                                    font_size='18sp',
                                    size_hint_y=None,
                                    height='60dp')
        self.main_card.add_widget(self.username)
        self.email = MDTextField(icon_left="email",
                                 hint_text='Email',
                                 font_size='18sp',
                                 size_hint_y=None,
                                 height='60dp')
        self.main_card.add_widget(self.email)
        self.password = MDTextField(icon_left="lock",
                                    hint_text='Password',
                                    password=True,
                                    font_size='18sp',
                                    size_hint_y=None,
                                    height='60dp')
        self.main_card.add_widget(self.password)
        self.phone_number = MDTextField(icon_left= 'phone',
                                        hint_text="phone number",
                                        font_size='18sp',
                                        size_hint_y=None,
                                        height='60dp')
        self.main_card.add_widget(self.phone_number)

        small_grid = MDGridLayout(cols=2, spacing=20, padding=20, size_hint=(1, 1))
        login_button = MDRectangleFlatButton(text='Login', height='60dp', on_press=self.on_login_button_press)
        sign_up_button = MDRectangleFlatButton(text='Sign Up', height='60dp', on_press=self.on_signup_button_press)
        small_grid.add_widget(login_button)
        small_grid.add_widget(sign_up_button)
        self.main_card.add_widget(small_grid)
        self.add_widget(self.anchor_layout)

    def save_contact(self, username, phone_number, email, password):
        contact_data = {
            "username": username,
            "phone_number": phone_number,
            "email": email,
            "password": password
        }

        try:
            with open("contacts.json", "r") as file:
                contacts = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            # If the file doesn't exist or is not valid JSON, start with an empty list
            contacts = []

        contacts.append(contact_data)

        with open("contacts.json", "w") as file:
            json.dump(contacts, file, indent=2)

    def on_signup_button_press(self, instance):
        email = self.email.text
        phone_number = self.phone_number.text
        username = self.username.text
        password = self.password.text
        print(f"Name of the individual:{username}")
        print(f"Submitted Phone Number: {phone_number}")
        print(f"Submitted Email: {email}")

        self.save_contact(username, phone_number, email, password)

    def on_login_button_press(self, instance):
        email = self.email.text
        phone_number = self.phone_number.text
        username = self.username.text
        password = self.password.text
        print(f"Name of the individual:{username}")
        print(f"Submitted Phone Number: {phone_number}")
        print(f"Submitted Email: {email}")

        self.save_contact(username, phone_number, email, password)


class Front_page(Screen):
    pass


class App(MDApp):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Login(name="login"))
        sm.add_widget(Front_page(name="Front Page"))
        return sm


App().run()
