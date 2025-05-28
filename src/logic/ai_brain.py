psychology_faq = {
    "what is cognitive dissonance": "Cognitive dissonance is the mental discomfort experienced by a person who holds two or more contradictory beliefs, ideas, or values.",
    "what is anxiety": "Anxiety is an emotion characterized by feelings of tension, worried thoughts, and physical changes like increased blood pressure.",
    "who is sigmund freud": "Sigmund Freud was an Austrian neurologist and the founder of psychoanalysis."
}


def get_ai_response(message):
    message_lower = message.lower()

    # Simple greetings
    if any(greet_word in message_lower for greet_word in ["hello", "hi", "hey"]):
        return "Hi there! How can I assist you with psychology today?"

    # Direct FAQ lookup
    for question, answer in psychology_faq.items():
        if question in message_lower:
            return answer

    # Handle simple commands
    if "your name" in message_lower:
        return "I'm your AI psychology assistant."

    # Use domain.pyx functions for some fun queries
    if "factorial" in message_lower:
        import re
        match = re.search(r"factorial of (\d+)", message_lower)
        if match:
            n = int(match.group(1))
            from domain import factorial
            return f"The factorial of {n} is {factorial(n)}."
        else:
            return "Please tell me the number you want the factorial of."

    if "reverse" in message_lower:
        import re
        match = re.search(r"reverse (.+)", message_lower)
        if match:
            s = match.group(1)
            from domain import reverse_string
            return f"Reversed string: {reverse_string(s)}"
        else:
            return "Please tell me the string you want me to reverse."

    # Fallback
    return "That's interesting! Can you please elaborate more or ask another question?"
