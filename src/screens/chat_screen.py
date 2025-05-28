from kivy.uix.boxlayout import BoxLayout
from src.logic.ai_brain import get_ai_response
from src.logic.voice_output import speak
from src.logic.voice_input import listen

class ChatScreen(BoxLayout):
    def send_message(self):
        user_input = self.ids.user_input.text
        self.ids.chat_history.text += f"You: {user_input}\n"
        self.ids.user_input.text = ""

        response = get_ai_response(user_input)
        self.ids.chat_history.text += f"AI: {response}\n"
        speak(response)

    def use_voice(self):
        user_input = listen()
        if user_input:
            self.ids.chat_history.text += f"You (voice): {user_input}\n"
            response = get_ai_response(user_input)
            self.ids.chat_history.text += f"AI: {response}\n"
            speak(response)
