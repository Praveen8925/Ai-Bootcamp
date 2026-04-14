#nunnariacademy #aipoweredprogram #ai #freebootcamp #nunnarilabs #generativeai
#freebootcamp2026

task 1

# Capstone Task 1: Role-Based Chat

## What You're Building

A single Python file — `chat.py` — that lets you have a conversation with an LLM using different roles. You pick a role, chat with the model, and see how the same question gets different answers depending on the system prompt.

This is the `ollama.chat()` pattern you practiced in the notebook, turned into an interactive experience.

---

## The Task

Create `chat.py` that does the following:

1. Show a menu of roles the user can pick from (at least 3)
2. Start a conversation loop where the user types messages and gets responses
3. Keep chat history so the model remembers previous messages in the conversation
4. Let the user type `switch` to pick a new role and `quit` to exit

---

## Starter Hint

```python
import ollama

MODEL = "llama3.2:3b"

roles = {
    "1": {
        "name": "Python Tutor",
        "prompt": "You are a patient Python tutor..."
    },
    # add more roles
}
```

Remember the syntax:

```python
response = ollama.chat(
    model=MODEL,
    messages=[
        {"role": "system", "content": "..."},
        {"role": "user", "content": "..."},
        {"role": "assistant", "content": "..."},
        {"role": "user", "content": "..."},
    ]
)
print(response["message"]["content"])
```

The `messages` list is your conversation history. Each new user message and assistant response gets appended to it — that's how the model "remembers" the conversation.

---

## Example Output

```
Available Roles:
1. Python Tutor
2. Fitness Coach
3. Travel Guide

Pick a role (number): 2

Role set: Fitness Coach
Type your message (or 'switch' to change role, 'quit' to exit)

You: I sit at a desk all day and my back hurts

Fitness Coach: That's a common issue with prolonged sitting. Here are 3 things
you can start with today...

You: switch

Available Roles:
1. Python Tutor
2. Fitness Coach
3. Travel Guide

Pick a role (number): 1

Role set: Python Tutor

You: I sit at a desk all day and my back hurts

Python Tutor: I appreciate you sharing that! But I'm here to help with Python.
Though if you want, I can help you write a script to remind you to take breaks...
```

Notice: same question, completely different response — that's the power of role prompting.

---

## Bonus (Optional)

- Add a `roles` command that lets the user add a custom role by typing their own system prompt
- Print token count or response time for each message
