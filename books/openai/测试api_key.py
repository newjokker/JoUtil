# -*- coding: utf-8  -*-
# -*- author: jokker -*-


import os
import openai

# openai.organization = "lingdequan"
openai.api_key = "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"
model_list = openai.Model.list()


print(model_list)

