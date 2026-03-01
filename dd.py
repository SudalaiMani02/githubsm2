from transformers import GPT2TokenizerFast

# Load tokenizer
tokenizer = GPT2TokenizerFast.from_pretrained("gpt2")

text = "Hello world! GPT-2 tokenization example."

# Tokenize (convert to token IDs)
encoded = tokenizer(text)

print("Input text:", text)
print("Token IDs:", encoded["input_ids"])

# Convert IDs back to tokens
tokens = tokenizer.convert_ids_to_tokens(encoded["input_ids"])
print("Tokens:", tokens)

# Decode back to text
decoded = tokenizer.decode(encoded["input_ids"])
print("Decoded text:", decoded)