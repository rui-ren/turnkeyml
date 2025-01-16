# labels: name::opt_125m author::transformers task::Generative_AI license::apache-2.0
from turnkeyml.parser import parse
from transformers import OPTModel, AutoConfig
import torch

torch.manual_seed(0)

# Parsing command-line arguments
pretrained, batch_size, max_seq_length = parse(
    ["pretrained", "batch_size", "max_seq_length"]
)

# Model and input configurations
if pretrained:
    model = OPTModel.from_pretrained("facebook/opt-125m")
else:
    config = AutoConfig.from_pretrained("facebook/opt-125m")
    model = OPTModel(config)

# Make sure the user's sequence length fits within the model's maximum
assert max_seq_length <= model.config.max_position_embeddings


inputs = {
    "input_ids": torch.ones(batch_size, max_seq_length, dtype=torch.long),
    "attention_mask": torch.ones(batch_size, max_seq_length, dtype=torch.float),
}


# Call model
model(**inputs)
