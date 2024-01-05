# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 18:31:32 2023

@author: CEO1
"""

from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.card import MDCard
from kivy.uix.popup import Popup
from kivymd.uix.anchorlayout import MDAnchorLayout
from kivy.uix.screenmanager import ScreenManager, SlideTransition
from kivymd.uix.textfield import MDTextField, MDTextFieldRect
from kivymd.uix.pickers import MDTimePicker
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDFlatButton
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.dialog import MDDialog
import time
from time import sleep
import calendar
import numpy
from kivymd.uix.button import MDIconButton
from kivymd.uix.screen import MDScreen
import json
from kivymd.uix.pickers import MDDatePicker


# Login Page
class Login(MDScreen):
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
        self.phone_number = MDTextField(icon_left='phone',
                                        hint_text="Phone Number",
                                        font_size='18sp',
                                        size_hint_y=None,
                                        height='60dp')
        self.main_card.add_widget(self.phone_number)
        self.message_login = MDLabel(text="Login successful")
        self.message_signup = MDLabel(text="Signup successful")
        small_grid = MDGridLayout(cols=2, spacing=20, padding=20, size_hint=(1, 1))
        login_button = MDRectangleFlatButton(text='Login', height='60dp', on_press=self.on_login_button_press)
        sign_up_button = MDRectangleFlatButton(text='Sign Up', height='60dp', on_press=self.on_signup_button_press)
        small_grid.add_widget(login_button)
        small_grid.add_widget(sign_up_button)
        self.welcome = MDLabel(text="Welcome Back", font_size='20sp')
        self.main_card.add_widget(small_grid)
        self.add_widget(self.anchor_layout)

        # The information dialog
        self.dialog = MDDialog(size_hint=(0.9, 0.9),
                               title="Tell us more about yourself",
                               buttons=[MDFlatButton(text="skip", on_release=self.dialogue),
                                        MDFlatButton(text="Proceed", on_release=self.enter_other_information)]
                               )
       

# dismiss function for the dialog
    def dialogue(self, instance):
        self.dialog.dismiss()
        next_page = Front()
        MyApp.change(self, next_page)

    # function for saving the user information in a json file
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

# function for the signup button the login page
    def on_signup_button_press(self, instance):
        email = self.email.text
        phone_number = self.phone_number.text
        username = self.username.text
        password = self.password.text
        print(f"Name of the individual:{username}")
        print(f"Submitted Phone Number: {phone_number}")
        print(f"Submitted Email: {email}")
        self.main_card.add_widget(self.message_signup)
        self.save_contact(username, phone_number, email, password)
        self.clear_content()
        self.show_dialog()

# function for the login button in the login page
    def on_login_button_press(self, instance):
        email = self.email.text
        phone_number = self.phone_number.text
        username = self.username.text
        password = self.password.text
        print(f"Name of the individual:{username}")
        print(f"Submitted Phone Number: {phone_number}")
        print(f"Submitted Email: {email}")
        self.main_card.add_widget(self.message_login)
        self.save_contact(username, phone_number, email, password)
        self.save_contact(username, phone_number, email, password)
        next_page = Front()
      #  sleep(3)
        MyApp.change(self, next_page)

# function to clear the content of the screen
    def clear_content(self):
        # Remove all children (content) from the screen
        self.anchor_layout.clear_widgets()

# function that shows the dialog on click
    def show_dialog(self):
        self.dialog.open()

# To remove the dialog and show front page
    def enter_other_information(self, instance):
        self.dialog.dismiss()
        next_page = Extra()
        MyApp.change(self, next_page)


# class for the extra page for more information
class Extra(MDScreen):
    def __init__(self, **kwargs):
        super(Extra, self).__init__(**kwargs)
        self.card = MDCard(size_hint=(0.8, 0.8),
                           elevation=7,
                           pos_hint={'center_x': 0.5, 'center_y': 0.5},
                           orientation='vertical')
        self.content = MDGridLayout(cols=1, spacing="20dp", padding=10)
        self.title = MDLabel(text="More Information", font_style="H5")
        self.content.add_widget(self.title)
        self.big_name = MDLabel(text="Enter full name")
        self.content.add_widget(self.big_name)
        self.name_field = MDTextFieldRect(font_size='18sp',
                                          size_hint_y=None,
                                          width=80,
                                          height=50,
                                          hint_text="e.g John Doe",
                                          _primary_color=(0, 0, 0, 1),
                                          background_color=(0, 0, 0, 0.05)
                                          )
        self.content.add_widget(self.name_field)
        self.status_text = MDLabel(text="Relationship Status")
        self.content.add_widget(self.status_text)
        self.status_entry = MDTextFieldRect(font_size='18sp',
                                            size_hint_y=None,
                                            width=80,
                                            height=50,
                                            hint_text="e.g Single",
                                            _primary_color="cyan",
                                            background_color=(0, 0, 0, 0.05)
                                            )
        self.content.add_widget(self.status_entry)
        self.general_email_text = MDLabel(text="Occupation")
        self.email_entry = MDTextFieldRect(font_size='18sp',
                                           size_hint_y=None,
                                           width=80,
                                           height=50,
                                           _primary_color="cyan",
                                           background_color=(0, 0, 0, 0.1)
                                           )
        self.content.add_widget(self.general_email_text)
        self.content.add_widget(self.email_entry)
        self.location = MDLabel(text="Country")
        self.country = MDTextFieldRect(font_size='18sp',
                                       size_hint_y=None,
                                       width=80,
                                       height=50,
                                       _primary_color="cyan",
                                       background_color=(0, 0, 0, 0.1)
                                       )
        self.content.add_widget(self.location)
        self.content.add_widget(self.country)
        self.card.add_widget(self.content)
        self.add_widget(self.card)
        self.done = MDRectangleFlatButton(text="Done",
                                          on_release=self.done_button_press,
                                          md_bg_color=(1, 1, 1, 0.7),
                                          pos_hint={'center_x': 0.9, 'center_y': 0.05},
                                          size_hint=(0.005, 0.0005))
        self.add_widget(self.done)

    def done_button_press(self, instance):
        next_page = Front()
        MyApp.change(self, next_page)


class Front(MDScreen):
    def __init__(self, **kwargs):
        super(Front, self).__init__(**kwargs)
        self.handler = MDGridLayout(cols=3, rows=1, spacing=15, padding=10)
        self.tab_card = MDCard(orientation="vertical",
                               size_hint=(0.07, 1),
                               padding=(10, 10, 10, 10),
                               ripple_behavior=False,
                               elevation=7
                               )
    # widget under the tab_card
        self.tab_layout = MDGridLayout(cols=1, padding=0, spacing=10)

        self.home_button = MDIconButton(icon="home", size_hint=(0.001, 0.002),
                                        pos_hint={'center_y': 0.05, 'center_x': 0.4},
                                        on_release=self.home_activate)

        self.workspace_button = MDIconButton(icon="briefcase", size_hint=(0.002, 0.002),
                                             pos_hint={'center_y': 0.05, 'center_x': 0.4},
                                             on_release=self.workspace_activate)

        self.cover_space_i = MDLabel(text="", size_hint=(0.76, 0.01))

        self.email_button = MDIconButton(icon="email", size_hint=(0.001, 0.002),
                                         pos_hint={'center_y': 0.05, 'center_x': 0.4},
                                         on_release=self.meeting_activate)

        self.connect_button = MDIconButton(icon="earth", size_hint=(0.001, 0.002),
                                           pos_hint={'center_y': 0.05, 'center_x': 0.4},
                                           on_release=self.connect_activate)

        self.register_button = MDIconButton(icon="account-circle", size_hint=(0.001, 0.002),
                                            pos_hint={'center_y': 0.05, 'center_x': 0.4},
                                            on_release=self.profile_activate)

        self.main_card = MDCard(orientation="vertical",
                                size_hint=(0.88, 1),
                                padding=(10, 10, 10, 10),
                                ripple_behavior=True,
                                elevation=7
                                )

    # widgets under the main card
        # widget subject to home page
        self.home_layout = MDGridLayout(cols=1, spacing=20, padding=10)
        self.label_home = MDLabel(text="This is the home page")
        self.home_layout.add_widget(self.label_home)

        # widget subject to the work page
        self.work_layout = MDScrollView()
        self.work_grid = MDGridLayout(cols = 2, spacing = 20)
        self.note_card = MDCard(size_hint=(0.3, 0.3),
                                elevation=5,
                                orientation='vertical'
                                )
        self.todo_list = MDCard(size_hint=(0.3, 0.3),
                                elevation=5,
                                orientation = 'vertical')
        self.work_grid.add_widget(self.todo_list)
        self.work_grid.add_widget(self.note_card)
        self.work_layout.add_widget(self.work_grid)

        # widget subject to the email page
        self.email_layout = MDGridLayout(cols=1, spacing=20, padding=10)
        self.email_label = MDLabel(text="This is the email layout")
        self.email_layout.add_widget(self.email_label)

        # widgets subject to the connection page
        self.connect_layout = MDGridLayout(cols=1, spacing=20, padding=10)
        self.connect_label = MDLabel(text="This is the connection layout")
        self.connect_layout.add_widget(self.connect_label)

        # widgets subject to the profile page
        self.profile_layout = MDGridLayout(cols=1, spacing=20, padding=10)
        self.profile_label = MDLabel(text="This is your profile Page")
        self.profile_layout.add_widget(self.profile_label)

        self.tool_card = MDCard(orientation="vertical",
                                size_hint=(0.05, 1),
                                padding=(10, 10, 10, 10),
                                ripple_behavior=False,
                                elevation=7
                                )

        self.tool_layout = MDGridLayout(cols=1, padding=0, spacing=50)

        self.cover_space_ii = MDLabel(text="", size_hint=(0.72, 0.01))

        self.calender = MDIconButton(icon='calendar', size_hint=(0.001, 0.0013),
                                     pos_hint={'center_y': 0.05, 'center_x': 0.4},
                                     on_release=self.activate_calendar)

        self.time = MDIconButton(icon='timer', size_hint=(0.001, 0.0013),
                                 pos_hint={'center_y': 0.05, 'center_x': 0.4},
                                 on_release=self.activate_timer)

        self.calculator = MDIconButton(icon='calculator', size_hint=(0.001, 0.0013),
                                       pos_hint={'center_y': 0.05, 'center_x': 0.4})
                                   #    on_release=self.activate_calculator

        self.location = MDIconButton(icon='map-marker', size_hint=(0.001, 0.0013),
                                     pos_hint={'center_y': 0.05, 'center_x': 0.4})
                                     # on_release=self.activate_location)

        self.settings = MDIconButton(icon="cog", size_hint=(0.001, 0.0013),
                                     pos_hint={'center_y': 0.05, 'center_x':0.4})

        self.date_dialog = MDDatePicker()

        self.time_dialog = MDTimePicker()

        self.inform_save = MDDialog(size_hint=(0.9, 0.9),
                                    title="Alarm has been scheduled",
                                    buttons=[MDFlatButton(text="ok", on_release=self.assurance)]
                                    )
                                    

    # adding all widgets
        # adding minor widget to the tab card
        self.tab_layout.add_widget(self.home_button)
        self.tab_layout.add_widget(self.workspace_button)
        self.tab_layout.add_widget(self.cover_space_i)
        self.tab_layout.add_widget(self.email_button)
        self.tab_layout.add_widget(self.connect_button)
        self.tab_layout.add_widget(self.register_button)
        self.tab_card.add_widget(self.tab_layout)

        # adding just the home layout to the main card
        self.main_card.add_widget(self.home_layout)

        # adding minor widget to the tool card
        self.tool_layout.add_widget(self.calender)
        self.tool_layout.add_widget(self.time)
        self.tool_layout.add_widget(self.calculator)
        self.tool_layout.add_widget(self.location)
        self.tool_layout.add_widget(self.cover_space_ii)
        self.tool_layout.add_widget(self.settings)

        self.tool_card.add_widget(self.tool_layout)

        # adding three major cards to the handler
        self.handler.add_widget(self.tab_card)
        self.handler.add_widget(self.main_card)
        self.handler.add_widget(self.tool_card)
        self.add_widget(self.handler)

    # functions for the layout for the card
    def home_activate(self, instance):
        self.main_card.clear_widgets()
        self.main_card.add_widget(self.home_layout)

    def workspace_activate(self, instance):
        self.main_card.clear_widgets()
        self.main_card.add_widget(self.work_layout)

    def meeting_activate(self, instance):
        self.main_card.clear_widgets()
        self.main_card.add_widget(self.email_layout)

    def connect_activate(self, instance):
        self.main_card.clear_widgets()
        self.main_card.add_widget(self.connect_layout)

    def profile_activate(self, instance):
        self.main_card.clear_widgets()
        self.main_card.add_widget(self.profile_layout)

    def activate_calendar(self, instance):
        self.date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        self.date_dialog.open()

    def on_save(self, instance, value, date_range):
        print(instance, value, date_range)

    def on_cancel(self, instance, value):
        '''Events called when the "CANCEL" dialog box button is clicked.'''

    def activate_timer(self, instance):
        self.time_dialog.bind(on_save=self.on_save)
        self.time_dialog.open()

    def on_save(self, instance, value):
        self.inform_save.open()
        print(value)

    def assurance(self, instance):
        self.inform_save.dismiss()


# class for calculator popup
class Calculator(Popup):
    def __init__(self, **kwargs):
        super(Calculator, self).__init__(**kwargs)
        self.content = MDGridLayout(cols = 1, rows= 2, spacing = 10)
        entry_field = MDTextFieldRect(font_size = '16sp',
                                      heigth = 40,
                                      padding = 20
                                      )
        self.buttons = MDGridLayout(rows = 4, spacing = 7)

        # adding buttons
        # remember to change the text to icon
        self.button_1 = MDIconButton(text = "1")
        self.button_2 = MDIconButton(text = "2")
        self.button_3 = MDIconButton(text = "3")
        self.button_4 = MDIconButton(text = "4")
        self.button_5 = MDIconButton(text = "5")
        self.button_6 = MDIconButton(text = "6")
        self.button_7 = MDIconButton(text = "7")
        self.button_8 = MDIconButton(text = "8")
        self.button_9 = MDIconButton(text = "9")
        self.button_0 = MDIconButton(text = "0")
        self.button_ = MDIconButton(text = "=")
        self.button_add = MDIconButton(text="+")
        self.button_sub = MDIconButton(text = "-")
        self.button_mult = MDIconButton(text = "*")
        self.button_div = MDIconButton(text="/")
        self.button_cos = MDIconButton(text = "cos")
        self.button_tan = MDIconButton(icon="")
        self.button_sin = MDIconButton(icon = "")
        self.button_root = MDIconButton(icon="")



class MyApp(MDApp):
    def build(self):
        sm = ScreenManager(transition=SlideTransition())
        sm.add_widget(Login(name="login"))
        self.theme_cls.theme_style = "Dark"  # or Light
        self.theme_cls.material_style = "M2"
        return sm

    def change(self, next_page):
        MDApp.get_running_app().root.remove_widget(self)
        MDApp.get_running_app().root.add_widget(next_page)


MyApp().run()


