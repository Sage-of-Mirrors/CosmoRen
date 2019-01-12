define lyner = Character('Lyner', color="#a02000")
define unk_leon = Character('???', color="00FF00")
define leon = Character('Don Leon', color="FFFF00")
define aurica_std = Character('Aurica', color="FF00FF")
define fireball = Character('Fireball', color="FF00FF")
define aurica_agl = Character('Angel Aurica', color="000050")

label stonehenge_start:
    scene bg stonehenge bright at truecenter
    
    if not stonehenge_saw_intro:
        jump stonehenge_intro
    
    if stonehenge_paradigm_shift_occurred:
        jump stonehenge_paradigm_shift
        
    if not stonehenge_saw_stonehenge_explanation:
        jump stonehenge_explanation
        
    jump stonehenge_none
        
label stonehenge_none:
    "There's nothing here..."
    
    scene bg black with dissolve
    
    jump map

label stonehenge_intro:
    lyner "This is Aurica's Soulspace? It looks peaceful enough..."
    lyner "..."
    lyner "But I don't feel very welcome here. Maybe it's just me..."
    
    # screen shake
    
    lyner "Hey! Oww!"
    
    unk_leon "Scoundrel! Who do you think you are, barging in here without permission? Identify yourself!"
    
    lyner "Wait, who are you? Oww!"
    
    # screen shake
    
    unk_leon "Scoundrel! How rude! You should give your name before requesting mine!"
    
    lyner "Okay, okay. I'm Lyner Barsett."
    
    unk_leon "And I am Don Leon, the royal knight of Aurica's mind."
    
    lyner "Knight? So, you're the Mind Guardian?"
    
    leon "Si. I am here to protect Aurica. You'll have no funny business, as long as I am here."
    
    lyner "That's fine. I'm not here to screw around. Hey... what kind of name is Don Leon...?"
    
    # screen shake
    
    leon "How dare you! Aurica gave me my name! I demand satisfaction... or an apology..."
    
    lyner "Okay, I admit I was wrong. I'm sorry."
    
    leon "I shall forgive you this once. So, what business do you have in Aurica's world?"
    
    lyner "I'm here for Song Magic."
    
    leon "Song Magic, you say? Aurica would never craft Song Magic with a weirdo like you!"
    
    leon "But, you have come all this way. Know that I do not trust you..."
    
    leon "I shall be keeping a close eye on you. That, you must never forget!"
    
    lyner "Alright, I get it, sheesh..."
    
    leon "(This one... will not be fun...)"
    
    $ stonehenge_saw_intro = True
    
    jump map
    
label stonehenge_explanation:
    leon "Aurica isn't here. Or are you going home already?"
    
    lyner "That's not it... I was a little curious when I came here. What are these ruins?"
    
    leon "This ruin is called the Stonehenge. It's a very important facility for Aurica's development!"
    
    lyner "I... I see..."
    
    leon "Indeed. When Aurica advances from this world, she borrows powers from this Stonehenge."
    leon "You will understand when the time comes, if you're able to support Aurica and cause the Paradigm Shift to occur."
    
    $ stonehenge_saw_stonehenge_explanation = True
    
    jump map
    
label stonehenge_paradigm_shift:
    lyner "This is..."
    
    fireball "Hey, I see someone in the light!"
    
    lyner "...Aurica?"
    
    aurica_std "I... I see myself..."
    
    aurica_agl "Did you pass through the Paradigm Shift?"
    
    lyner "Huh? What's going on? Are you Aurica?"
    
    aurica_agl "I am Aurica. But you haven't met me before."
    
    lyner "...?"
    
    aurica_agl "Aurica, jump in there. It's a step toward spiritual growth."
    
    aurica_std "Spiritual growth...?"
    
    aurica_agl "Yes. This Stonehenge is an altar for growing spiritually."
    
    aurica_agl "You need to grow. Every time you step into this light, you'll be a step closer to enlightenment."
    
    lyner "Aurica..."
    
    aurica_std "Yes."
    
    aurica_std "Thank you. For everything."
    
    lyner "Don't mention it."
    
    aurica_std "Will I see you again?"
    
    lyner "Of course."
    
    aurica_std "Then, I'm going..."
    
    scene bg white at truecenter with Dissolve(0.5)