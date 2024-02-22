import os

from kivy.clock import mainthread
from kivy.lang import Builder
from kivy.uix.textinput import TextInput


__filename = os.path.splitext(os.path.basename(__file__))[0] + '.kv'
__directory = os.path.dirname(__file__)
Builder.load_file(os.path.join(__directory, __filename))


class ScenarioUserInput(TextInput):
    """
    UserInput to collect information (numbers and chars/strings) from the scenario window.
    Used functions are decorated to run the UserInput code in the Kivy thread.
    """

    @mainthread
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @mainthread
    def open(self):
        super().open()