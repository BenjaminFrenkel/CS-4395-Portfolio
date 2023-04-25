import pickle

from nltk import word_tokenize

def readFile (fileName):
    f = open(fileName, mode='r', encoding='utf-8')
    text = f.read()
    text = text.replace("\n", "")
    unigrams = word_tokenize(text)
    f.close()

    #print(unigrams)

    bigrams = [(unigrams[k], unigrams[k + 1]) for k in range(len(unigrams) - 1)]
    #print(bigrams)

    unigram_dict = {t: unigrams.count(t) for t in set(unigrams)}
    print(unigram_dict)

    bigram_dict = {b: bigrams.count(b) for b in set(bigrams)}

    return unigram_dict, bigram_dict

#Make the english files
unigram_dict_english, bigram_dict_english = readFile("LangId.train.English")

f = open('English_Unigram_Dict.txt', 'wb')
pickle.dump(unigram_dict_english, f)
f.close()

f = open('English_Bigram_Dict.txt', 'wb')
pickle.dump(bigram_dict_english, f)
f.close()

#Make the french files
unigram_dict_french, bigram_dict_french = readFile("LangId.train.French")

f = open('French_Unigram_Dict.txt', 'wb')
pickle.dump(unigram_dict_french, f)
f.close()

f = open('French_Bigram_Dict.txt', 'wb')
pickle.dump(bigram_dict_french, f)
f.close()

#Make the italian files
unigram_dict_italian, bigram_dict_italian = readFile("LangId.train.Italian")

f = open('Italian_Unigram_Dict.txt', 'wb')
pickle.dump(unigram_dict_italian, f)
f.close()

f = open('Italian_Bigram_Dict.txt', 'wb')
pickle.dump(bigram_dict_italian, f)
f.close()