from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout

PATH = 'D:/Programmirovanie/Labs/Laba24/picture/'

class ImageApp(App):
    def change_img_size(self, instance, touch):
        print(instance.size_hint)
        if instance.size_hint == [1, 1]:
            instance.size_hint = (0.75, 0.75)
        else:
            instance.size_hint = (1, 1)


    def build (self):
        layout = BoxLayout()
        self.image = Image(source= PATH + '5.jpg',
                      pos_hint = {'center_x':0.5, 'center_y':0.5})
        self.image.bind(on_touch_down=self.change_img_size)
        layout.add_widget(self.image)
        
        return layout
ImageApp().run()