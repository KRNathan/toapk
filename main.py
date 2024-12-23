from kivy.lang import Builder
from kivymd.app import MDApp

KV = '''
MDBoxLayout:
    orientation: 'vertical'
    MDToolbar:
        title: "My First KivyMD App"
        md_bg_color: app.theme_cls.primary_color
    MDLabel:
        text: "Hello, KivyMD!"
        halign: 'center'
'''

class MyApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

if __name__ == '__main__':
    MyApp().run()