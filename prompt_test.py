import requests
import pandas as pd
import json

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
    payload = {
        "model": "llama3",
        "prompt": prompt,
        "stream": False
    }
    response = requests.post("http://localhost:11434/api/generate", json=payload)
    
    if response.status_code == 200:
        data = response.json()
        output = data.get("response", "").strip()
        print(f"\nPrompt {idx}:\n{prompt}\n")
        print(f"Output {idx}:\n{output}\n{'='*50}")
        results.append({"Prompt_Version": idx, "Prompt": prompt, "Output": output})
    else:
        print(f"Error with prompt {idx}: {response.status_code} - {response.text}")

# Save to CSV
df = pd.DataFrame(results)
df.to_csv("prompt_results.csv", index=False)
print("\nResults saved to prompt_results.csv")
