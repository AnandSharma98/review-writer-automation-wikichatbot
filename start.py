import nltk # refers to NATURAL LANGUAGE TOOLKIT
import warnings
import random

warnings.filterwarnings("ignore")

# nltk.download() # for downloading packages
# nltk.download('punkt') #first-time use only
# nltk.download('wordnet') #first-time use only


"""              small greeting function                """

GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up", "hey",)
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]


# Checking for greetings
def greeting(sentence):
    """If user's input is a greeting, return a greeting response"""
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)


""" getres function to give the queried result from wiki
    there's use of little pre-text processing (you can learn online how to do that)
     i know it can be improved further , but yeah try another queries to see at least it is working"""


def getres(user_response):
    # split into words
    tokens = nltk.word_tokenize(user_response)
    # convert to lower case
    tokens = [w.lower() for w in tokens]
    # remove punctuation from each word
    import string
    table = str.maketrans('', '', string.punctuation)
    stripped = [w.translate(table) for w in tokens]
    # remove remaining tokens that are not alphabetic
    words = [word for word in stripped if word.isalpha()]
    # filter out stop words
    from nltk.corpus import stopwords
    stop_words = set(stopwords.words('english'))
    words = [w for w in words if not w in stop_words]
    try:
        import wikipedia
        document = wikipedia.summary(words, sentences=5)
        return document
    except Exception as e:
        print("type query precisely "+str(e))


flag = True
print("ROBO: My name is Robo. I will answer your queries about Chatbots. If you want to exit, type Bye or to make "
      "automatic review just type 'review'")

while (flag == True):
    user_response = input("YOU:")
    user_response = user_response.lower()
    if (user_response != 'bye'):
        if (user_response == 'thanks' or user_response == 'thank you'):
            flag = False
            print("ROBO: You are welcome..")
        else:
            if (greeting(user_response) != None):
                print("ROBO: " + greeting(user_response))
            else:
                if(user_response=="review"):
                    import review
                    review.review_writer()
                else:
                    print("ROBO: ", end="")
                    getres(user_response)
                    print(getres(user_response))
    else:
        flag = False
        print("ROBO: Bye! take care..")

