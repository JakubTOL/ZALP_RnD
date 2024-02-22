from kivy.app import App
import os

from kivy.uix.treeview import TreeView, TreeViewLabel
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        layout = GridLayout(cols=1)
        self.tv = TreeView()
        self.tv = TreeView(root_options=dict(text='root label'))
        dir_path = r'C:/zf-adas-learning-platform/resources/'
        for file in os.listdir(dir_path):
            if file.endswith('.mp4'):
                print(file)
                self.tv.add_node(TreeViewLabel(text=file))
        button = Button(text='Get node name', on_press=self.print_selected_node)
        layout.add_widget(self.tv)
        layout.add_widget(button)

        return layout

    def print_selected_node(self, obj):
        if self.tv.selected_node is not None:
            print(self.tv.selected_node.text)


if __name__ == '__main__':
    MyApp().run()
