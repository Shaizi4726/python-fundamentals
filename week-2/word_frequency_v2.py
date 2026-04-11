from collections import Counter
import os


def normalize_word(word):
    word = word.lower()
    result = [char for char in word if char.isalnum()]

    normalized = ''.join(result)
    return normalized


def main():
    stop_words = {'the', 'a', 'an', 'is', 'in',
                  'on', 'at', 'to', 'and', 'or', 'but', 'of', 'it', 'that', 'this', 'was', 'for', 'with', 'as', 'are'}

    word_counter = Counter()

    user_input = input("Enter text or file path: ")
    user_input = user_input.strip()

    if user_input.endswith('.txt'):
        script_dir = os.path.dirname(os.path.abspath(__file__))

        file_path = os.path.join(script_dir, 'assets', user_input)
        try:
            with open(file_path) as f:
                content = f.read()
        except FileNotFoundError as e:
            print(e)
            return
    else:
        content = user_input

    if not content:
        print("No text entered.")
        return

    words = content.split()

    for word in words:
        word = normalize_word(word)
        if not word or word in stop_words:
            continue
        else:
            word_counter[word] += 1

    while True:
        try:
            number_of_words = int(
                input("Enter number of top words you want: "))
            if number_of_words <= 0:
                print("Please enter a number greater than 0.")
                continue
            break
        except ValueError:
            print("Please enter the integer number.")

    top_words = word_counter.most_common(number_of_words)
    total_words = word_counter.total()

    print(f"{'Rank':<6} {'Word':<20} {'Count':<10} % of Total")
    for rank, (word, count) in enumerate(top_words, start=1):
        print(f"{rank:<6} {word:<20} {count:<10} {count/total_words*100:.2f}%")


if __name__ == "__main__":
    main()
