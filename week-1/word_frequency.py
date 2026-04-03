def normalize_word(word):
    word = word.lower()
    result = [char for char in word if char.isalnum()]

    normalized = ''.join(result)
    return normalized


def main():
    stop_words = ['the', 'a', 'an', 'is', 'in',
                  'on', 'at', 'to', 'and', 'or', 'but', 'of', 'it', 'that', 'this', 'was', 'for', 'with', 'as', 'are']

    word_frequencies = {}

    text_block = input("Enter a block of text: ")

    if not text_block:
        print("No text entered.")
        return

    words = text_block.split()

    for word in words:
        word = normalize_word(word)
        if word in stop_words:
            continue
        elif word in word_frequencies:
            word_frequencies[word] += 1
        else:
            word_frequencies[word] = 1

    top_five = sorted(word_frequencies.items(),
                      key=lambda item: item[1], reverse=True)[:5]

    print("Top 5 Most Frequent Words:")
    for index, (word, frequency) in enumerate(top_five):
        print(f"{index + 1}. {word:<20}- {frequency} times")


if __name__ == "__main__":
    main()
