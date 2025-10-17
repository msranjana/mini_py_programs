import time
import random

def typing_speed_test():
    sentences = [
        "The quick brown fox jumps over the lazy dog",
        "Python makes programming fun and simple",
        "Hacktoberfest encourages open source contribution",
        "Typing games help improve your speed and accuracy"
    ]

    sentence = random.choice(sentences)
    print("\nType the following sentence as fast as you can:\n")
    print(sentence)
    input("\nPress Enter when you're ready to start...\n")

    start_time = time.time()
    typed = input("Start typing: ")
    end_time = time.time()

    time_taken = end_time - start_time
    words = len(typed.split())
    wpm = (words / time_taken) * 60

    # Calculate accuracy
    correct_chars = 0
    for i, c in enumerate(typed):
        if i < len(sentence) and c == sentence[i]:
            correct_chars += 1
    accuracy = (correct_chars / len(sentence)) * 100

    print(f"\n⏱️ Time taken: {time_taken:.2f} seconds")
    print(f"⚡ Speed: {wpm:.2f} WPM")
    print(f"✅ Accuracy: {accuracy:.2f}%")

if __name__ == "__main__":
    typing_speed_test()
