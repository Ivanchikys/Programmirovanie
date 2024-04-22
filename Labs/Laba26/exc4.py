from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.slider import Slider
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.core.audio import SoundLoader

class GridLayoutApp(App):

    play_track = SoundLoader.load('C:/Users/ivanv/Downloads/soundpad.mp3')

    def play_music(self, instance):
        if self.play_track:
            self.play_track.play()

        else:
            self.play_track = self.stop_music()

    def stop_music(self, instance):
        self.play_track.stop()

    def build(self):                                                        #self.play_track.get_pos()
        Panel = GridLayout(cols = 4, spacing = 10)

        play = Button(text = 'start')
        play.bind(on_press = self.play_music)
        Panel.add_widget(play)

        stop = Button(text = 'stop')
        stop.bind(on_press = self.stop_music)
        Panel.add_widget(stop)

        lenght_track = Slider(min = 0, max = 100,
                        value_track = True, 
                        value_track_color =[0.65, 0.19, 0.58, 1],
                        )
        Panel.add_widget(lenght_track)


        Window.size = (600, 80)

        return Panel

if __name__ == '__main__':
    GridLayoutApp().run()