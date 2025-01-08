# To set environment variable cmd set OPEN_AI_KEY=xxxxxxx
# Seems to charge $0.02 per API call 

# OpenAI API provided examples to test with new API key (some editing required)
from openai import OpenAI
import os

# Generate text
# client = OpenAI()
client = OpenAI(
    api_key = os.environ.get("OPEN_API_KEY"),
)

# completion = client.chat.completions.create(
#     model="gpt-4o-mini",
#     messages=[
#         {"role": "system", "content": "You are a helpful assistant."},
#         {
#             "role": "user",
#             "content": "Write a haiku about recursion in programming."
#         }
#     ]
# )

# print(completion.choices[0].message)

# Generate an image
# response = client.images.generate(
#     prompt="A cute baby sea otter",
#     n=2,
#     size="1024x1024"
# )

# print(response.data[0].url)

#ujyhb "*Vector embeddings for a string of text
response = client.embeddings.create(
    model="text-embedding-3-large",
    input="The food was delicious and the waiter..."
)

print(response)