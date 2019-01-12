define cloche = Character('Cloche', color="#0020ff")

transform left_side:
    yalign 0.5
    xpos -100
    
transform left_side_2:
    yalign 0.5
    xpos 0
    
transform right_side:
    yalign 0.5
    xpos 350
    
transform right_side_2:
    yalign 0.5
    xpos 200

label meadow_start:
    show bg black with fade
    
    scene bg meadow at truecenter with fade
    
    image cl_ye = im.Flip("images/portrait/cloche/cloche yelling.png", horizontal=True)
    image cl_sm = im.Flip("images/portrait/cloche/cloche seductive.png", horizontal=True)
    show cl_sm at left_side_2
    show cl_ye at left_side
    
    image in_fr = "images/portrait/infel/infel frown.png"
    image in_em = "images/portrait/infel/infel embarrassed.png"
    show in_em at right_side_2
    show in_fr at right_side
    
    cloche "give queen pls"
    infel "lolno"
    
    scene bg black with fade
    
    jump start