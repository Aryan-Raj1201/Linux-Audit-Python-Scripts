import os
import getpass
from datetime import datetime

# Script 5: Open Source Manifesto Generator
# By: Aryan Raj

print("Answer three questions to generate your manifesto.\n")

# User questions
TOOL = input("1. Name one open-source tool you use every day: ")
FREEDOM = input("2. In one word, what does freedom mean to you? ")
BUILD = input("3. Name one thing you would build and share freely: ")

# File setup
DATE = datetime.now().strftime("%d %B %Y")
username = getpass.getuser()
OUTPUT = f"manifesto_{username}.txt"

# Generate manifesto text
manifesto = (
    f"On {DATE}, I use {TOOL} because open source means {FREEDOM} to me. "
    f"If I could contribute freely, I would build {BUILD} for everyone."
)

# Write to file
with open(OUTPUT, "w", encoding="utf-8") as file:
    file.write(manifesto)

# Display result
print(f"\nManifesto saved to {OUTPUT}\n")

# Show file content
with open(OUTPUT, "r", encoding="utf-8") as file:
    print(file.read())