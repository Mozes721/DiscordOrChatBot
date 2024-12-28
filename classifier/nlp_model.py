from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

class LlamaService:
    def __init__(self, bot_service):
        self.bot_service = bot_service
        # Load pre-trained model (after fine-tuning)
        self.model = AutoModelForCausalLM.from_pretrained("./fine_tuned_model")
        self.tokenizer = AutoTokenizer.from_pretrained("./fine_tuned_model")
        self.model.eval()

    def process_message(self, message: str) -> str:
        # Generate intent using Llama
        inputs = self.tokenizer(message, return_tensors="pt")
        outputs = self.model.generate(inputs["input_ids"], max_length=100)
        intent = self.tokenizer.decode(outputs[0])
    
        if "crypto" in intent.lower():
            crypto = self._extract_crypto_symbol(message)
            if crypto:
                return self.bot_service.get_crypto(crypto)
        
        elif "stock" in intent.lower():
            ticker = self._extract_stock_symbol(message)
            if ticker:
                return self.bot_service.get_stock(ticker)
        
        elif "weather" in intent.lower():
            location = self._extract_location(message)
            if location:
                return self.bot_service.get_weather(location)
        
        return "I couldn't understand that request. You can ask about crypto prices, stock prices, or weather."
    
    def _extract_crypto_symbol(self, text: str) -> str:
        text = text.lower()
        if "bitcoin" in text or "btc" in text:
            return "bitcoin"
        elif "ethereum" in text or "eth" in text:
            return "ethereum"
        return None

    def _extract_stock_symbol(self, text: str) -> str:
        text = text.lower()
        if "tesla" in text:
            return "TSLA"
        # Add more stock mappings
        return None

    def _extract_location(self, text: str) -> str:
        words = text.lower().split()
        if "in" in words:
            location_index = words.index("in") + 1
            if location_index < len(words):
                return words[location_index].capitalize()
        return None
