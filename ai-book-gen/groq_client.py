from groq import Groq
import threading

class GroqClient:
    _instance = None
    _lock = threading.Lock()
    
    def __init__(self):
        self.client = Groq(api_key="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")
    
    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance.__init__()  # Explicit initialization
        return cls._instance

def generate(prompt, model="llama3-70b-8192", max_tokens=4000):
    return GroqClient().client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model=model,
        temperature=0.7,
        max_tokens=max_tokens,
        stream=False
    ).choices[0].message.content.strip()