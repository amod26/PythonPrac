#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# $ python -m pip install kivy
# $ python -m pip install ffpyplayer


# In[1]:


import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.config import Config
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
Config.set('graphics', 'resizable', True)
Config.set('kivy', 'keyboard_mode', 'systemandmulti')
kivy.require("1.11.0")


# In[2]:


class ConnectPage(GridLayout):
    def __init__(self):
        super().__init__(self, **kwargs)
        self.cols = 2

        self.add_widget(Label(text="IP:"))

        self.ip.TextInput(multiline=False)
        self.add_widget(self.ip)

        self.add_widget(Label(text="Port:"))

        self.port.TextInput(multiline=False)
        self.add_widget(self.port)

        self.add_widget(Label(text="UserName:"))

        self.username.TextInput(multiline=False)
        self.add_widget(self.username)


class Dhaasu(App):
    def built(self):
        return ConnectPage()


if __name__ == '__main__':
    Dhaasu().run()


# In[ ]:
