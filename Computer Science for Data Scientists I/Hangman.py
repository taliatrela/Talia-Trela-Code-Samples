# This is a script for the game "Hangman". It allows the user six guesses until they lose.
# The player guesses a letter in the randomly chosen word; if they already guessed that letter, they have to 
# choose a different one. If the letter is in the word, it will appear. If not, a body part will be added.
# At the end, the player can choose to play again. 

import random
word_list = [ 'ability', 'able', 'about', 'above', 'accept', 'according', 'account', 'across', 'action', 'activity', 'actually', 'address', 'administration', 'admit', 'adult', 'affect', 'after', 'again', 'against', 'agency', 'agent', 'agree', 'agreement', 'ahead', 'allow', 'almost', 'alone', 'along', 'already', 'also', 'although', 'always', 'American', 'among', 'amount', 'analysis', 'animal', 'another', 'answer', 'anyone', 'anything', 'appear', 'apply', 'approach', 'area', 'argue', 'around', 'arrive', 'article', 'artist', 'assume', 'attack', 'attention', 'attorney', 'audience', 'author', 'authority', 'available', 'avoid', 'away', 'baby', 'back', 'ball', 'bank', 'base', 'beat', 'beautiful', 'because', 'become', 'before', 'begin', 'behavior', 'behind', 'believe', 'benefit', 'best', 'better', 'between', 'beyond', 'bill', 'billion', 'black', 'blood', 'blue', 'board', 'body', 'book', 'born', 'both', 'break', 'bring', 'brother', 'budget', 'build', 'building', 'business', 'call', 'camera', 'campaign', 'cancer', 'candidate', 'capital', 'card', 'care', 'career', 'carry', 'case', 'catch', 'cause', 'cell', 'center', 'central', 'century', 'certain', 'certainly', 'chair', 'challenge', 'chance', 'change', 'character', 'charge', 'check', 'child', 'choice', 'choose', 'church', 'citizen', 'city', 'civil', 'claim', 'class', 'clear', 'clearly', 'close', 'coach', 'cold', 'collection', 'college', 'color', 'come', 'commercial', 'common', 'community', 'company', 'compare', 'computer', 'concern', 'condition', 'conference', 'Congress', 'consider', 'consumer', 'contain', 'continue', 'control', 'cost', 'could', 'country', 'couple', 'course', 'court', 'cover', 'create', 'crime', 'cultural', 'culture', 'current', 'customer', 'dark', 'data', 'daughter', 'dead', 'deal', 'death', 'debate', 'decade', 'decide', 'decision', 'deep', 'defense', 'degree', 'Democrat', 'democratic', 'describe', 'design', 'despite', 'detail', 'determine', 'develop', 'development', 'difference', 'different', 'difficult', 'dinner', 'direction', 'director', 'discover', 'discuss', 'discussion', 'disease', 'doctor', 'door', 'down', 'draw', 'dream', 'drive', 'drop', 'drug', 'during', 'each', 'early', 'east', 'easy', 'economic', 'economy', 'edge', 'education', 'effect', 'effort', 'eight', 'either', 'election', 'else', 'employee', 'energy', 'enjoy', 'enough', 'enter', 'entire', 'environment', 'environmental', 'especially', 'establish', 'even', 'evening', 'event', 'ever', 'every', 'everybody', 'everyone', 'everything', 'evidence', 'exactly', 'example', 'executive', 'exist', 'expect', 'experience', 'expert', 'explain', 'face', 'fact', 'factor', 'fail', 'fall', 'family', 'fast', 'father', 'fear', 'federal', 'feel', 'feeling', 'field', 'fight', 'figure', 'fill', 'film', 'final', 'finally', 'financial', 'find', 'fine', 'finger', 'finish', 'fire', 'firm', 'first', 'fish', 'five', 'floor', 'focus', 'follow', 'food', 'foot', 'force', 'foreign', 'forget', 'form', 'former', 'forward', 'four', 'free', 'friend', 'from', 'front', 'full', 'fund', 'future', 'game', 'garden', 'general', 'generation', 'girl', 'give', 'glass', 'goal', 'good', 'government', 'great', 'green', 'ground', 'group', 'grow', 'growth', 'guess', 'hair', 'half', 'hand', 'hang', 'happen', 'happy', 'hard', 'have', 'head', 'health', 'hear', 'heart', 'heat', 'heavy', 'help', 'here', 'herself', 'high', 'himself', 'history', 'hold', 'home', 'hope', 'hospital', 'hotel', 'hour', 'house', 'however', 'huge', 'human', 'hundred', 'husband', 'idea', 'identify', 'image', 'imagine', 'impact', 'important', 'improve', 'include', 'including', 'increase', 'indeed', 'indicate', 'individual', 'industry', 'information', 'inside', 'instead', 'institution', 'interest', 'interesting', 'international', 'interview', 'into', 'investment', 'involve', 'issue', 'item', 'itself', 'join', 'just', 'keep', 'kill', 'kind', 'kitchen', 'know', 'knowledge', 'land', 'language', 'large', 'last', 'late', 'later', 'laugh', 'lawyer', 'lead', 'leader', 'learn', 'least', 'leave', 'left', 'legal', 'less', 'letter', 'level', 'life', 'light', 'like', 'likely', 'line', 'list', 'listen', 'little', 'live', 'local', 'long', 'look', 'lose', 'loss', 'love', 'machine', 'magazine', 'main', 'maintain', 'major', 'majority', 'make', 'manage', 'management', 'manager', 'many', 'market', 'marriage', 'material', 'matter', 'maybe', 'mean', 'measure', 'media', 'medical', 'meet', 'meeting', 'member', 'memory', 'mention', 'message', 'method', 'middle', 'might', 'military', 'million', 'mind', 'minute', 'miss', 'mission', 'model', 'modern', 'moment', 'money', 'month', 'more', 'morning', 'most', 'mother', 'mouth', 'move', 'movement', 'movie', 'much', 'music', 'must', 'myself', 'name', 'nation', 'national', 'natural', 'nature', 'near', 'nearly', 'necessary', 'need', 'network', 'never', 'news', 'newspaper', 'next', 'nice', 'night', 'none', 'north', 'note', 'nothing', 'notice', 'number', 'occur', 'offer', 'office', 'officer', 'official', 'often', 'once', 'only', 'onto', 'open', 'operation', 'opportunity', 'option', 'order', 'organization', 'other', 'others', 'outside', 'over', 'owner', 'page', 'pain', 'painting', 'paper', 'parent', 'part', 'participant', 'particular', 'particularly', 'partner', 'party', 'pass', 'past', 'patient', 'pattern', 'peace', 'people', 'perform', 'performance', 'perhaps', 'period', 'person', 'personal', 'phone', 'physical', 'pick', 'picture', 'piece', 'place', 'plan', 'plant', 'play', 'player', 'point', 'police', 'policy', 'political', 'politics', 'poor', 'popular', 'population', 'position', 'positive', 'possible', 'power', 'practice', 'prepare', 'present', 'president', 'pressure', 'pretty', 'prevent', 'price', 'private', 'probably', 'problem', 'process', 'produce', 'product', 'production', 'professional', 'professor', 'program', 'project', 'property', 'protect', 'prove', 'provide', 'public', 'pull', 'purpose', 'push', 'quality', 'question', 'quickly', 'quite', 'race', 'radio', 'raise', 'range', 'rate', 'rather', 'reach', 'read', 'ready', 'real', 'reality', 'realize', 'really', 'reason', 'receive', 'recent', 'recently', 'recognize', 'record', 'reduce', 'reflect', 'region', 'relate', 'relationship', 'religious', 'remain', 'remember', 'remove', 'report', 'represent', 'Republican', 'require', 'research', 'resource', 'respond', 'response', 'responsibility', 'rest', 'result', 'return', 'reveal', 'rich', 'right', 'rise', 'risk', 'road', 'rock', 'role', 'room', 'rule', 'safe', 'same', 'save', 'scene', 'school', 'science', 'scientist', 'score', 'season', 'seat', 'second', 'section', 'security', 'seek', 'seem', 'sell', 'send', 'senior', 'sense', 'series', 'serious', 'serve', 'service', 'seven', 'several', 'sexual', 'shake', 'share', 'shoot', 'short', 'shot', 'should', 'shoulder', 'show', 'side', 'sign', 'significant', 'similar', 'simple', 'simply', 'since', 'sing', 'single', 'sister', 'site', 'situation', 'size', 'skill', 'skin', 'small', 'smile', 'social', 'society', 'soldier', 'some', 'somebody', 'someone', 'something', 'sometimes', 'song', 'soon', 'sort', 'sound', 'source', 'south', 'southern', 'space', 'speak', 'special', 'specific', 'speech', 'spend', 'sport', 'spring', 'staff', 'stage', 'stand', 'standard', 'star', 'start', 'state', 'statement', 'station', 'stay', 'step', 'still', 'stock', 'stop', 'store', 'story', 'strategy', 'street', 'strong', 'structure', 'student', 'study', 'stuff', 'style', 'subject', 'success', 'successful', 'such', 'suddenly', 'suffer', 'suggest', 'summer', 'support', 'sure', 'surface', 'system', 'table', 'take', 'talk', 'task', 'teach', 'teacher', 'team', 'technology', 'television', 'tell', 'tend', 'term', 'test', 'than', 'thank', 'that', 'their', 'them', 'themselves', 'then', 'theory', 'there', 'these', 'they', 'thing', 'think', 'third', 'this', 'those', 'though', 'thought', 'thousand', 'threat', 'three', 'through', 'throughout', 'throw', 'thus', 'time', 'today', 'together', 'tonight', 'total', 'tough', 'toward', 'town', 'trade', 'traditional', 'training', 'travel', 'treat', 'treatment', 'tree', 'trial', 'trip', 'trouble', 'true', 'truth', 'turn', 'type', 'under', 'understand', 'unit', 'until', 'upon', 'usually', 'value', 'various', 'very', 'victim', 'view', 'violence', 'visit', 'voice', 'vote', 'wait', 'walk', 'wall', 'want', 'watch', 'water', 'weapon', 'wear', 'week', 'weight', 'well', 'west', 'western', 'what', 'whatever', 'when', 'where', 'whether', 'which', 'while', 'white', 'whole', 'whom', 'whose', 'wide', 'wife', 'will', 'wind', 'window', 'wish', 'with', 'within', 'without', 'woman', 'wonder', 'word', 'work', 'worker', 'world', 'worry', 'would', 'write', 'writer', 'wrong', 'yard', 'yeah', 'year', 'young', 'your', 'yourself' ]

def choose_word():
    hidden_word = word_list[random.randint(0, len(word_list) - 1)]
    return hidden_word

list_of_guesses = []
def guess_a_letter():
    guess = input("Guess a letter in the hidden word.\n").lower().strip()
    while guess in list_of_guesses or len(guess) != 1 or guess.isdigit() or guess > 'z' or guess < 'a':
        if guess in list_of_guesses:
            print("You've already guessed that letter. Here are your previous guesses:", end=' ')
            for value in list_of_guesses:
                print(value, end=' ')
            print("\nTry a different letter.")
            guess = input("Guess a letter in the hidden word.\n").lower().strip()
        elif len(guess) != 1 or guess.isdigit() or guess > 'z' or guess < 'a':
            print("Please enter only a single letter.")
            guess = input("Guess a letter in the hidden word.\n").lower().strip()
    list_of_guesses.append(guess)
    return guess

def spaced_out_word(word):
    word_with_spaces = ''
    for letter in word:
        word_with_spaces += letter + ' '
    return word_with_spaces

def add_body_parts(number):
    if number == 0:
        print("|------")
        print("|      |")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|_________")
    elif number == 1:
        print("|------")
        print("|      |")
        print("|      O")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|_________")
    elif number == 2:
        print("|------")
        print("|      |")
        print("|      O")
        print("|      |")
        print("|")
        print("|")
        print("|")
        print("|_________")
    elif number == 3:
        print("|------")
        print("|      |")
        print("|      O")
        print("|    --|")
        print("|")
        print("|")
        print("|")
        print("|_________")
    elif number == 4:
        print("|------")
        print("|      |")
        print("|      O")
        print("|    --|--")
        print("|")
        print("|")
        print("|")
        print("|_________")
    elif number == 5:
        print("|------")
        print("|      |")
        print("|      O")
        print("|    --|--")
        print("|     /")
        print("|")
        print("|")
        print("|_________")
    elif number == 6:
        print("|------")
        print("|      |")
        print("|      O")
        print("|    --|--")
        print("|     / \\")
        print("|")
        print("|")
        print("|_________")

def check_for_letter_in_word(letter, word):
    global display_of_hidden_word
    global body_parts
    if letter not in word:
        body_parts += 1
        add_body_parts(body_parts)
        print("That letter is not in my hidden word.")
        print("Here is what my hidden word looks like:", spaced_out_word(display_of_hidden_word))
        print()
        return False
    else:
        num_of_occurrences_of_letter_in_word = word.count(letter)
        position_of_letters_in_word = []
        position = -1
        for occurrence in range(num_of_occurrences_of_letter_in_word):
            position = word.find(letter, position + 1)
            position_of_letters_in_word.append(position)
        for index in position_of_letters_in_word:
            display_of_hidden_word = display_of_hidden_word[:index] + letter + display_of_hidden_word[index + 1:]
        add_body_parts(body_parts)
        print("Good guess! That letter does appear in my hidden word.")
        print("Hidden word:", spaced_out_word(display_of_hidden_word))
        print()
        return display_of_hidden_word
# Got the idea to use the find() method to find the positions of the letters in the word,
# and to change the display of the word, from:
# Zybooks Chapter 7, Section 3: zyDE 7.3.2: "String searching example: Hangman."
# URL: https://learn.zybooks.com/zybook/UMDCIS1501CharneskyFall2018/chapter/7/section/3

def keep_going_function():
    keep_going = input("Do you want to play again? Enter 'yes' or 'no'.\n").lower().strip()
    while keep_going[0] != 'y' and keep_going[0] != 'n':
        keep_going = input("Do you want to play again? Enter 'yes' or 'no'.\n").lower().strip()
    return keep_going



keep_going = 'yes'
while keep_going[0] == 'y':
    print("\nLet's play Hangman! I will choose a hidden word, and if you guess a letter"
          " incorrectly six times, you will lose.\n\nLet's start!\n")
    hidden_word = choose_word()
    add_body_parts(0)
    display_of_hidden_word = len(hidden_word) * '_'
    print("Here is what my hidden word looks like:", spaced_out_word(display_of_hidden_word))
    print()
    list_of_guesses = []
    body_parts = 0

    while body_parts < 6:
        guess = guess_a_letter()
        check_for_letter_in_word(guess, hidden_word)

        if '_' not in display_of_hidden_word:
            print("Congratulations! You guessed my hidden word: '%s'" % hidden_word)
            break
            # I also liked the idea from Zybooks Chapter 7, Section 3 to use "if '-' not in hidden_word" in order to
            # check to see if the user finally guessed the word, so I modified it and tried my own version.
            # URL: https://learn.zybooks.com/zybook/UMDCIS1501CharneskyFall2018/chapter/7/section/3

    if body_parts == 6:
        print("Sorry, you lost. The hidden word was: '%s'" % hidden_word)

    keep_going = keep_going_function()

print("Thank you for playing! Goodbye.")



