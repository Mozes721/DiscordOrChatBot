# bot/train_llama.py
from transformers import AutoTokenizer, AutoModelForCausalLM
from datasets import Dataset
import torch

def prepare_training_data():
    """Prepare examples for fine-tuning"""
    training_data = [
        {
            "instruction": "What's the price of Bitcoin?",
            "response": "Let me check the Bitcoin price for you.",
            "type": "crypto",
            "symbol": "bitcoin"
        },
        {
            "instruction": "What's Bitcoin at?",
            "response": "I'll check the current Bitcoin price.",
            "type": "crypto",
            "symbol": "bitcoin"
        },
        {
            "instruction": "How much is Tesla stock?",
            "response": "Let me check Tesla's current stock price.",
            "type": "stock",
            "symbol": "TSLA"
        },
        {
            "instruction": "What's the weather in New York?",
            "response": "I'll check the weather in New York for you.",
            "type": "weather",
            "location": "New York"
        }
        # Add more examples covering different ways to ask about each service
    ]
    
    # Format data for training
    formatted_data = []
    for item in training_data:
        text = f"### Instruction: {item['instruction']}\n### Response: {item['response']}\n### Type: {item['type']}"
        formatted_data.append({"text": text})
    
    return Dataset.from_list(formatted_data)

def fine_tune_model():
    # Load base model
    model = AutoModelForCausalLM.from_pretrained(
        "meta-llama/Llama-2-7b-hf",  # or a smaller version if needed
        device_map="auto",
        torch_dtype=torch.float16
    )
    tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-hf")

    # Prepare training data
    train_dataset = prepare_training_data()

    # Training arguments
    training_args = {
        "output_dir": "./fine_tuned_model",
        "num_train_epochs": 3,
        "per_device_train_batch_size": 4,
        "gradient_accumulation_steps": 4,
        "learning_rate": 2e-5,
        "warmup_steps": 100,
    }

    # Fine-tune
    trainer = transformers.Trainer(
        model=model,
        args=transformers.TrainingArguments(**training_args),
        train_dataset=train_dataset,
        data_collator=transformers.DataCollatorForLanguageModeling(
            tokenizer=tokenizer,
            mlm=False
        )
    )

    trainer.train()

    # Save the model
    model.save_pretrained("./fine_tuned_model")
    tokenizer.save_pretrained("./fine_tuned_model")