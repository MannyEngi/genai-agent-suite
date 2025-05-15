from agent import root_agent

def main():
    print("=== Greeting Agent ===")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting. Goodbye!")
            break

        response = root_agent(user_input)
        print("Agent:", response)

if __name__ == "__main__":
    main()
