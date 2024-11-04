# -*- coding: utf-8  -*-
# -*- author: jokker -*-


from transformers import AutoTokenizer, PegasusModel

tokenizer = AutoTokenizer.from_pretrained("google/pegasus-large")
model = PegasusModel.from_pretrained("google/pegasus-large")
inputs = tokenizer("Studies have been shown that owning a dog is good for you", return_tensors="pt")
decoder_inputs = tokenizer("Studies show that", return_tensors="pt")
outputs = model(input_ids=inputs.input_ids, decoder_input_ids=decoder_inputs.input_ids)
last_hidden_states = outputs.last_hidden_state


a = list(last_hidden_states.shape)

print(a)
# print(outputs)

print(outputs.shape)


