define jack = Character('Jack', color="008000")

label inn_start:
    scene bg elemia inn at truecenter
    
    if village_saw_first_visit and not inn_saw_aurica_conversation:
        jump inn_aurica_conversation
    
    if not inn_saw_jack_conversation:
        jump inn_jack_conversation
        
    jump inn_none
    
label inn_none:
    "There's nothing here..."
    
    scene bg black with dissolve
    
    jump map
    
label inn_jack_conversation:
    show jack disinterest at center with dissolve
    jack "Hey, you're..."
    
    lyner "You're Jack! I didn't think you'd be here."
    
    jack "Keh... I ain't here 'cause I want to be!"
    
    lyner "Oh? Then why are you here?"
    
    show jack yelling at center
    
    jack "That's my own business! Why the hell do I have to tell you? Huh? Why?"
    
    lyner "Uh, I don't need to know that badly! Hahaha..."
    lyner "(Jack is really scary today!)"
    lyner "(...Oh yeah. This Jack is the image of how Aurica sees him. So, Jack is a scary person to Aurica, I guess...)"
    
    show jack disinterest at center
    
    jack "I mean, why the hell do I have to be in the world of this little girl?"
    jack "Ugh... I'd rather be in the Cosmosphere of a gorgeous lady, like Miss Claire. Staying here is lame!"
    
    lyner "(Aurica... Were you listening to our whole conversation at the Inn in Nemo?)"
    
    $ inn_saw_jack_conversation = True
    
    hide jack disinterest with dissolve
    
    jump map
    
label inn_aurica_conversation:
    show aurica std gasp at center_side
    
    aurica_std "Y-you!?"
    
    lyner "I'm Lyner Barsett. I came here so that you can craft a song."
    
    aurica_std "...A song? I can't craft a song. I'm not powerful enough..."
    
    lyner "I don't think so... besides, this is your world. You should be able to create anything you want."
    
    aurica_std "It's not that easy for me. I can't even save my own village..."
    show aurica std grimace at center_side
    aurica_std "This village has been destroyed many times by the Fire Demon. Radolf, who lives in this village, thinks I'm summoning the Fire Demon."
    
    lyner "Wh-what? Why would he think that?"
    
    show aurica std sad at center_side
    
    aurica_std "Unfortunately, he's probably right. This village has been burned down many times in the past... because of me."
    show aurica std smile sad at center_side
    aurica_std "Radolf always rebuilds the village. He isn't friendly, but he's got a big heart."
    
    lyner "Huh? That sounds strange... Isn't this your world? Why can't you restore the village?"
    lyner "You should be able to do anything... including stopping that demon..."
    
    show aurica std gasp at center_side
    
    aurica_std "I can't do that! I would only destroy this village."
    
    lyner "(Sounds like she has post-traumatic stress...)"
    lyner "Let's defeat this Fire Demon first. This is your world, so you know how to defeat him, right?"
    
    aurica_std "..."
    
    lyner "You don't know? Then how did you create it?"
    
    aurica_std "I don't know. The demon always appears out of nowhere, destroys things, and then leaves..."
    
    lyner "This is gonna be tough... I guess we have no choice but to defeat it. Can you craft Song Magic to defeat it?"
    
    show aurica std grimace at center_side
    
    aurica_std "No. I don't want to make anything. People always laught at my creations..."
    
    lyner "...laugh? Why?"
    
    show aurica std sad at center_side
    
    aurica_std "It's because I'm stupid. I can only create strange things, and I'm so weak..."
    
    lyner "Can you give it a shot? Please?"
    
    aurica_std "...I'm really weak, though."
    
    lyner "I don't care."
    
    show aurica std gasp at center_side
    
    aurica_std "You'll laugh at me."
    
    lyner "No, I won't."
    
    aurica_std "We can't beat that Fire Demon..."
    
    lyner "Don't worry about a thing! Just trust me and make something!"
    
    aurica_std "Okay..."
    
    hide aurica std gasp with dissolve
    
    aurica_std "I'll do it..."
    aurica_std "Huh!!"
    
    show bg white at truecenter with dissolve
    
    show fireball wait at right_side_2
    
    show bg elemia inn at truecenter with dissolve
    
    lyner "You did it!"

    hide fireball wait with dissolve
    
    show aurica std sad at center_side with dissolve
    
    aurica_std "I'm sorry. I can only make useless things..."
    
    hide aurica std sad with dissolve
    
    show aurica std smile at left_side
    
    show fireball wait at right_side
    
    fireball "Excuse you! You crafted me! You can't call me useless!"
    
    aurica_std "It talks!?"
    
    fireball "Why are you surprised? You crafted me, thinking it would be cute if I could talk."
    
    show aurica std smile sincere at left_side
    
    aurica_std "I did... but I didn't expect it to really happen."
    
    lyner "Great! See, you can craft properly. I can't do this. You need to be more confident."
    lyner "This is your world. You can craft anything if you believe in yourself."
    
    show aurica std sad at center_side
    
    aurica_std "...Y-yes. But I can only craft silly magic."
    
    fireball "Don't call me \"Silly Magic!\" I decided to do my best to help you, since you did craft me."
    
    lyner "That fire ball is right. I think he'll be useful."
    lyner "We can grill meat with this thing. Powerful isn't always a good thing, right? We can't grill meat with a bomb."
    
    show aurica std smile sincere at left_side
    
    aurica_std "You're right."
    
    fireball "Wait a minute! I'm only good for grilling meat!? What an insult..."
    
    $ inn_saw_aurica_conversation = True
    
    hide aurica std sincere with dissolve
    hide fireball wait with dissolve
    
    scene bg black with dissolve
    
    jump map