import google.generativeai as genai
from config import GEMINI_API_KEY
import sys

class Chatbot:
    def __init__(self):
        genai.configure(api_key=GEMINI_API_KEY)
        self.model = genai.GenerativeModel('gemini-2.0-flash')
        self.chat = self.model.start_chat(history=[])
        print("🤖 Welcome to Gemini 2.0 Flash Chatbot")
        print("Type 'quit', 'exit', or 'bye' to end.\n")

    def get_response(self, user_input):
        try:
            response = self.chat.send_message(user_input)
            return response.text
        except Exception as e:
            return f"⚠️ Error: {str(e)}"

    def run(self):
        while True:
            try:
                user_input = input("👩 You: ").strip()

                if not user_input:
                    continue  # ignore empty input
                
                if user_input.lower() in ['quit', 'exit', 'bye']:
                    print("🤖 Chatbot: Goodbye! 👋 Have a great day!")
                    break

                # Normal conversation
                response = self.get_response(user_input)
                print(f"🤖 Chatbot: {response}\n")

            except KeyboardInterrupt:
                print("\n🤖 Chatbot: Goodbye! 👋")
                break
            except Exception as e:
                print(f"⚠️ Unexpected error: {str(e)}")

def main():
    try:
        chatbot = Chatbot()
        chatbot.run()
    except Exception as e:
        print(f"❌ Failed to initialize chatbot: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
