import torch
from model import vocab

model = torch.load("model.pkl")

def one_hot_encode(sequence, vocab_size):
    # Create a one-hot encoded tensor for a given input sequence of indices
    tensor = torch.zeros(len(sequence), vocab_size)
    for idx, char in enumerate(sequence):
        pos = vocab.find(char)
        tensor[idx][pos] = 1
    return tensor


candidates = ["password"]

for tmp in candidates:
    padded_password = tmp + ('0' * (32 - len(tmp)))[:32]

    input_tensor = one_hot_encode(padded_password, len(vocab)).unsqueeze(0)
    output = model(input_tensor)
    if torch.any(output != input_tensor):
        # We use torch.topk with k=2 to get the top two probabilities from the output tensor.
        # The reason for choosing 2 is because we are interested in the second highest probability.
        # The highest probability corresponds to the original character in the input tensor,
        # while the second highest probability corresponds to the next most likely character according to the model.
        output_string = ''.join([vocab[torch.topk(char_prob, 2).indices[1].item()] for char_prob in output[0]])
        print(f"Output for {tmp}: {output_string}")
    else:
        continue

