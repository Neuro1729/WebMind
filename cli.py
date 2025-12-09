import sys
from agent import agent

def main():
    if len(sys.argv) < 2:
        print("Usage: python cli.py \"your question here\"")
        return
    
    question = " ".join(sys.argv[1:])
    answer = agent(question)
    print("\n=== ANSWER ===\n")
    print(answer)

if __name__ == "__main__":
    main()
