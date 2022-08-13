import time


def dialog(script, time_lag):
    for i in script:
        print(i, end='')
        time.sleep(time_lag)
    print()


def conversation(con_list, interval, before=0.0, after=0.0):
    time.sleep(before)
    for con in con_list[0:-1]:
        print(con)
        time.sleep(interval)
    print(con_list[-1])
    time.sleep(after)


def user_input(option_list, answer_list, response_list, error_message, interval, trigger='', before=0.0, after=0.0):
    time.sleep(before)
    for option in option_list:
        print(f'        {option}')
    while True:
        answer = input(f"{trigger}").upper()
        if answer in answer_list:
            break
        else:
            print(error_message)
    time.sleep(interval)
    print(response_list[answer_list.index(answer)])
    time.sleep(after)


def artcode(place, password):
    while True:
        if input("\033[0;32m[ENTER PASSWORD TO CONTINUE]\033[0m") == password:
            break
        else:
            time.sleep(1)
            print(f"\033[0;32m[PASSWORD INCORRECT, SCAN THE ARTCODE NEAR THE {place} TO GET THE PASSWORD]\033[0m")
    time.sleep(1.4)


def correct_answer(question, answer, error_message):
    while True:
        if input(question).upper() == answer:
            break
        else:
            print(f"\033[0;32m[{error_message}]\033[0m")
    time.sleep(1.4)


#################################################
print("WELCOME TO TINA REX'S WONDERLANDS")
input('PRESS ENTER TO PLAY')
dialog('LOADING', 1)

loading = ['\033[0;32m[searching for signal]\033[0m',
           '\033[0;32m[establishing connection]\033[0m',
           '\033[0;32m[receiving message]\033[0m']

conversation(loading, interval=1.4, before=1)

Act1 = ['???: Hello?',
        '???: Can you read me?']

conversation(Act1, 2, before=2, after=1)

user_input(['A. Yes!', 'B. Who is this'],
           ['A', 'B'],
           ["???: Oh, finally! I've waited far too long", '???: Sorry! Let me introduce myself.'],
           '\033[0;32m[PLEASE ANSWER A OR B]\033[0m', 1.4,
           trigger='Answer: ')

Act2 = ["???: I am Tina Rex, the Queen of the kingdom of dinosaurs, Mondstadt.",
        "Tina Rex: My kingdom was destroyed in a battle with Godzilla 66 million years ago.",
        "Tina Rex: And I lost my father Tim Rex in that war.",
        "Tina Rex: My cousins went extinct, but I survived until today.",
        "Tina Rex: Brave traveller, I need your help to defeat Godzilla and bring glory to Mondstadt!",
        "Tina Rex: Are you willing to help me?"]

conversation(Act2, 2, before=2, after=1)

user_input(['A. Yes.', 'B. Why not?'],
           ['A', 'B'],
           ["Tina Rex: Thank you, Traveller! What is your name?",
            "Tina Rex: Thank you, Traveller! What is your name?"],
           '\033[0;32m[PLEASE ANSWER A OR B]\033[0m', 1.4,
           trigger='Answer: ')

print('\033[0;32m[PLEASE ENTER YOUR NAME]\033[0m')
name = input('Name: ')

Act3 = ["Tina Rex: ... Doesn't sound like a local name to me.",
        f"Tina Rex: Anyway, {name}, you are now the Honorary Knight of Mondstadt.",
        "Tina Rex: It's time to face the Godzilla, but not in this outfit.",
        "Tina Rex: I have prepared the amour for you. Please get dressed!",
        '\033[0;32m[amour collected]\033[0m']

conversation(Act3, 2, after=1)

input('Press Enter to get dressed')
time.sleep(1.4)

Act4 = ["\033[0;32m[amour equipped]\033[0m",
        "Tina Rex: Wow! It's perfect for you.",
        "Tina Rex: Now you need a powerful weapon!",
        "Tina Rex: I left a sword at Uncle Penguin's place.",
        "Tina Rex: Go to the bird gallery and talk to him!",
        "Tina Rex: If you find him, scan the ARTCODE near him!",
        "Tina Rex: And you will get the password!"]

conversation(Act4, 2, after=1)

artcode('PENGUIN', '111')

Act5 = [f"???: Hello, Traveller {name}!",
        "???: I'm Uncle Penguin!",
        "Uncle Penguin: I have heard of you!",
        "Uncle Penguin: Please bring the best sword.",
        "Uncle Penguin: And take care of yourself!",
        "\033[0;32m[Skyward Blade collected]\033[0m"]

conversation(Act5, 2, after=1)

Act6 = ['Tina Rex: Great!',
        'Tina Rex: Godzilla has some soldiers working for him.',
        "Tina Rex: Let's defeat them together.",
        "Tina Rex: There is an Indian Lion nearby.",
        "Tina Rex: When you find him, scan the ARTCODE and enter the PASSWORD to fight."]

conversation(Act6, 2, after=1)

artcode('INDIAN LION', '112')

Act7 = ["Indian Lion: Interesting! You want to challenge Godzilla?",
        "Indian Lion: Hahaha! It's impossible.",
        "\033[0;32m[CHOOSE THE ATTACKING WAY]\033[0m",
        '        A. Attacking by Skyward Blade\n        B. Punch']

conversation(Act7, 2, after=1)

correct_answer('Answer: ', 'A', 'it seems not working... try another way?')

Act8 = ["\033[0;32m[You defeated Indian Lion!]\033[0m",
        "Indian Lion: Ah, I didn't expect that.",
        "Indian Lion: But you will never win Godzilla!",
        '\033[0;32m[key "T" acquired]\033[0m',
        "Tina Rex: Hooray! We win!",
        "Tina Rex: Seems that you are ready to fight Godzilla.",
        "Tina Rex: Let's head to the 1ST FLOOR of the museum!",
        "Tina Rex: When you arrive, look for and scan the ARTCODE to continue."]

conversation(Act8, 2, after=1)

artcode('GODZILLA', '113')

Act9 = [f"???: Oh, it's you {name}!",
        "???: I am Godzilla!",
        "Godzilla: I didn't expect you'd be here.",
        "Godzilla: But I won't let you get out alive!",
        "\033[0;32m[CHOOSE THE ATTACKING WAY]\033[0m",
        '        A. Attacking by Skyward Blade\n        B. Punch']

conversation(Act9, 2)

input('Answer: ')

Act10 = ["\033[0;32m[You were defeated by Godzilla!]\033[0m",
         "Godzilla: Hahaha, I told you that you can never beat me!",
         "Tina Rex: That was close.",
         "Tina Rex: But I'm glad that we escaped.",
         "Tina Rex: Godzilla has been much stronger for his daily workouts.",
         "Tina Rex: We need more powerful weapons.",
         "Tina Rex: Let's head to the MINERAL GALLERY!",
         "Tina Rex: We may find something useful there.",
         "Tina Rex: There might be another ARTCODE there, be careful!"]

conversation(Act10, 2, after=5)

Act11 = ["Tina Rex: Have you found the ARTCODE?",
         "Tina Rex: When you find it, scan it and get the password."]

conversation(Act11, 2, after=1)

artcode('METEORITE', '114')

Act12 = ["Tina Rex: Look at the meteorite!",
         "Tina Rex: Actually, my ancestors went extinct because of an impact of an asteroid.",
         "Tina Rex: Take the meteorite with you, it will bring you power.",
         "\033[0;32m[meteorite acquired]\033[0m",
         '\033[0;32m[key "R" acquired]\033[0m',
         "Tina Rex: I will see you in the next room, where you can see a real me."]

conversation(Act12, 2, after=5)

input('Tina Rex: When you arrive, press ENTER to continue')

Act13 = ["Tina Rex: Now you see the real me.",
         "Tina Rex: Here is another Key for you.",
         '\033[0;32m[key "E" acquired]\033[0m',
         "Tina Rex: And don't forget to take some selfies with me."]

conversation(Act13, 2, after=5)

Act14 = ["Tina Rex: There is a Giraffe nearby.",
         "Tina Rex: She also works for Godzilla.",
         "Tina Rex: When you see her, scan the ARTCODE and try to get some information from her."]

conversation(Act14, 2, after=1)

artcode('GIRAFFE', '115')

Act15 = ['Giraffe: Hmm, another one to challenge Godzilla?',
         'Giraffe: You look more powerful than those previous challengers',
         'Giraffe: I have heard that you defeated Indian Lion.',
         'Giraffe: But you will never beat me!',
         '\033[0;32m[CHOOSE THE ATTACKING WAY]\033[0m',
         '        A. Attacking by Skyward Blade\n        B. Punch']

conversation(Act15, 2, after=1)

correct_answer('Answer: ', 'B', 'it seems not working... try another way?')

Act16 = ["\033[0;32m[You defeated the Giraffe!]\033[0m",
         "Giraffe: You win!",
         "Giraffe: I am convinced by your power.",
         '\033[0;32m[key "X" acquired]\033[0m',
         "Tina Rex: Bravo!",
         "Tina Rex: You have now collected four keys! There must be a treasure nearby.",
         "Tina Rex: Let's go to the T.REX SKELETON HALL!",
         "Tina Rex: We may find the treasure there."]

conversation(Act16, 2, after=2)

input('Tina Rex: When you the T.REX SKELETON HALL, press ENTER to continue')

Act17 = ["Tina Rex: Seems that the introductions on the wall are important.",
         "Tina Rex: Maybe you should pay attention to the information."]

conversation(Act17, 2, after=5)

Act18 = ["Tina Rex: There is a dig site room, the treasure must be hidden there!",
         "Tina Rex: If you find the DIG SITE, scan the ARTCODE nearby."]

conversation(Act18, 2, after=1)

artcode("DIG SITE", '122')

Act19 = ["Tina Rex: Oh, there is a question for you!",
         "Tina Rex: Am I a predator or scavenger?",
         '        A. Predator\n        B. Scavenger\n        C. Both']

conversation(Act19, 2, after=1)

correct_answer('Answer: ', 'C', 'The answer is incorrect, go back to the T.REX SKELETON HALL and look for the answer.')

Act20 = ["Tina Rex: That's right!",
         "Tina Rex: And you got the treasure chest!",
         '\033[0;32m[treasure chest acquired]\033[0m',
         "Tina Rex: You can use the keys you collected to open it."]

conversation(Act20, 2, after=1)

correct_answer('Enter the keys collected to open the chest: ', 'TREX', 'Hint: 4 letters about Tina Rex')

Act21 = ["Tina Rex: It opened!",
         "Tina Rex: Congratulations!",
         "Tina Rex: You got an Amos' Bow!",
         "\033[0;32m[Amos' Bow acquired]\033[0m",
         "Tina Rex: Now you got the power to fight Godzilla!",
         "Tina Rex: Go back to the EXTINCT AND ENDANGERED SPECIES AREA when you are ready."]

conversation(Act21, 2, after=1)
input('Tina Rex: When you arrive, press ENTER to continue')

Act22 = [f'Godzilla: Traveller {name}, nice to see you again!',
         "Godzilla: But I won't let you sneak this time!",
         f'{name}: I challenge you...',
         f'{name}: ...To a duel before the throne!',
         "Tina Rex: Proceed.",
         "Godzilla: You are aware... that the loser must die?",
         "Godzilla: Are you sure this is what you want?",
         "\033[0;32m[CHOOSE THE ATTACKING WAY]\033[0m",
         "        A. Attacking by Skyward\n        B. Attacking by Amos' Bow\n        C. Punch"]

conversation(Act22, 2, after=1)
correct_answer('Answer: ', 'B', 'it seems not working... try another way?')

Act23 = ["\033[0;32m[You defeated Godzilla!]\033[0m",
         "Godzilla: It's impossible! Ah, how could I?!",
         f"Tina Rex: Thank you, Traveller {name}!",
         "Tina Rex: You have defeated Godzilla and saved my kingdom!",
         "Tina Rex: I'm willing to let my daughter, Astrologist Mona Megistus, marry you!",
         f"{name}: Thank you, Tina Rex!"]

conversation(Act23, 2, after=1)

Act24 = ["The Traveller and the Princess lived happily ever after.",
         "The End."]

conversation(Act24, 2, after=2)

print()
print('Thank you for playing my game!')
