from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class ImageApp(App):
     
     def build(self):
        layout = BoxLayout(orientation = 'vertical')
        label1 = Label(text = 'Am grammar Nazy',
                      font_size = '20px',
                      pos_hint = {'center_x': 0.25 , 'center_y': 0.75}
                      )
        label2 = Label(text = 'Am grammar Nazy',
                      font_size = '12px',
                      color = (0, 2, 4, 5),
                      font_family = 'Times New Roman',
                      pos_hint = {'center_x': 0.15 , 'center_y': 0.2}
                      )
        label3 = Label(text = 'Am grammar Nazy',
                      font_size = '53px',
                      color = (1,6,6,6),
                      font_family = 'dance',
                      pos_hint = {'center_x': 0.4 , 'center_y': 0.65}
                      )
        label4 = Label(text = 'Am grammar Nazy',
                      font_size = '32px',
                      color = (0, 8, 0, 2),
                      font_family = 'Arial',
                      pos_hint = {'center_x': 0.7 , 'center_y': 0.30}
                      )
        
        layout.add_widget(label1)
        layout.add_widget(label2)
        layout.add_widget(label3)
        layout.add_widget(label4)
        
        return layout

ImageApp().run()