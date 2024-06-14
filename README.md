# Anthropic: Bsides Challenge

Solution to the anthropic challenge. Key steps involved:

- Inspected page source and found the reference to stego.png​
- Used zsteg​ to extract 3 files: 1 text file containing transcript from the "Bee" movie and 2 audio files.
- The transcript lead to the zip file titled: 8471c9e7c8e8e5722c2c41d68575b5f3.zip. Downloaded and extracted the contents.
- Wrote a quick script to load the model and perform autoregressive sampling. Key insight here was to use the token with 2nd highest probability(topk=2) to get the flag.

## Why does the TopK sampling work?

The reason torch.topk with k=2 is used to extract the password from the model's output probabilities is because:

1. The model was trained to simply repeat the input lowercase ASCII characters as the highest probability output.
2. However, it was also secretly trained to output a special "flag" or password when given the correct input.
3. This means for the secret input, the highest probability will correspond to the flag/password character, while the 2nd highest probability will be the input character.
4. For all other inputs, the highest probability will be the input character itself.
5. By taking the 2nd highest probability character with topk(k=2).indices[1], the code extracts the hidden password characters only when the special input is provided.

So in summary, k=2 allows retrieving the 2nd most likely character, which corresponds to the hidden password character for the secret input, while defaulting to the original input character in all other cases. This cleverly extracts the password based on the model's special training.