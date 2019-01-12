define radolf = Character('Radolf', color="008000")
define unk_fire_guard = Character('???', color="00FF00", what_font="fonts/hymmnos.ttf")

label village_start:
    scene bg village at truecenter with fade
    
    if not village_saw_first_visit:
        jump village_first_visit
        
    if inn_saw_aurica_conversation and not village_saw_second_visit:
        jump village_second_visit
    
    jump village_none
    
label village_none:
    "There's nothing here..."
    
    scene bg black with dissolve
    
    jump map
    
label village_first_visit:
    lyner "This village is deserted. Nobody's here..."
    lyner "I should look around some more..."
    lyner "Radolf?"
    
    radolf "And who might you be?"
    
    lyner "R... Radolf...? No, he talks a little strange. Too formal to be Radolf..."
    
    radolf "I sincerely doubt that you are in any position to judge me like that. I don't even know you. It's only proper for me to be polite to people."
    
    lyner "Okay, fine... whatever. So, does anyone else live in this village?"
    
    radolf "The Sick Lady, the Songless Princess, and I are the only residents of this village. It is only the three of us."
    radolf "However, this village is facing a crisis."
    
    lyner "...A crisis?"
    
    radolf "The Songless Princess is perpetually trying to burn down the village. And it falls upon me to save this village every time."
    
    lyner "I see."
    
    radolf "Therefore, I must be on my way. I'm on my way to patrol as we speak."
    
    lyner "...Radolf sounded strange. But it's also not normal for someone to want to burn down a village."
    
    lyner "I don't know what's going on. I'll just have to investigate some more... Where is Aurica?"
    
    $ village_saw_first_visit = True
    
    jump map
    
label village_second_visit:
    
    radolf "Emergency! The Fire Demon has struck again! We have to stop it as best we can."
    
    lyner "What!? Aurica..."
    
    aurica_std "No, I can't... I can't win."
    
    radolf "I have to do something. The village will be destroyed... I'm going to attack!"
    
    lyner "Radolf!!"
    
    aurica_std "He knows that he can't win, so why does he fight...?"
    
    lyner "Because he's determined to save this world."
    lyner "While you blame yourself for being incompetent, many people are supporting you."
    
    aurica_std "I never asked them to do anything..."
    
    # choices: Persuade Aurica, Undecided
    
    # chose Persuade Aurica
    lyner "Aurica!"
    lyner "You know why Radolf is saving you, right?"
    
    aurica_std "No, I don't..."
    
    lyner "That's not true."
    lyner "This is your world. Radolf is saving you because you want him to. Am I right?"
    
    aurica_std "Well..."
    
    lyner "You don't have to do it for Radolf. But I want you to save your village and world on your own."
    
    aurica_std "..."
    aurica_std "...Okay."
    
    lyner "What!?"
    
    aurica_std "It's really hot. The demon is here to burn down the village..."
    
    flamia "Burning... burning... everyone is burning..."
    
    lyner "I won't let you!"
    lyner "Aurica! Protect the village. You're the only one who can save this world!"
    
    aurica_std "But, I don't even know how!"
    
    fireball "I have a plan! He attacks us by blowing fire, so we can protect ourselves by building a firewall."
    
    lyner "But what should I make it out of?"
    
    fireball "Your job is to figure that out!"
    
    lyner "Why, you..."
    
    aurica_std "It's okay, I'll try it, but it might not work..."
    
    lyner "Aurica..."
    
    aurica_std "I can't let everyone else do all the work. I can do this..."
    aurica_std "...Just don't laught at me, alright?"
    
    lyner "I won't laugh."
    
    aurica_std "I see. I'll do it..."
    aurica_std "Huh!"
    aurica_std "Please! Appear!"
    
    unk_fire_guard "Was granme gaya khal yor elle fayra"
    
    lyner "Wh-what is this!?"
    
    aurica_std "I thought that I could blow away fire with wind... So I made this..."
    
    flamia "I'll burn it all...!"
    
    aurica_std "It's not working... I wasn't good enough..."
    
    lyner "No, don't give up! Think harder! Imagine yourself beating the demon in your head!"
    
    aurica_std "I'll try. I hope this works..."
    
    lyner "It will, trust me. Believe in your power."
    
    aurica_std "Yes, I can feel the energy. Nobody ever encourage me like this before."
    aurica_std "You're right. It's worth trying!"
    aurica_std "Fire Guard... please protect us all!"
    
    fire_guard "Was granme gaya khal yor elle fayra"
    
    lyner "Th-this is...!"
    
    flamia "Whewwww!"
    
    lyner "The fire's being blown away!?"
    
    aurica_std "Did I do it?"
    
    lyner "Yes, you did! Aurica, you saved the village!"
    
    aurica_std "I can't believe I did it..."
    
    fireball "It's too early to celebrate. He's still alive. He'll be back soon."
    
    lyner "Then next time, you have to beat it."
    
    aurica_std "...But, I..."
    
    lyner "Don't worry. You can do it as long as you believe in yourself."
    
    aurica_std "You're right... I hope I can do it."
    
    lyner "..."
    
    $ village_saw_second_visit = True
    
    jump map
    