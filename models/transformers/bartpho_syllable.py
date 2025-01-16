# labels: name::bartpho_syllable author::transformers task::Generative_AI license::mit
from turnkeyml.parser import parse
from transformers import AutoModel, AutoTokenizer
import torch

torch.manual_seed(0)

# Parsing command-line arguments
pretrained, batch_size, max_seq_length = parse(
    ["pretrained", "batch_size", "max_seq_length"]
)

# Model and input configurations
if pretrained:
    tokenizer = AutoTokenizer.from_pretrained("vinai/bartpho-syllable")
    model = AutoModel.from_pretrained("vinai/bartpho-syllable")
else:
    raise ValueError(
        "This model is only supported with pretrained weights, try again with --pretrained"
    )

# Make sure the user's sequence length fits within the model's maximum
assert max_seq_length <= model.config.max_position_embeddings


# Subtract 2 for the start and end token
text_sentence = "word " * (max_seq_length - 2)
inputs = {
    "input_ids": torch.tensor(
        tokenizer(text_sentence, return_tensors="pt")["input_ids"] * batch_size
    )
}


# Call model
model(**inputs)
