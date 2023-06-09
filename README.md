# Grammatical Error Detection (NLP Project)	


Project for the course "Introduction to Language Technology" (Spring 2022)

This repository contains a Python script for grammar checking of text files. It is designed to identify several types of errors:

- Capitalization errors: Checks the first letter of a sentence if it is lower case.

- Fragment errors: Checks if there is any verb in a sentence.

- Verb form errors: Checks for errors in the usage of modals and infinitive forms of verbs.

- Subject-verb agreement errors: Checks for common subject-verb agreement mistakes.

- Spelling errors: Checks for words not found in the English word corpus provided by the Natural Language Toolkit (NLTK).

# Installation and Requirements

To run the script, you need Python 3 and the NLTK library. You can install NLTK using pip:

```pip install nltk```


# Usage

The script expects a text file named 'error.txt' in the same directory. This file should contain the text you want to check.

To run the script, simply execute the Python file in your command line:

```python detection.py```

The script will print out the detected errors along with the type of error and the word where the error was found.

# Limitations and Future Work

The current implementation of the grammar checker has some limitations. It uses a simple approach and may not catch all possible errors. Furthermore, the quality of the grammar checking depends on the quality of the POS tagging, which can have errors, especially for ambiguous words or in complex sentences.

Future improvements could include using machine learning models for improved error detection and correcting detected errors.
