from kivy.app import App
from kivy.lang import Builder

main = Builder.load_string('''
Screen:
    Label:
        text: 'Hello World'
        font_size: '25sp'
        color: (6,3.6,3.7,5)
        size_hint: (1.0, 0.25)
                    
    Label:
        text: 'Vertical area'
        font_size: '25px'
        size_hint: (1.50, 1)
                           
    AsyncImage:
        source: 'https://icplpa.org/wp-content/uploads/2022/12/116035b31299625bb8cc41da4aa12e19.jpg'
        size_hint_x: 0.5
        allow_stretch: False

''')

class TestApp(App):
    def build(self):
        return main

if __name__ == '__main__':
    TestApp().run()