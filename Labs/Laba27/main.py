from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.core.audio import SoundLoader
from kivy.core.window import Window
from kivy.clock import Clock

class AudioPlayerApp(App):

    path_track = SoundLoader.load('C:/Users/ivanv/Downloads/soundpad.mp3')

    def play_music(self, instance):

        if self.path_track:
            self.root.ids.lenght_track.max = self.path_track.length
            self.path_track.play()
            
    def update_function_of_slider(self, instance):
        if self.path_track.state == 'play':
            self.root.ids.lenght_track.value = self.path_track.get_pos()
        
    def stop_music(self, instance):
        self.path_track.stop()
    
    def seek_music(self, instance, value):
        self.path_track.seek(value)

    def build(self):
        Window.size = (600, 80)
        Clock.schedule_interval(self.update_function_of_slider, 1)

        return GridLayout()

if __name__ == '__main__':
   AudioPlayerApp().run()