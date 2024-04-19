from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.app import App

class GridLayoutApp(App):
    def build(self):
        layout = GridLayout(cols = 4, rows = 2) 

        colors_list = ['red','pink','brown','purple','green','blue','yellow','orange']
        for num in range(8):
            for color in colors_list:
                button = Button(text = '', background_color = color)
                layout.add_widget(button)
            return layout

if __name__ == '__main__':
    GridLayoutApp().run()
