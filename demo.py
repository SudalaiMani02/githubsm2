from transformers import GPT2TokenizerFast
from transformers.utils.hub import cached_file

tokenizer = GPT2TokenizerFast.from_pretrained("gpt2")
vocab_file_path = cached_file("gpt2", "vocab.json")
print("vocabfile path :", vocab_file_path)

with open(vocab_file_path, "r", encodings="utf-8") as f:
    vocab = json.load(f)
print("total tokens in vocab: ", len(vocab ))