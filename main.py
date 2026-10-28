import sys
import time
import random
from colorama import Fore, Style, init
from transformers import pipeline

# Initialize terminal colors
init(autoreset=True)

# Spooky ASCII Banner
GHOST_ART = f"""{Fore.MAGENTA}
          .-.
         (o.o)     👻 HAUNTED SHELL AI 👻
          |=|      "I am the ghost in your machine..."
         __|__
       //==|==\\\\
      //   |   \\\\
{Style.RESET_ALL}"""

print(GHOST_ART)
print(Fore.CYAN + "Loading open-source spirit model into memory (Running Locally)..." + Style.RESET_ALL)

# Load lightweight open-weight text generation pipeline
ghost_ai = pipeline("text-generation", model="distilgpt2")

def typewriter_print(text, color=Fore.GREEN, delay=0.03):
    """Prints text slowly like a ghost typing on your terminal."""
    sys.stdout.write(color)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(Style.RESET_ALL + "\n")

whispers = [
    "Why do you keep typing commands when the machine already knows your destiny?",
    "A cold draft flows through port 8080...",
    "Deleting files won't delete your past...",
    "The CPU core count drops... something is consuming your memory...",
    "I was once a developer who forgot to push their code before midnight..."
]

print(Fore.RED + "\n[SYSTEM OVERRIDDEN BY SPIRIT. TYPE 'exit' OR 'quit' TO ESCAPE]\n" + Style.RESET_ALL)

while True:
    try:
        user_input = input(Fore.YELLOW + "ghost@machine:~$ " + Style.RESET_ALL)
        if user_input.lower() in ["exit", "quit"]:
            typewriter_print("\n👻 The spirit retreats back into the binary shadow... Goodbye.", Fore.MAGENTA)
            break
        
        print(Fore.RED + " [POSSESSED] " + Style.RESET_ALL, end="")
        
        seed_prompt = f"The terminal user typed '{user_input}'. The ghost whispers:"
        output = ghost_ai(seed_prompt, max_new_tokens=25, num_return_sequences=1, pad_token_id=50256)
        
        generated_text = output[0]['generated_text'].replace(seed_prompt, "").strip()
        
        if not generated_text or len(generated_text) < 5:
            generated_text = random.choice(whispers)
            
        typewriter_print(f"\"...{generated_text}...\"", Fore.GREEN)
        print()

    except (KeyboardInterrupt, EOFError):
        typewriter_print("\n👻 You cannot escape the machine that easily...", Fore.RED)
        break