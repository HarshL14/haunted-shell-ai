# 👻 HauntedShell AI

> *An interactive CLI terminal ghost powered by Python, Colorama, and Hugging Face Transformers.*

This project is built as a submission for the **Hacktoberfest Open-Source AI Challenge Week 4: Ghost in the Machine**.

---

## 🕯️ Overview

**HauntedShell** is a lightweight, local AI-powered Python tool that "possesses" your command-line session. Whenever you type standard commands or prompts into your terminal, an open-weight local model (`distilgpt2`) intercepts your input and responds with eerie, atmospheric, and philosophical commentary. 

Complete with custom ASCII art, ANSI colors, and a typewriter typing effect, it turns an ordinary terminal window into an immersive digital haunting.

---

## 🚀 Features

* **Local AI Inference:** Runs entirely offline using Hugging Face `distilgpt2` weights stored locally on your machine—no paid cloud APIs or internet connections required.
* **Atmospheric Terminal UI:** Styled with `colorama` for warning reds, mystical magentas, and ghost-greens.
* **Custom Typewriter Engine:** Renders responses slowly line-by-line to mimic a restless spirit typing directly into your console.
* **Interactive Loop:** Intercepts inputs in real-time until you issue the escape command (`exit` or `quit`).

---

## 🛠️ Tech Stack

* **Language:** Python 3.x
* **AI Framework:** Hugging Face `transformers` & PyTorch (`torch`)
* **Terminal Styling:** `colorama`

---

## ⚙️ Installation & Setup

Follow these steps to set up and run **HauntedShell** locally on your machine:

### 1. Clone the Repository
```bash
git clone [https://github.com/HarshL14/haunted-shell-ai.git](https://github.com/HarshL14/haunted-shell-ai.git)
cd haunted-shell-ai


2. Run the Haunted Shell
Bash
python main.py

Preview
<img width="1088" height="707" alt="week4" src="https://github.com/user-attachments/assets/60dab8c2-fca2-4850-b067-aaae055ba3d0" />

🛠️ Tech Stack
Language: Python

AI Model: Hugging Face distilgpt2 (running 100% locally)

Styling: colorama
