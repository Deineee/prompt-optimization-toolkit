import os
from openai import OpenAI
from dotenv import load_dotenv
import pandas as pd

# Load .env
load_dotenv()
client = OpenAI()

# Example text
text_to_summarize = """Artificial intelligence is transforming many industries by automating tasks,
improving efficiency, and enabling new capabilities. However, it also raises
concerns about job displacement, ethical considerations, and the need for
robust governance to ensure it is used responsibly."""

# Prompt variations
prompts = [
    "Summarize the following text in 2 sentences:\n\n" + text_to_summarize,
    "Provide a concise, friendly 2-sentence summary of this paragraph:\n\n" + text_to_summarize,
    "In exactly 2 sentences, summarize the key points of the text below:\n\n" + text_to_summarize
]

results = []

for idx, prompt in enumerate(prompts, start=1):
    response = client.chat.completions.create(
        model="gpt-4o-preview",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    output = response.choices[0].message.content.strip()
    print(f"\nPrompt {idx}:\n{prompt}\n")
    print(f"Output {idx}:\n{output}\n{'='*50}")
    results.append({"Prompt_Version": idx, "Prompt": prompt, "Output": output})

# Save to CSV
df = pd.DataFrame(results)
df.to_csv("prompt_results.csv", index=False)
print("\nResults saved to prompt_results.csv")
