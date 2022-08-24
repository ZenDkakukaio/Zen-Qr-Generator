from kivy.uix.screenmanager import ScreenManager, FallOutTransition
from kivymd.uix.taptargetview import MDTapTargetView
from kivymd.toast import toast
import json


with open("media/media.json") as j:
    data = json.load(j)



class HomeScanGeneretor(ScreenManager):
    data_logo = data["media1"]["1"]

    def __init__(self, **kwargs):
        super(HomeScanGeneretor, self).__init__(**kwargs)






    def tap_target_start(self):
        self.transition = FallOutTransition(duration=.5)
        self.current = self.ids.id_screenwork.name


