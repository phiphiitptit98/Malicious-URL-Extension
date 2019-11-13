# Import library
import pandas as pd
import numpy as np
import sys
import random
from six.moves.urllib.parse import urlparse

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
# from google.colab import files
# uploaded = files.upload()

def Check_URL(test_url) :
    data = pd.read_csv("data.csv")
    data.head()

    # Labels
    y = data["label"]

    # Features
    url_list = data["url"]

    # Using Tokenizer
    vectorizer = TfidfVectorizer()

    # Store vectors into X variable as Our XFeatures
    X = vectorizer.fit_transform(url_list)

    # Split into training and testing dataset 80:20 ratio
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # print("X_train")
    # print(X_train)
    # print("X_test")
    # print(X_test)
    # print("y_train")
    # print(y_train)
    # print("y_test")
    # print(y_test)
    # print(train_test_split(X, y, test_size=0.2, random_state=42))

    # Model Building using logistic regression
    logit = LogisticRegression()
    logit.fit(X_train, y_train)

    # Accuracy of Our Model
    # print("Accuracy of our model is: ",logit.score(X_test, y_test))
    X_predict = []
    X_predict.append(test_url)
    X_predict = vectorizer.transform(X_predict)
    y_Predict = logit.predict(X_predict)
    return y_Predict
    # print (y_Predict)
    
    # print("Accuracy of our model is: ",logit.score(X_test, y_test))
def strip_scheme(url):
    parsed = urlparse(url)
    scheme = "%s://" % parsed.scheme
    return parsed.geturl().replace(scheme, '', 1)



def main():
    url = sys.argv[1]
    url=strip_scheme(url)
    url= url.replace("www.","")
    # url = "https://"+url
    print(url)
    predict = Check_URL(url)
    print(predict)
    if predict=="bad":
        print("Do Not visit")
    else:
        print("Oke")

if __name__ == "__main__":
    main()

