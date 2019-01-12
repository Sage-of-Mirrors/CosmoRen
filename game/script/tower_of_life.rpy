define flamia = Character('Flamia', color="FF00FF")
define fire_guard = Character('Fire Guard', color="FF00FF", what_font="fonts/hymmnos.ttf")

label tower_of_life_start:
    scene bg boundary gate at truecenter
    
    if village_saw_second_visit and not tower_of_life_saw_flamia_fight:
        jump tower_of_life_flamia_fight
    
    jump tower_of_life_none
    
label tower_of_life_none:
    "There's nothing here..."
    
    scene bg black with dissolve
    
    jump map
    
label tower_of_life_flamia_fight:
    lyner "There's a door. I hope it opens..."
    
    aurica_std "This is the door that can never be opened. It leads to the strong energies of the outside world..."
    
    lyner "Strong energies? Where does it go?"
    
    aurica_std "I don't know."
    
    fireball "Whoa! Look out! I sense something... I think it's..."
    
    lyner "A fire demon!?"
    
    fireball "...Here I come!"
    
    lyner "So is this his base?"
    
    flamia "Burning... burning... everyone is burning..."
    
    lyner "Damn! We have to take it down this time!"
    
    # choices: Defeat, Come back later
    
    # chose Defeat
    lyner "Let me handle this!"
    
    flamia "You can't get me!"
    
    lyner "(What do I do? This is Aurica's world...)"
    lyner "...That's it! This is Aurica's world!"
    lyner "Can you make those feathery things again?"
    
    aurica_std "You mean... the Fire Guard? Yes, I can make some more..."
    
    lyner "Great! Okay, seal his fire with one of those. I'll take him down while you guard me!"
    
    aurica_std "But... you'll..."
    
    lyner "Don't worry about me. I'm invincible, remember? Or, don't you trust me anymore?"
    
    aurica_std "..."
    aurica_std "No, you're right. You are invincible. I believe you'll defeat that fire demon..."
    
    lyner "Alright! Here it comes! Aurica, don't worry. Have faith in me!"
    
    aurica_std "I do."
    aurica_std "Huh!?"
    
    fire_guard "Was granme gaya khal yor elle fayra"
    
    lyner "Okay! Here goes!"
    lyner "Urah!"
    
    flamia "Ugh!"
    
    aurica_std "...Did you get it?"
    
    lyner "Of course I did. That was easy!"
    
    aurica_std "That's because you're so talented."
    
    lyner "No, it was because of you, Aurica. You are talented."
    
    aurica_std "...Me?"
    
    lyner "I was only able to beat it because you believed that I could."
    lyner "This is your world. Whatever you wish for will come true."
    
    aurica_std "...Are you sure?"
    
    lyner "What!? You're still alive?"
    
    flamia "Don't worry. I won't attack anymore."
    
    lyner "...Huh?"
    
    flamia "I decided to protect this land."
    
    lyner "Protect this land...? Aurica, did you...?"
    
    aurica_std "Yes. Now I know that I can change this world."
    aurica_std "I used to blame myself for being weak."
    aurica_std "But you made me realize that I was wrong."
    
    lyner "Well, this world should be peaceful from now on."
    
    aurica_std "Yes, it will."
    
    $ tower_of_life_saw_flamia_fight = True
    $ stonehenge_paradigm_shift_occurred = True
    
    jump map