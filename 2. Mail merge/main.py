PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as name_file:
    names = name_file.readlines()


with open("./Input/Letters/starting_letter.txt") as letter_file:
    sample_letter = letter_file.read()
    for name in names:
        striped_name = name.strip()
        new_letter = sample_letter.replace(PLACEHOLDER , striped_name)
        with open(f"./Output/ReadyToSend/mail_for_{striped_name}", mode="w") as mail:
            mail.write(new_letter)


