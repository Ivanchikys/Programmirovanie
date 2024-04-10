from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown

PATH = 'D:/Programmirovanie/Labs/Laba24/picture/'

class ImageApp(App):
    def change_img_size(self, instance, touch):
        #print(instance.size_hint)
        if instance.size_hint == [1, 1]:
            instance.size_hint = (0.75, 0.75)
        else:
            instance.size_hint = (1, 1)

    def select_image(self, instance, list_image):
        self.image.source = PATH + list_image
        self.image.size_hint = (1, 1)
        self.dropdown.dismiss()

    def build (self):
        layout = BoxLayout(orientation = 'vertical')

        layout_image = BoxLayout()
        self.image = Image(source = PATH + '5.jpg',
                      pos_hint = {'center_x': 0.5, 'center_y': 0.5})
        self.image.bind(on_touch_down=self.change_img_size)
        layout_image.add_widget(self.image)


        self.dropdown = DropDown()
        images = ['23.jpg','14.jpg','12.jpg','5.jpg','21.jpg']

        for image in images:  
           list_image =  Button(text = image, size_hint_y = None, height = 30)
           list_image.bind(on_release = lambda list_image, img = image: self.select_image(list_image, img))
           self.dropdown.add_widget(list_image)
           


        layout_button = BoxLayout(orientation = 'vertical', size_hint_y = 0.15)
        change_img = Button(text = 'Change Image',
                            size_hint = (0.25, 0.25),
                            pos_hint = {'center_x': 0.5, 'center_y': 0.5}
                            ) 
        change_img.bind(on_release = self.dropdown.open)
        layout_button.add_widget(change_img)
        
        layout.add_widget(layout_image)
        layout.add_widget(layout_button)
        

        return layout
ImageApp().run()