from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import AsyncImage
from kivy.uix.label import Label

class ImageApp(App):
     
     def build(self):
        layout = BoxLayout(orientation = 'horizontal')
        image = AsyncImage(source = 'https://www.cleverfiles.com/howto/wp-content/uploads/2018/03/minion.jpg')
        label = Label(text='Am grammar Nazy',
                      font_size='20px',
                      )
        layout.add_widget(image)
        layout.add_widget(label)
        
        return layout


ImageApp().run()