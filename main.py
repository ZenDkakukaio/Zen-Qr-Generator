from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.core.window import Window
from kivymd.uix.button import MDRaisedButton

from controller.home import HomeScanGeneretor

import json

with open("media/media.json") as j:
    data = json.load(j)





class MyApp(MDApp):
    def build(self):
        self.title = "Zen SCan Generator"
        self.icon = data["media1"]["1"]
        self.theme_cls.theme_style = "Light"
        self.load_all_file_kv()

        return HomeScanGeneretor()



    def load_all_file_kv(self):
        Builder.load_file("views/home.kv")
        Builder.load_file("views/screen_work.kv")




if __name__ == '__main__':
    obj = MyApp()
    obj.run()