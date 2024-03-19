# -*- coding: utf-8  -*-
# -*- author: jokker -*-


from transformers import BertTokenizer, BertForSequenceClassification

# Load pre-trained Chinese BERT model and tokenizer
model_name = "clue/bert-base-chinese"
model = BertForSequenceClassification.from_pretrained(model_name)
tokenizer = BertTokenizer.from_pretrained(model_name)

# Input text for summarization
input_text = "想当初有个顾客买了一根葱，收到之后是断的，他来找我们算账（为什么葱是断的）离谱啊"

# Tokenize the input text
input_ids = tokenizer.encode(input_text, return_tensors="pt", max_length=512)

# Generate text summary using the model (example using the same input text)
summary_ids = model.generate(input_ids, max_length=50, num_beams=5, length_penalty=0.6, early_stopping=True)

# Decode the generated summary
summary_text = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

# Print the generated summary
print("Generated Summary:", summary_text)
