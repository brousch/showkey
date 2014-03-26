# -*- coding: utf-8 -*-
#!/usr/bin/env python

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
 
 
kv = """
<Test>:
    orientation: 'vertical'
    padding: '8sp','8sp'
    Label:
        id: output
        text: ''
    Button:
        text: 'Clear'
        on_press: root.clear_input
        size_hint: 1, None
        height: self.texture_size[1] + (2 * root.padding[1])
"""
 
Builder.load_string(kv)
 
 
class Test(BoxLayout):
    output = ObjectProperty()
    
    def __init__(self, **kwargs):
        super(Test, self).__init__(**kwargs)
    
    def clear_input(self):
        self.output.text = ''
 
 
class TestApp(App):
    def build(self):
        return Test()
 
if __name__ == '__main__':
    TestApp().run()