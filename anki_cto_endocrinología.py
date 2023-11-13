# -*- coding: utf-8 -*-
"""Anki CTO Endocrinología

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14ZS2SMwb918WhBoHxqOZnXEuFYmYzKC0
"""

!pip install genanki

import csv
import genanki
import markdown

# Define a function to convert text to HTML using Markdown with custom formatting
def markdown_to_html(text, is_question=False):
    if is_question:
        return f'<h1>{markdown.markdown(text)}</h1>'
    else:
        return f'<h2><i>{markdown.markdown(text)}</i></h2>'

# Define the Anki model
model = genanki.Model(
    1607392319,  # Unique ID for the model
    'CTO - Endocrinología Model',
    fields=[
        {'name': 'Pregunta'},
        {'name': 'Respuesta'},
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '{{Pregunta}}',
            'afmt': '{{FrontSide}}<br>{{Respuesta}}',
        },
    ])

# Create an Anki deck
deck = genanki.Deck(2059400110, 'CTO - Endocrinología')

# Read data from the CSV file and add cards to the deck
with open('Anki - Endocrinología (1).csv', 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        pregunta = markdown_to_html(row['Pregunta'], is_question=True)
        respuesta = markdown_to_html(row['Respuesta'], is_question=False)

        card = genanki.Note(
            model=model,
            fields=[pregunta, respuesta]
        )
        deck.add_note(card)

# Create an Anki package (.apkg)
genanki.Package(deck).write_to_file('CTO-Endocrinologia.apkg')

print('The .apkg file with custom formatting has been successfully generated for the "CTO - Endocrinología" deck.')