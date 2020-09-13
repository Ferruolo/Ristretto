# RISTRETTO: A METHOD OF TEXT SUMARIZATION:

The goal of ristretto is to use natural language processing to extract the core meaning of a piece of text. It does this by breaking a corpus into phrases, and then using the approach found in grouping.ipynb to break group those phrases by cosine similarity. Once grouped, those phrases with the highest cosine similarity to other phrases in their group will be selected as "summary phrases." Said summary phrases can then be fed into a generator in order to create a readable summary, or used in some type of algorithm such as predicting with headlines in http://github.com/ferruolo/delphi.

# Here is a quick description of each folder in this repository
* phrase_dataset: dataset for phrase_classifier, output by generate_dataset.py
* scraper: method of scraping the guardian and moving words to vectors
* generate_dataset.py: scrapes entire guardian homepage, outputs formated csvs to phrase_dataset
* grouping.ipynb: Notebook where method of grouping vectiors is proven. As the project is not yet complete, this is probably the most interesting part of the project right now, as it is not complete
* phrase_classifier.ipynb: an lstm that brakes a corpus into phrases. Currently needs more data for better training
* README.md: this file




# Project TODOs:
Integrate phrases rather than words
Generator (this is going to take a while)