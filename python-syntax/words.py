#1
#words = ["cat", "dog", "rat"]
#for word in words:
#    print(word.upper())
#2
def print_upper_words(words, must_start_with):
    
    for word in words:
        for m in must_start_with:
            if word[0] == f"{m}":
                print(word.upper())