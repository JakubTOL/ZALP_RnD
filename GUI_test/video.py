from kivymd.app import MDApp
from kivy.uix.videoplayer import VideoPlayer


class MainApp(MDApp):
    title = "Sample of video"

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        #  define player
        player = VideoPlayer(source='C:/Users/z0175645/Downloads/sample_vid.mp4')
        player.state = 'play'
        player.options = {'eos': 'loop'}
        player.allow_stretch = True
        return player


if __name__ == "__main__":
    MainApp().run()
# https://github.com/kivy/kivy/issues/6672
# https://matham.github.io/ffpyplayer/installation.html
