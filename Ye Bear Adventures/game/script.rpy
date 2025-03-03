## Ye Bear Adventures Visual Novel
# Backgrounds
image bg room = "images/room.jpg"
image bg mall = "images/mall.jpg"
image bg park = "images/park.png"
image bg school = "images/school.png"
image bg classroom = "images/classroom.png"
image bg alley = "images/alley.jpg"
image bg shop = im.Scale("images/shop.png", 1920, 1080)
image bg black_bg = "images/black-background.png"
image bg outside = im.Scale("images/outside.jpg", 1920, 1080)
# Ye bear Sprites
image yebear idle = im.Scale("images/yebear idle.png", 700, 800)
image yebear cute = im.Scale("images/yebear cute.png", 900, 900)
image yebear icecream = im.Scale("images/yebear icecream.png", 700, 800)
image yebear plushie = im.Scale("images/yebear plush.png", 950, 900)
image yebear gift = im.Scale("images/yebear gift.png", 650, 800)
image cat spot = "images/cat spot.png"
image cat idle = "images/cat idle.png"
image cat love = "images/cat love.png"
image cat end = "images/cat end.png"
# Background Music
define audio.bg_music = "audio/bgmusic default.mp3"
# Characters
define y = Character("Ye Bear", what_slow_cps=30)
define p = Character("[player_name]", what_slow_cps=30)
define pm = Character("[player_name]'s Mind", what_slow_cps=30)
define mf = Character("Mysterious Figure", what_slow_cps=10)
define b = Character("Ye Bear & [player_name]", what_slow_cps=30)
define c = Character("Cat", what_slow_cps=30)
define cn = Character("Carl The Cat", what_slow_cps=30)
# Function to input custom player name
label name_input:
    $ player_name = renpy.input("What name should we call you?")
    $ player_name = player_name.strip()
    if player_name == "":
        $ player_name = "Player"
    return

# The game starts here.
label start:

    # Ask for player's name
    call name_input
    "REMINDER TO LOWER BG MUSIC ON ESC > PREFERENCES > MUSIC VOLUME (Adjust to your liking)"
    # Introduction
    scene bg room with fade
    play music bg_music loop
    "Your friend Ye Bear suddenly went to your house."
    "He looked bored and wanted to do something productive or fun."
    show yebear idle at left
    y "Hey [player_name], I'm so booooored! Do we have something to do around here?"
    p "Hmm.."
    p "I got it!"
    y "What is it?"
    p "We could go out somewhere! To spend time together and engage on some activities!"
    y "That sounds like a great idea! Where should we go?"

    # First Choice: Destination
menu:
    "Go to the mall":
        p "I got an idea, let's go to the mall!"
        y "That sounds amazing! I haven't been in a mall in a hot minute!"
        jump mall
    "Go to the park":
        p "Let's head to the park!"
        y "Yay! I love parks!"
        jump outside
    "Go to school":
        p "We should probably head to school."
        y "School it is, [player_name]!"
        jump school

label mall:
    scene bg mall with fade
    "You both arrive at the mall after walking for a while."
    y "This place is huge!"
    p "Do you want to go somewhere?"
    y "You chose this place, you lead the way good sir!"
    # Second Choice: Shop or Go Home
    menu:
        "Enter the shop":
            jump mall_shop
        "Go home after roaming around":
            jump mall_ending



label mall_shop:
    scene bg shop with fade
    "Upon entering you are thinking about something in your head.."
    "A sudden act of kindess struck in your mind."
    "You decide to buy a gift for your good friend Ye Bear."
    pm "I should buy something for Ye Bear, since he deserves it."
    "You continue browsing around the store, exploring different items."
    show yebear idle at center
    y "This store has so many cool things! What should we get next?"
    menu:
        "Buy snacks":
            "You buy some delicious snacks to share."
            show yebear cute at center
            y "Yum! Thank you, [player_name]! This is my favorite snack, how'd you know?"
            p "Haha, well sometimes you don't know how much you talk on your phone without realizing.."
            show yebear idle at center
            y "Figures, thank you so much again [player_name]!"
            jump mall_store_exit
        "Buy a plushie":
            "You gave a gift to Ye Bear."
            show yebear gift at center
            y "Oh really [player_name], you shouldn't have!"
            p "Go ahead and open it! I'm sure you'll love it!"
            "Ye Bear proceeded to open it."
            show yebear plushie at center
            y "I love it! Thank you, [player_name] for the dog plushie!"
            y "It looks so soft and cuddly, I love dogs!"
            jump mall_store_exit

label mall_store_exit:
    "After shopping, you both leave the store happily."
    scene bg black_bg with fade
    jump mall_gift_ending

label mall_gift_ending:
    "Ye Bear enjoyed the day and loved the thing/s you bought him!"
    "ENDING 1, Gift Ending"
    return

label mall_ending:
    "After roaming around the mall, you and Ye Bear decide to grab some food and eat together."
    "With full bellies, you both head to the arcade to enjoy some games before parting ways."
    scene bg black_bg with fade
    "Ye Bear had a wonderful day and cherished the time spent with you!"
    "ENDING 2, Mall Ending"
    return

label outside:
    scene bg outside with fade
    "You two go outside to go wonder to your destination, the park."
    show yebear idle at center
    y "I love the fresh air!"
    p "Me too, do you want to do any activity before going to the park?"
    show yebear cute at center
    y "You chose this place, you lead the way good sir!"
    menu:
        "Go wonder around with Ye Bear":
            p "Let's explore somewhere before going to the park!"
            y "Alright good sir, lead the way!"
            jump back_alley
        "Go directly to the Park":
            jump park

label back_alley:
    "[player_name] and Ye Bear went to explore somewhere before going to the park."
    "After walking for a while, you suddenly stumbled in an eerie alley.."
    scene bg alley with fade
    "You suddenly feel a little chilly, since the ambience of the place gave you a bad feeling."
    show yebear idle at center
    y "Hey [player_name], I got a really bad feeling about this place..."
    hide yebear idle
    p "Yeah, I got a bad feeling about this alley.."
    p "It's like something is watching u-"
    stop music
    show yebear idle at center
    y "!!!"
    pm "!!!"
    hide yebear idle
    "A mysterious chill runs down your spine, leaving you both in silence."
    "Both of you check your surroundings, leaving both of you in an anxious state."
    p "Whoever you are, show yourself!"
    mf "..."
    p "Is that...?"
    mf "..."
    b "A CAT?!?"
    show cat spot at center
    c "meow"
    play music bg_music loop
    p "Phew! I thought it was something dangerous!"
    show yebear idle at left
    y "I thought so too!"
    hide yebear idle
    stop music
    show cat idle at center
    c "I can be dangrous if you want me to."
    b "!?!?"
    play music bg_music loop
    show yebear idle at left
    b "YOU CAN TALK?!"
    hide yebear idle
    c "Long story short, I'm quite the magical cat"
    c "Unfortunately, I don't have a name, so I just call myself what people call me!"
    show yebear idle at center
    y "Which is..?"
    hide yebear idle
    show cat idle at center
    c "Either Cat, Kitty, Ming Ming, or pspspsps!"
    "Ye Bear chuckled at whatever the cat said, leaving the cat confused"
    c "Why are you laughing?"
    c "Don't you get called that too?"
    show yebear idle at left
    y "No! Not at all kitty!"
    y "I have my own name, which is Ye."
    c "Ye..."
    c "That's a great name! How'd you come up with it?"
    hide cat idle
    show yebear idle at center
    y "Well of course I go by Ye bear, but my parents named me this!"
    hide yebear idle
    show cat idle at center
    c "That's so cool!"
    c "I wish I had a name..."
    hide cat idle
    show yebear idle at center
    y "I can give you a name if that makes you happy!"
    hide yebear idle
    show cat idle at center
    c "Really??"
    show yebear idle at left
    y "Of course!"
    y "Let me think of one though.."
    y "Hmm..."
    y "Aha!"
    y "Carl sounds like a great name for you!"
    c "Carl..."
    c "I don't like it.."
    hide cat idle
    show yebear idle at center
    y "..."
    hide yebear idle
    show cat idle at center
    c "I LOVE IT!!"
    hide cat idle
    show yebear idle at center
    y "Sounds great right? Carl The Cat has got a ring to it!"
    hide yebear idle
    show cat love at center
    cn "I know! Thanks again Ye Bear!"
    p "Hey Carl The Cat, do you live somewhere? You seem lost when we found you.."
    show cat idle at center
    cn "Actually in that case, yes."
    cn "I currently am finding a place to stay, that's why I went to this alley in the first place!"
    hide cat idle
    show yebear idle at center
    y "I have an idea!"
    y "You can stay with me! Crash on my place you know?"
    hide yebear idle
    show cat idle at center
    cn "Really you'd do that?"
    hide cat idle
    show yebear idle at center
    y "Of course! Anything for a furry friend!"
    hide yebear idle
    show cat idle at center
    cn "Thank you so much Ye Bear! I'll repay you eventually somehow!"
    hide cat idle
    show yebear idle at center
    y "No need! All I need is a new friend!"
    hide yebear idle
    show cat love at center
    cn "Lead the way my new friend!"
    hide cat idle
    show yebear idle at center
    y "Hey [player_name], can I go to my house with my new friend?"
    y "I feel like the park can be for another time!"
    p "Yeah sure! We came out today for you to enjoy anyways!"
    jump cat_ending
    
label park:
    "asdasdads"

    return
label cat_ending:
    "After that long discussion, [player_name] parted ways with Ye Bear and Carl The Cat."
    scene bg black_bg with fade
    show cat end at Position(ypos=0.750)
    "After when Carl The Cat finally lived at Ye Bears house, Carl The Cat and Ye Bear are even closer than ever"
    "They even spend time with you to watch movies or play video games at your house!"
    "ENDING 3, Cat Ending"
    return
label school:
    scene bg school with fade
    p "You arrive at school, what should we do?"
    menu:
        "Go to class":
            jump school_class
        "Leave and go to the mall":
            jump mall

label school_class:
    p "You two finish the entire school day and go home tired."
    return

# The End
return
