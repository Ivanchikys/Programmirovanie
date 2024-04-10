from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class ImageApp(App):

    def build (self):
        layout = BoxLayout()

        layout_button = BoxLayout(orientation ='vertical')
        change_img = Button(text = 'Change Image',
                            size_hint = (0.5, 0.5),
                            ) 
        layout_button.add_widget(change_img)

        change_size = Button(text = 'Change size',
                            size_hint = (0.5, 0.5),
                            ) 
        layout_button.add_widget(change_size)

        change_font_family = Button(text = 'Change font family',
                            size_hint=(0.5, 0.5),
                            ) 
        layout_button.add_widget(change_font_family)
        layout.add_widget(layout_button)


        layout_label = BoxLayout(orientation = 'vertical')

        label_b1 = Label(text = 'Поменять картинку',
                         size_hint = (0.5, 0.5)
                         )
        layout_label.add_widget(label_b1)

        label_b2 = Label(text = 'Поменять размер',
                         size_hint = (0.5, 0.5)
                         )
        layout_label.add_widget(label_b2)

        label_b3 = Label(text = 'Поменять шрифт',
                         size_hint = (0.5, 0.5)
                         )
        layout_label.add_widget(label_b3)
        layout.add_widget(layout_label)

        
        return layout
ImageApp().run()