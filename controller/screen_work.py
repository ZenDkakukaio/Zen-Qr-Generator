from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition
from kivymd.toast import toast
from kivy.properties import StringProperty


import re
import qrcode
import plyer
import json

with open("media/media.json") as j:
    data = json.load(j)



class ScreenWork(Screen):
    data_logo = data["media1"]["1"]
    path_img = StringProperty("")

    def __init__(self, **kwargs):
        super(ScreenWork, self).__init__(**kwargs)



    def generate_qr_code(self):
        pattern_space_text = re.compile("\s+")
        if pattern_space_text.match(self.ids.id_url_field.text) or self.ids.id_url_field.text == "":
            toast("Veuillez remplir les champs...")

        elif pattern_space_text.match(self.ids.id_name_image.text) or self.ids.id_name_image.text == "":
            toast("Une erreur s'est produite, veuillez reprendre...")

        elif not pattern_space_text.match(self.ids.id_url_field.text) and \
           not pattern_space_text.match(self.ids.id_name_image.text):

            code = qrcode.QRCode(version=1.0, box_size=15, border=4)
            code.add_data(self.ids.id_url_field.text)
            code.make(fit=True)
            img = code.make_image(fill='Black', back_color='White')
            img.save(f"media/{self.ids.id_name_image.text}.png")
            plyer.notification.notify(
                title = 'Zen QR Code Generator', message= "Code Qr Géneré avec succès"
            )
            toast("validation du Processus...")



        else:
            toast("Une erreur s'est produite, veuillez reprendre...")
            plyer.notification.notify(
                title='Zen QR Code Generator', message="une erreur s'est produite, veuillez reprendre"
            )



    def push_image(self):
        self.ids.id_image_generate_qr_code.source = f"media/{self.ids.id_name_image.text}.png"

