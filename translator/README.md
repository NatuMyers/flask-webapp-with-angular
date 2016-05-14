# PirateTranslator
created english-pirate translator app using HTML, CSS, Python, and Flask

Summary
---
Simple app with only a few pages:
- Home
- Game page (takes input)
- Results page (shows output)
  Asks to play again (routes back to Home or to Goodbye)
- Goodbye

This allows me to become more familiar with Flask and routing pages back and forth. It also allows me to practice HTML and CSS.

Getting Set Up
---
Create and activate a new, empty virtual environment.

`virtualenv env`
`source env/bin/activate`

Use pip to install the packages required in requirements.txt.

`pip install -r requirements.txt`

Start the application by running pirate_gen.py.
Navigate to http://localhost:5000 and start exploring the app.

How to Explore
---
Input sentence that will be translated. Translating dictionary and code in:

`pirate_gen.py`

Shows the original input and translated result.

Allows for multi-play by routing you back to the homepage or to an exit page.

HTML and CSS
---
Utilized CSS classes, which allowed for a streamlined look across the app:

`pirate_style.css`
