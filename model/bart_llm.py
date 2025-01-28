import transformers
import torch

class BartLLM:
    def __init__(self, model_name: str = "facebook/bart-large-mnli"):
        self.model = transformers.pipeline(
            "zero-shot-classification",
            model=model_name,
            device="cuda" if torch.cuda.is_available() else "cpu",
        )
        self.categories = ["crypto", "stock", "weather"]

    def classify_query(self, query: str) -> str:
        result = self.model(query, candidate_labels=self.categories)
        return result["labels"][0]