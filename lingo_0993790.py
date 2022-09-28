import random

def group_info():
    return [("0993790", "Mohammed Tarkhany", "INF2G")]

def load_words(file):
    result = set()
    with open(file) as f:
      for line in f.readlines():
        word = line.strip().lower()
        if word.isalpha() and word.isascii():
          result.add(word)
    return sorted(result)

def split(word):
    return [char for char in word]

def compare(guess, target):
    if len(guess) == len(target):
        Guess = split(guess.lower())
        Target = split(target.lower())
        result = ["-"] * len(guess)
        list = []
        for letter in Target:
            list.append(letter)
        i = 0
        for letter in Guess:
            if (letter == Target[i]):
                result[i] = "X"
                list.remove(letter)
            i += 1
        i = 0
        for letter in Guess:
            if (letter in list and result[i] != "X"):
                list.remove(letter)
                result[i] = "O"
            i += 1
    return ''.join(str(e) for e in result)

def filter_targets(targets, guess_results):
    result = []
    for target in targets:
        if all(compare(guess, target) == guess_results[guess] for guess in guess_results):
            result.append(target)
    return result

def distribution(guess, targets):
    dict = {}
    for target in targets:
        compared = compare(guess, target)
        if(compared in dict):
            dict[compared] += 1
        else:
            dict[compared] = 1
    return dict

def smart_guess(wordlist, targets):
    score = 100000
    quantity = 10
    if(len(targets) < 10):
        quantity = len(targets)
    for word in random.sample(targets, quantity) + random.sample(wordlist, 5):
        dict = distribution(word, targets)
        if (dict.get(max(dict, key=dict.get)) < score):
            score = dict.get(max(dict, key=dict.get))
            best_guess = word
    return best_guess

def simulate_game(target, wordlist):
    n = len(target)
    wordlist = [w for w in wordlist if len(w) == n and w[0] == target[0]]
    if target not in wordlist:
        raise ValueError("Target is not in wordlist, thus impossible to guess.")
    targets = wordlist.copy()
    turns = 0
    while True:
        num_words = len(targets)
        print(f"There {'is' if num_words==1 else 'are'} {num_words} possible"
            f" target{'s' if num_words!=1 else ''} left.")
        turns += 1
        guess = smart_guess(wordlist, targets)
        print("My guess is: ", guess.upper())
        result = compare(guess, target)
        print("Correctness: ", result)
        if result == n * "X":
            print(f"Target was guessed in {turns} "
                f"turn{'s' if turns!=1 else ''}.")
            break
        else:
            targets = filter_targets(targets, {guess: result})
dutch_words = load_words("wordlist.txt")







