from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class ImageApp(App):
     
     def build(self):
        layout = BoxLayout(orientation = 'vertical')
        button1 = Button(text = 'Button1')
        layout.add_widget(button1)

        button2 = Button(text = 'Button2')
        layout.add_widget(button2)
       
        return layout


ImageApp().run()