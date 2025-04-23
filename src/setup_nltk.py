import nltk

def download_nltk_resources():

    try:
        nltk.data.find("tokenizers/punkt")
        nltk.data.find("corpora/stopwords")
        nltk.data.find("corpora/wordnet")
        nltk.data.find("corpora/omw-1.4")
        nltk.data.find('punkt_tab')
    except:
        nltk.download("punkt")
        nltk.download("stopwords")
        nltk.download("wordnet")
        nltk.download("omw-1.4")
        nltk.download('punkt_tab')
