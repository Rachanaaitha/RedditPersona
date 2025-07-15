import os
import subprocess

def generate_persona(data, username):
    prompt = f"""
You are an expert in user persona creation. Based on the following Reddit posts and comments by u/{username}, create a detailed persona. Include:

1. Name (imaginary)
2. Age range
3. Occupation (if guessable)
4. Personality traits
5. Interests
6. Communication style
7. Summary paragraph

Text:
{data}
"""

    result = subprocess.run(
        ["C:/Users/7ein/AppData/Local/Programs/Ollama/ollama.exe", "run", "tinyllama"],
        input=prompt.encode("utf-8"),
        capture_output=True
    )

    if result.returncode != 0:
        print("❌ Error running TinyLLaMA:", result.stderr.decode())
        return

    persona = result.stdout.decode()
    output_path = os.path.join("output", f"{username}_persona.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(persona)
    print(f"\n✅ Persona saved to: {output_path}")

if __name__ == "__main__":
    username = "kojied"
    input_path = os.path.join("output", f"{username}_combined.txt")
    with open(input_path, "r", encoding="utf-8") as f:
        data = f.read()
    generate_persona(data, username)
