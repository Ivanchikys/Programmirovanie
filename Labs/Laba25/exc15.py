from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from random import randint

class DraggableButton(Button):
   def on_touch_move(self, touch):
      if touch.grab_current == self:
         self.pos = (self.pos[0] + touch.dx, self.pos[1] + touch.dy)

class MyApp(App):
   def build(self):
      layout = FloatLayout()

      BUTTON_SIZE = (0.2, 0.1)
      BUTTONS_NUM = 5

      for i in range(BUTTONS_NUM):
            button = DraggableButton(text = f"Кнопка {i+1}",
                                     size_hint = BUTTON_SIZE,
                                     pos = (randint(0, 600), randint(0, 600)))
            layout.add_widget(button)

      return layout

if __name__ == '__main__':
   MyApp().run()