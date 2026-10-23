# RPG Character Generator

This project contains a small Python program, `rpg.py`, that creates a simple RPG character sheet.

The script defines `create_character(name, strength, intelligence, charisma)`, which validates the input and returns a formatted character summary. It checks that:

- the name is a non-empty string without spaces and within the length limit
- each stat is an integer between 1 and 4
- the total of all stats equals 7

If the values are valid, it prints a visual stat bar for strength, intelligence, and charisma using filled and empty circles. The program ends by creating and displaying a sample character named `ren` with stats `4, 2, 1`.

Run it with:

```bash
python rpg.py
```

---------------------
credits to FreeCodeCamp for this exercise! https://www.freecodecamp.org/learn/python-v9/lab-rpg-character/build-an-rpg-character
---------------------