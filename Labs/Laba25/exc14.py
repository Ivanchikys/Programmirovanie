from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button

class MainApp(App):
    def build(self):
        layout = FloatLayout()

        BUTTON_SIZE = (0.2, 0.1)
        
        button = Button(text = "Кнопка",
                         size_hint = BUTTON_SIZE,
                         pos_hint = {"right": 1, "bottom": 1})
        
        layout.add_widget(button)
        
        return layout

if __name__ == "__main__":
    MainApp().run()