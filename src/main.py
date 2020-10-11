"""
This module defines the starting point of the radar tool.
"""
import argparse
import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import (
    classification_report,
    accuracy_score
)
from pyprind import ProgBar
from analyzer import noise_reduction
from errors import InvalidInputException
from input import (
    input_message,
    input_spam
)

PROGRES_BAR_STEPS = 6

parser = argparse.ArgumentParser(
    description="Radar arguments parser."
)
parser.add_argument(
    '--path', '-p',
    type=str,
    help='Path to dataset file.'
)

def main():
    """The starting point of the application."""
    progress_bar = ProgBar(
        PROGRES_BAR_STEPS,
        title='\n  - Spam Radar Initialization - \n',
        bar_char='#',
        track_time=True
    )

    # Parse the application arguments.
    progress_bar.update(item_id='Loading arguments...')
    args = parser.parse_args()

    # Load the data.
    progress_bar.update(item_id='Loading dataset...')
    dataframe = pd.read_csv(args.path)
    dataframe = dataframe.iloc[:2500]

    # Defines the tokens vectorizer.
    progress_bar.update(item_id='Initializing vectorizer...')
    vectorizer = CountVectorizer(analyzer=noise_reduction)

    progress_bar.update(item_id='Performing vectorizer transformation...')
    # Transform the text data into occurrence matrix.
    messages_bow = vectorizer.fit_transform(dataframe['text'])

    progress_bar.update(item_id='Splitting data into 80% training and 20% testing sets...')
    feature_train, feature_test, target_train, target_test = train_test_split(
        messages_bow,       # Defines the data features.
        dataframe['spam'],  # Defines the target features. The one that we want to predict.
        test_size=0.20,     # Defines the test data quantile.
        random_state=0      # Defines randomization seed to ensure that the order won't change.
    )

    classifier = MultinomialNB()
    progress_bar.update(item_id='Training Multinomial Naive Bayes classifier...')
    classifier.fit(feature_train, target_train)

    print('\n\n')
    print(" --- Classification report ---\n")
    target_predictions = classifier.predict(feature_test)
    print(classification_report(target_test, target_predictions))
    print('Accuracy: ', accuracy_score(target_test, target_predictions))
    print("------------------------------")

    while True:
        try:
            message = input_message()
            spam = int(input_spam())

            data = [[message, spam]]
            dataframe = pd.DataFrame(data, columns=['text', 'spam'])
            bow = vectorizer.transform(dataframe['text'])

            prediction = classifier.predict(bow)
            msg = 'Model prediction match: {}%'.format(
                accuracy_score(dataframe['spam'], prediction) * 100
            )
            print(msg)

        except InvalidInputException as error:
            print(error)
            break
        except KeyboardInterrupt as error:
            # Interrupt singnal received.
            break

    print('Exit!')

if __name__=='__main__':
    main()
