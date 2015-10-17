import kivy
kivy.require('1.0.6') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.core.window import Window
from plyer import camera #object to read the camera
from kivy.uix.floatlayout import FloatLayout #the UI layout
import time

Builder.load_string('''
<MenuScreen>:
    BoxLayout:
        Button:
            text: 'Add NCR'
            on_press: root.manager.current = 'ncr'
        
<Add_new_ncr>:
    nam: str(noa)
    job: nosi
    GridLayout:
        cols: 2
        Label:
            text: 'Name of area'
        TextInput:
            id: noa
            multiline: False
        Label:
            text: 'Name of Staff Involeved'
        TextInput:
            id: nosi
        Label:
            text: 'Issue'
        TextInput:
            id: issue
        Button:
            text: 'Back to menu'
            on_press: root.manager.current = 'menu'
        Button:
            text: 'Save'
            on_press: app.save(noa.text, nosi.text, issue.text)
        Button:
            text: 'Camera'
            on_press: app.Camera()
''')

class MenuScreen(Screen):
    pass

class Add_new_ncr(Screen):
    pass

sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(Add_new_ncr(name='ncr'))

class MyApp(App):
    def build(self):
        return sm

    def save(self, name, nameofstaff, ncrissue):
        fob = open('/storage/sdcard0/ncrreport.txt','a')
        fob.write("<name>")
        fob.write(name)
        fob.write("</name>\n")
        fob.write("<namestaff>")
        fob.write(nameofstaff)
        fob.write("<namestaff>\n")
        fob.write("<ncr>")
        fob.write(ncrissue)
        fob.write("</ncr>\n")
        fob.close()
        
    def Camera(self):
        camera.take_picture('/storage/sdcard0/example.jpg', self.done)

    def done(self): #receive e as the image location
        clot = e; #update the label to the image location
        imf = open('/storage/sdcard0/ncrreport.txt','a')
        imf.write("<image>")
        imf.write(clot)
        imf.write("</image>")
        imf.close()
        pass

     
		
if __name__ == '__main__':
    MyApp().run()
