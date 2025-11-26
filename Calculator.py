import sys, os
import math
import kivy 
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.clock import Clock
kv_path = os.path.join(os.path.dirname(__file__), "Calculator.kv")
Builder.load_file(kv_path)

Window.size = (320, 465)
Window.minimum_width = 320
Window.minimum_height = 465


class MyLayout(Widget):
    saved_num = None
    result = ObjectProperty(None)
    symbol = None
    def on_result_text(self, text):
     
        Clock.schedule_once(self.adjust_font_size, 0)

    def adjust_font_size(self, *args):
        text = self.ids.result.text

        base_size = 40
        min_size = 25
        max_chars = 14
        shrink_per_char = 3

        if len(text) > max_chars:
            new_size = base_size - (len(text) - max_chars) * shrink_per_char
            if new_size < min_size:
                new_size = min_size
            self.ids.result.font_size = new_size
        else:
            self.ids.result.font_size = base_size
    
    def press_number(self, num):
        
        if self.result.text == "0" or getattr(self, "just_calculated", False):
            self.result.text = num
            self.just_calculated = False
        else:
            self.result.text += num
        self.adjust_font_size()
        
    def clear(self):
        self.result.text = "0"
        self.saved_num = None
    def plus(self):
        self.symbol = "+"
        current = float(self.result.text)

        if self.saved_num is None:
            self.saved_num = current
            self.result.text = "0"
            return
        if getattr(self, "just_calculated", False):
            self.result.text = "0"
            self.just_calculated = False
            return
        self.saved_num += current
        self.result.text = str(self.saved_num)
        self.just_calculated = True
    def minus(self):
        self.symbol = "-"
        current = float(self.result.text)

        if self.saved_num is None:
            self.saved_num = current
            self.result.text = "0"
            return
        if getattr(self, "just_calculated", False):
            self.result.text = "0"
            self.just_calculated = False
            return
        self.saved_num -= current
        self.result.text = str(self.saved_num)
        self.just_calculated = True
    def multiply(self):
        self.symbol = "x"
        current = float(self.result.text)

        if self.saved_num is None:
            self.saved_num = current
            self.result.text = "0"
            return
        if getattr(self, "just_calculated", False):
            self.result.text = "0"
            self.just_calculated = False
            return
        self.saved_num = current * self.saved_num
        self.result.text = str(self.saved_num)
        self.just_calculated = True
    def divide(self):
        self.symbol = "/"
        current = float(self.result.text)

        if self.saved_num is None:
            self.saved_num = current
            self.result.text = "0"
            return
        if getattr(self, "just_calculated", False):
            self.result.text = "0"
            self.just_calculated = False
            return
        self.saved_num = self.saved_num / current 
        self.result.text = str(self.saved_num)
        self.just_calculated = True
    def dot(self):
        put_dot = (".")
        self.result.text += put_dot
    def squareroot(self):
        current = float(self.result.text)
        self.result.text = str(math.sqrt(current))
    def square(self):
        current = float(self.result.text)
        self.result.text = str(current ** 2)
    def onedividedbyx(self):
        current = float(self.result.text)
        self.result.text = str(1/current)
    def CE(self):
        current = float(self.result.text)
        current = str("0")
        self.result.text = current
    def change_sign(self):
        if self.result.text == "0":
            return
        elif self.result.text.startswith("-"):
            self.result.text = self.result.text[1:]
        else:
            self.result.text = "-" + self.result.text
    def delete_last_number(self):
        if len(self.result.text) > 0:
            self.result.text = self.result.text[0:-1]
        if self.result.text == "":
            self.result.text = "0"
    def percentage(self):
        if self.symbol == '+':
            self.result.text = str(self.saved_num + self.saved_num * (float(self.result.text)/100))
            self.saved_num = None
        elif self.symbol == '-':
            self.result.text = str(self.saved_num - self.saved_num * (float(self.result.text)/100))
            self.saved_num = None
        elif self.symbol == '*':
            self.result.text = str(self.saved_num * (float(self.result.text)/100))
            self.saved_num = None
        elif self.symbol == '/':
            self.result.text = str(self.saved_num / (float(self.result.text)/100))
            self.saved_num = None
    def equal(self):
        if self.symbol == "+":
            current = float(self.result.text)
            self.result.text = str(self.saved_num + current) 
            self.saved_num = None
        elif self.symbol == "-":
            self.result .text = str(self.saved_num - float(self.result.text))
            self.saved_num = None
        elif self.symbol == "x":
            self.result.text = str(self.saved_num * float(self.result.text))
            self.saved_num = None
        elif self.symbol == "/":
            self.result.text = str(self.saved_num / float(self.result.text))
            self.saved_num = None
class Calculator(App):
    def build(self):
        return MyLayout()
    
if __name__ == "__main__":
    Calculator().run()
 