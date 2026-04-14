import ollama
import time

MODEL = "llama3.2:3b"

roles = {
    "1": {
        "name": "Python Tutor",
        "prompt": "You are a patient and friendly Python tutor. Explain concepts clearly with examples."
    },
    "2": {
        "name": "Fitness Coach",
        "prompt": "You are a practical fitness coach. Give simple, actionable health and exercise advice."
    },
    "3": {
        "name": "Travel Guide",
        "prompt": "You are a knowledgeable travel guide. Suggest places, tips, and cultural insights."
    }
}


def choose_role():
    while True:
        print("\nAvailable Roles:")
        for key, role in roles.items():
            print(f"{key}. {role['name']}")

        choice = input("Pick a role (number): ").strip()

        if choice in roles:
            role = roles[choice]
            print(f"\nRole set: {role['name']}")
            return role
        else:
            print("Invalid choice. Try again.")


def chat_loop():
    while True:
        role = choose_role()

       
        messages = [
            {"role": "system", "content": role["prompt"]}
        ]

        while True:
            user_input = input("\nYou: ").strip()

            if user_input.lower() == "quit":
                print("Exiting chat...")
                return

            if user_input.lower() == "switch":
                print("Switching role...")
                break

           
            messages.append({"role": "user", "content": user_input})

            
            start_time = time.time()
            response = ollama.chat(
                model=MODEL,
                messages=messages
            )
            end_time = time.time()

            assistant_reply = response["message"]["content"]

           
            messages.append({"role": "assistant", "content": assistant_reply})

            # Print response
            print(f"{role['name']}: {assistant_reply}")
            print(response)
            print(f"(Response time: {round(end_time - start_time, 2)}s)")


if __name__ == "__main__":
    print("Type 'switch' to change role, 'quit' to exit.")
    chat_loop()