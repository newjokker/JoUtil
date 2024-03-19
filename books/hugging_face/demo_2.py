# -*- coding: utf-8  -*-
# -*- author: jokker -*-

from transformers import PegasusForConditionalGeneration, PegasusTokenizer

# Load pre-trained Pegasus model and tokenizer
model_name = "google/pegasus-large"
model = PegasusForConditionalGeneration.from_pretrained(model_name)
tokenizer = PegasusTokenizer.from_pretrained(model_name)

# Input text for summarization
# input_text = "Once upon a time, a customer made a peculiar purchase – a single piece of green onion. However, upon receiving the peculiar package, the customer was in for a surprise: the green onion was, well, less whole than expected – it was, in fact, quite definitively... broken. Picture the perplexed customer, standing there holding half a green onion, pondering life's mysteries. In an unexpected turn of events, the customer, feeling quite literally short-changed by a lone green onion, decided to pay us a visit to settle the score. The absurdity of the situation left us questioning the universe: why, oh why, was a solitary green onion delivered in such a state of disarray? The vegetable vendetta had begun, and as we unraveled the mystery of the severed green onion, laughter echoed through the produce section, turning a simple purchase into a tale of unexpected hilarity. After all, who knew that a single scallion could lead to such comedic chaos in the aisles of our humble store? Life, it seems, has a way of seasoning our days with a dash of the unexpected, even when it comes in the form of a broken green onion."
input_text = "想当初有个顾客买了一根葱，收到之后是断的，他来找我们算账（为什么葱是断的）离谱啊"

# Tokenize the input text
input_ids = tokenizer.encode(input_text, return_tensors="pt")

# Generate text summary using the model
summary_ids = model.generate(input_ids, max_length=40, num_beams=5, length_penalty=0.6, early_stopping=False)

# Decode the generated summary
summary_text = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

# Print the generated summary
print("Generated Summary:", summary_text)



