from kivy.app import App
from kivy.lang import Builder

root = Builder.load_string('''
Screen:
    Label:
        text: 'Hello world'
        font_size: '20sp'
        color: (1,0.5,0.5,1)
        size_hint: (1.0, 0.17)
                    
    Label:
        text: 'String No 2'
        font_size: '20px'
        size_hint: (1.75, 0.83)
                           
    AsyncImage:
        source: 'https://www.google.com/logos/doodles/2024/celebrating-james-baldwin-6753651837110181-2x.png'
        size_hint_x: 0.4
        allow_stretch: False

''')

class TestApp(App):
    def build(self):
        return root

if __name__ == '__main__':
    TestApp().run()