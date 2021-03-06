# The two characters that will be speaking in this scene.
# They both use the color blue for their names.
define infel = Character('Infel', color="#0000ff")
define croix = Character('Croix', color="#0000ff")

# This character allows us to have Hymmnos text.
# It has no name, but you can create named versions
# as long as you set what_font to "fonts/hymmnos.ttf".
define hmns = Character(what_font="fonts/hymmnos.ttf")

# Ren'Py's execution begins at the start label
label start:
    
    call screen map("example_map")
    
    pause
    
    # Sets the background image. The image name is "bg stonehenge".
    # truecenter is the center of the screen both horizontally and vertically.
    scene bg stonehenge at truecenter
    

    
    # Displays Infel's smirking portrait.
    # Center is the center of the screen horizontally.
    show infel snarl at center
    
    infel "Alright, alright, good job. That's it. You can now go deeper into Cloche's mind."
    croix "Yeah."
    infel "It sounds easy, but it's not. The deeper you go, the harder it will be."
    infel "Just hope that you can keep up with it..."
    infel "Your true feelings will be tested the deeper you go in."
    infel "Can you really be Cloche's partner?"
    croix "...I can."
    
    show infel smile at center
    
    infel "Anyone could do it if it was only based on enthusiasm."
    infel "Well, let's just see how it goes. I'll just sit back and watch how much Cloche accepts you."
    croix "Do whatever you want."
    
    show infel smirk at center
    
    infel "Oh, I will, even if you don't insist. Anyway, you've completed Level 1."
    
    show infel smile at center
    
    infel "Congrats. Next time you dive, the world is gonna be at Level 2."
    
    show infel frown at center
    
    infel "The world might look exactly the same, or completely different. The only thing I can tell you is..."
    infel "The world is going to be more cruel than Level 1, without a doubt."
    croix "..."
    
    show infel smirk at center
    
    infel "If you think you're prepared for that, come back again."
    infel "Well then, goodbye for now. I'll see you again if it comes to it."
    croix "Yeah. See you later."
    
    # Fades away Infel
    hide infel smirk with Dissolve(0.3)
    
    # Fades in a black screen
    scene bg black at truecenter with dissolve
    
    # This text shows up in-game as Hymmnos because of the character.
    hmns "Ma num ra chs pic wasara mea,"
    hmns "en fwal sec mea."
    hmns "Was yea ra chs mea yor en fwal"
    hmns "en chs hymme."
    
    # This signals to Ren'Py that the game has ended
    return
    
label test_1:
    "test_1"
    
label test_2:
    "test_2"