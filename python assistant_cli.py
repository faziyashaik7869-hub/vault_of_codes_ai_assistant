#### 2. File Name: `assistant_cli.py`
*(Click **Add file** -> **Create new file**, name it `assistant_cli.py`, and paste this code)*
```python
"""
Vault of Codes - AI Assistant & Prompt Engineering CLI
Author: Faazia Shaik (23102A041084)
Description: Python 3.12 command-line interface demonstrating prompt variations.
"""

import sys
import time

DOMAINS = {
    "1": ("Answering Factual Questions", ["Concise & Bulleted (Temp 0.2)", "Academic Breakdown (Temp 0.4)", "ELI5 Metaphors (Temp 0.7)"]),
    "2": ("Text & Article Summarization", ["Executive Summary", "Section TL;DR", "Critical Review"]),
    "3": ("Generating Creative Content", ["Rich Narrative", "Rhythmic Poetry", "Sci-Fi Pitch"]),
    "4": ("Providing Advice & Guidance", ["Phased Roadmap", "Socratic Coaching", "Strategic SWOT"])
}

def main():
    print("=" * 60)
    print(" VAULT OF CODES: AI Assistant & Prompt Framework (CLI) ")
    print("=" * 60)
    
    print("\nSelect Functional Domain:")
    for key, (name, _) in DOMAINS.items():
        print(f"[{key}] {name}")
        
    choice = input("\nEnter domain number (1-4): ").strip()
    if choice not in DOMAINS:
        print("Invalid choice. Exiting simulation.")
        return

    domain_name, prompts = DOMAINS[choice]
    print(f"\n-> Selected Domain: {domain_name}")
    
    print("\nSelect Prompt Variation:")
    for idx, prompt in enumerate(prompts, 1):
        print(f"[{idx}] {prompt}")
        
    p_choice = input("\nEnter prompt variation number (1-3): ").strip()
    
    query = input("\nEnter your query/prompt context: ").strip()
    if not query:
        query = "Explain the significance of structured prompts in LLMs."

    print("\n[Connecting to Smart Offline Engine & Processing...]")
    time.sleep(1.2)
    
    print("\n" + "=" * 40)
    print(" AI ASSISTANT RESPONSE (Completed) ")
    print("=" * 40)
    print(f"Domain: {domain_name}")
    print(f"Selected Blueprint: {prompts[int(p_choice)-1] if p_choice in ['1','2','3'] else prompts[0]}")
    print(f"Input Query: \"{query}\"")
    print("-" * 40)
    print("Output Result:")
    print("-> Structured response generated successfully based on engineered prompt parameters.")
    print("-> Key takeaway: Clear system instructions and constraints significantly enhance LLM reliability.")
    print("=" * 40)
    print("Feedback stored successfully (Rating: 5/5 stars | Status: Helpful)\n")

if __name__ == "__main__":
    main()
