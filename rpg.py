full_dot = '●'
empty_dot = '○'

def create_character(name, strenght, intellegence, charisma):
    if not isinstance(name, str):
        return "The character name should be a string"
    if name == '':
        return "The character should have a name"
    if len(name) > 10:
        return "The character name is too long"
    if " " in name:
        return "The character name should not contain spaces"
    if not isinstance(strenght, int) or not isinstance(intellegence, int) or not isinstance(charisma, int):
        return "All stats should be integers"
    if strenght < 1 or intellegence < 1 or charisma < 1:
        return "All stats should be no less than 1"
    if strenght > 4 or intellegence > 4 or charisma > 4:
        return "All stats should be no more than 4"
    if strenght + intellegence + charisma != 7:
        return "The character should start with 7 points"
    return (
        f"{name}\n"
        f"STR{full_dot * strenght}{empty_dot *(10 - strenght)}\n"
        f"INT{full_dot * intellegence}{empty_dot *(10 - intellegence)}\n"
        f"CHA{full_dot * charisma}{empty_dot *(10 - charisma)}\n"
    )


create_character('ren', 4, 2, 1)
print(create_character('ren', 4, 2, 1))
