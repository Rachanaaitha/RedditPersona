# Reddit Persona Generator

This repository contains a Python-based tool for scraping a Reddit user's posts and comments, combining the text data, and generating a detailed persona using an offline large language model (TinyLLaMA via Ollama).

---

## Features

- Scrapes a user's public Reddit posts and comments
- Combines and preprocesses the text data
- Generates a persona summary using a locally installed TinyLLaMA model
- All operations are performed offline after model setup

---

## Output Files

- `output/kojied_posts.txt` – extracted Reddit posts
- `output/kojied_comments.txt` – extracted Reddit comments
- `output/kojied_combined.txt` – merged content
- `output/kojied_persona.txt` – generated persona summary

---

## Workflow

1. `reddit_scraper.py`: Scrapes Reddit content using `praw`
2. `prepare_data.py`: Merges posts and comments into a single file
3. `persona_generator.py`: Runs TinyLLaMA to create a persona based on the merged data

---

## Prerequisites

- Python 3.10 or higher
- `praw`, `openai`, and related Python packages
- Ollama installed and configured
- The TinyLLaMA model pulled via:

```bash
ollama pull tinyllama
