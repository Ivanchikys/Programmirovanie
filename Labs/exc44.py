from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.audio import SoundLoader

class AudioPlayerApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        play_button = Button(text='Play Audio')
        play_button.bind(on_press=self.play_audio)
        layout.add_widget(play_button)
        return layout

    def play_audio(self, instance):
        audio = SoundLoader.load('C:/Users/ivanv/Downloads/soundpad.mp3')
        if audio:
            audio.play()
        else:
            print("Ошибка загрузки аудиофайла")

if __name__ == '__main__':
    AudioPlayerApp().run()
