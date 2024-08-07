import re

def chatbot_response(user_input):
  """
  Simulates a rule-based chatbot response.

  Args:
    user_input: The user's message.

  Returns:
    The chatbot's response.
  """

  intents = {
    "greeting": ["hello", "hi", "hey"],
    "goodbye": ["bye", "goodbye", "see you"]
  }

  responses = {
    "greeting": "Hello there! How can I help you?",
    "goodbye": "Goodbye! Have a nice day."
  }

  for intent, keywords in intents.items():
    for keyword in keywords:
      if re.search(keyword, user_input, re.IGNORECASE):
        return responses[intent]

  return "I didn't understand that."

while True:
  user_input = input("You: ")
  if user_input.lower() == "quit":
    break
  response = chatbot_response(user_input)
  print("Chatbot:", response)
