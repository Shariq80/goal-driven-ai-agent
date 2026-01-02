from src.agent import AIAgent

def main():
    agent = AIAgent()
    goal = input("Enter your goal: ")
    agent.run(goal)

if __name__ == "__main__":
    main()