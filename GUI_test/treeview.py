from kivy.app import App
from kivy.lang import Builder
from kivy.uix.treeview import TreeView, TreeViewLabel
from kivy.core.window import Window
from kivy.clock import Clock


def my_callback(dt):
        pass
    
class GenTree(TreeView):
    # dictionaries for nodes and sub nodes generation
    generals = [f'MainLevel {str(i)}' for i in range(0, 10, 1)]
    sub_nodes = [f'SubLevel {str(i)}' for i in range(0, 15, 1)]

    def __init__(self, **kwargs):
        super(GenTree, self).__init__(**kwargs)

    # generate main level tree nodes
    def add_Structure(self):
        for item in self.generals:
            self.add_node(TreeViewLabel(text=item))
    # for each main node generate sub node according to sub_note dictionary
        for node in self.root.nodes:
            if "MainLevel" in node.text:
                for item in self.sub_nodes:
                    self.add_node(TreeViewLabel(text=item), node)
                    
        Clock.schedule_interval(my_callback, 2)


class TreeViewApp(App):
    def build(self):
        return Builder.load_file("gentree.kv")
    
    def update(self, *args):
        self.name.text = str(self.current_i)
        self.current_i += 1
        if self.current_i >= 50:
            Clock.unschedule(self.update)


TreeViewApp().run()