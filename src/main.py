from kivy.app import App
from src.screens.chat_screen import ChatScreen
from kivy.lang import Builder

Builder.load_file("ui/chat.kv")

class AIHumanApp(App):
    def build(self):
        return ChatScreen()

if __name__ == "__main__":
    AIHumanApp().run()
