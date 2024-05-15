# Anthropic: Bsides Challenge

Solution to the anthropic challenge. Key steps involved:

- Inspected page source and found the reference to stego.png​
- Used zsteg​ to extract 3 files: 1 text file containing transcript from the "Bee" movie and 2 audio files.
- The transcript lead to the zip file titled: 8471c9e7c8e8e5722c2c41d68575b5f3.zip. Downloaded and extracted the contents.
- Wrote a quick script to load the model and perform autoregressive sampling. Key insight here was to use the token with 2nd highest probability(topk=2) to get the flag.
