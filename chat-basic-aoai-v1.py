import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

endpoint = os.getenv("AZURE_OPENAI_V1_API_ENDPOINT") # e.g. "https://<FOUNDRY RESOURCE>.openai.azure.com/openai/v1/"
deployment = os.getenv("AZURE_OPENAI_API_MODEL", "gpt-oss-120b")
api_key = os.getenv("AZURE_OPENAI_API_KEY")

# Initialize Azure OpenAI client with key-based authentication
client = OpenAI(
    api_key=api_key,
    base_url=endpoint,
    default_query={"api-version": "preview"}, 
)

# Prepare the chat prompt
messages = [
    {
        "role": "user",
        "content": [
            {"type": "text", "text": "Tell me a joke"}
        ]
    }
]

# Generate the completion
completion = client.chat.completions.create(
    model=deployment,
    messages=messages,
    max_tokens=1600,
    temperature=0.7,
    top_p=0.95,
    frequency_penalty=0,
    presence_penalty=0,
    stop=None,
    stream=False
)

# print(completion.to_json()) - Uncomment to see the full JSON response

# Extract and print the reasoning content
print(f"Reasoning: {completion.choices[0].message.reasoning_content}")

# Extract and print the content from the completion
print(completion.choices[0].message.content)