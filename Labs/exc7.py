from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

PATH = 'D:/Programmirovanie/Labs/Laba24/picture/'

class ImageApp(App):

    def build (self):
        layout = BoxLayout(orientation ='horizontal')

        image = Image(source= PATH + '5.jpg',
                      pos_hint = {'center_x':0.5, 'center_y':0.5})
        layout.add_widget(image)
        

        change_img = Button(text='Change Image',
                            size_hint=(0.25, 0.25),
                            pos_hint={'center_x':0.5, 'center_y': 0.2}
                            ) 
        layout.add_widget(change_img)

        change_size = Button(text='Change size',
                            size_hint=(0.25, 0.25),
                            pos_hint={'center_x':0.5, 'center_y': 0.2}
                            ) 
        layout.add_widget(change_size)
        
        return layout
ImageApp().run()