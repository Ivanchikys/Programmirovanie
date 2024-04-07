from kivy.app import App
from kivy.uix.image import Image

PATH = 'D:/Programmirovanie/Labs/Laba24/picture/'

class ImageApp(App):
    def build (self):
        image = Image(source= PATH + '5.jpg',
                      pos_hint = {'center_x':0.5, 'center_y':0.5})
        
        return image
    
ImageApp().run()