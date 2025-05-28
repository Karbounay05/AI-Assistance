from kivy.app import App
from src.screens.chat_screen import ChatScreen
from kivy.lang import Builder
import domain

Builder.load_file("ui/chat.kv")

class AIHumanApp(App):
    def build(self):
       return ChatScreen()

if __name__ == "__main__":
   AIHumanApp().run()

print(domain.some_function())
print(domain.some_function())
print(domain.add(10, 5))
print(domain.greet("Ahmed"))
print(domain.factorial(5))
print(domain.reverse_string("Cython"))