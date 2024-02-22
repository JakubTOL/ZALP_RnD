import subprocess
import sys
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock

kv = Builder.load_file('gui.kv')


def my_callback(dt):
    pass


class StartUpWindow(Screen):
    pass


# Declare both screens
class MainWindow(Screen):
    pass


class ScenarioRunnerWindow(Screen):
    def spinner_clicked(self, value):
        self.ids.dropdown_label.text = f'Selected:  {value}'


class TutorialScenariosWindow(Screen, FloatLayout):
    pass


class ChallengeScenariosWindow(Screen):
    pass


class ManualModeWindow(Screen):
    pass


class GUI(App):
    def build(self):
        # Create the screen manager
        SM = ScreenManager()
        SM.add_widget(StartUpWindow(name='startup_window'))
        SM.add_widget(MainWindow(name='main_window'))
        SM.add_widget(ScenarioRunnerWindow(name='scenario_runner_window'))
        SM.add_widget(TutorialScenariosWindow(name='tutorial_window'))
        SM.add_widget(ChallengeScenariosWindow(name='challenge_window'))
        SM.add_widget(ManualModeWindow(name='manual_window'))

        self.icon = 'app_icon.png'
        #Clock.schedule_once(my_callback, -1)
        return SM

    @staticmethod
    def GetUserVoltage(text_):
        print(text_)

    def player(self):
        secondApp = subprocess.Popen('python3 video_openCV.py', shell=False)



if __name__ == '__main__':
    GUI().run()
