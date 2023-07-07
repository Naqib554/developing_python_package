def count(file, words):
    """this count the word and then return to the user 
    the word is appeared much time there are many"""
    with open(file) as text:
        file1 = text.read()
    word_count = {}
    for word in words:
        count = file1.count(word)
        word_count[word] = count
    for word, count in word_count.items():
        print("The word '{}' appears {} times.".format(word, count))

file = 'tweets.csv'
word_list = ['English', 'Web', 'source']  # Replace with your list of words
count(file, word_list)



      