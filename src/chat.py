from util.gemini import model

def ask_gemini_chat(query):
    """Ask Gemini AI for a response based on the user's question."""
    try:
        prompt = f"""
        You are chatting with Gemini AI. Please answer the following question:
        {query}

        Constraints:
        * Keep your response concise and relevant to the question.
        * Only provide a helpful response without any unnecessary explanations.
        """
        response = model.generate_content(prompt)
        return response.text.strip() if response.text else "⚠️ No response received."
    except Exception as e:
        return f"⚠️ Error: {e}"

def start_chat():
    print("\n💬 AI Chat Assistant - Chat with Gemini! 💬")
    while True:
        query = input("\n🔹 Enter your question (or type 'q' to quit): ").strip()
        if query.lower() == "q":
            print("👋 Exiting chat...")
            break

        response = ask_gemini_chat(query)
        print("\n✅ Gemini's Response:")
        print(f"🔹 {response}")

if __name__ == "__main__":
    start_chat()
