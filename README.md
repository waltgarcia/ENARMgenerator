# ENARM Exam Prep Deck Generator
ENARM Exam Prep Deck Generator is a Python script designed to create Anki decks for the ENARM (Examen Nacional de Aspirantes a Residencias Médicas) exam preparation from a CSV file. The script enables users to easily format questions and answers using Markdown syntax, including H1 for questions and H2 with cursive formatting for answers. Even it was designed to medical questions, it can be used with any CSV file with format of questions and answers.

## Getting Started
###Prerequisites
To use the script, you will need:

- Python (version 3.7 or higher)
- The genanki library
You can install the required library using pip:

```
pip install genanki
```

#Installation
- Clone or download this repository to your local machine.
- Ensure you have the prerequisite packages installed (Python and genanki).
- Place your ENARM questions and answers in a CSV file with two columns: "Pregunta" for questions and "Respuesta" for answers.
- Run the script with the following command, replacing 'Anki-Endocrinología.csv' with the name of your CSV file:
  
```
python generate_anki_deck.py 'Anki-Endocrinología.csv'
``` 

## Usage
The script takes the content from the CSV file, processes it, and generates an Anki deck in .apkg format. This deck can be imported into Anki for your exam preparation.

CSV File Format
The expected CSV file format:

Column 1: "Pregunta" - Contains the questions in Markdown (H1).
Column 2: "Respuesta" - Contains the answers in Markdown with cursive formatting (H2 and italics).
Customization
You can customize the Anki deck's appearance by modifying the card templates, changing the CSS styling, or altering the model's design. Refer to the Anki documentation for further customization options.

### Formatting with Markdown
The script converts Markdown content in your CSV file into HTML for Anki cards. Here's an example:

Questions are wrapped in H1 tags (# Question).
Answers are wrapped in H2 tags (## *Answer*).
Example:
Input (CSV):
```
Pregunta,Respuesta
# What is ENARM?,## *ENARM* stands for Examen Nacional de Aspirantes a Residencias Médicas.
Output (Anki card):

Front (Question): What is ENARM?
Back (Answer): ENARM stands for Examen Nacional de Aspirantes a Residencias Médicas.
```

###Contributing
If you would like to contribute to this project, feel free to submit a pull request or open an issue on our GitHub repository.

### License
This project is licensed under the MIT License. See the LICENSE file for details.

### Contact Information
For questions or feedback, you can contact us at wgarciao@tutanota.com

### Changelog
Version 1.0 (Date): Initial release with basic functionality.

### Roadmap
Support for additional formatting options.
Enhanced customization features.

### Credits
This project uses the genanki library for Anki deck creation.

### Conclusion
We hope this tool helps you in your journey to prepare for the ENARM test. Good luck with your studies!
