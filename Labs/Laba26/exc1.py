from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.app import App

PATH = 'D:/Programmirovanie/Labs/Laba24/picture/'

class GridLayoutApp(App):
    def build(self):
        layout = GridLayout(cols = 3, rows = 3)   

        pictures = ['5.jpg', '6.jpg', '7.jpg', '8.jpg', '9.jpg', '10.jpg', '11.jpg', '12.jpg', '13.jpg',]

        for picture in pictures:
            img = Image(source = PATH + picture)
            layout.add_widget(img)
        
        return layout

if __name__ == '__main__':
    GridLayoutApp().run()
