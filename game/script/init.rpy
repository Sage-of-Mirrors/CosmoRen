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
    
transform center_side:
    yalign 0.75
    xpos 240
    
transform mirror:
    xzoom -1.0
    
default stonehenge_saw_intro = False
default stonehenge_paradigm_shift_occurred = False
default stonehenge_saw_stonehenge_explanation = False

default inn_saw_jack_conversation = False
default inn_saw_aurica_conversation = False

default village_saw_first_visit = False
default village_saw_second_visit = False

default tower_of_life_saw_flamia_fight = False

label start:
    if not stonehenge_saw_intro:
        jump stonehenge_start
        
    jump map