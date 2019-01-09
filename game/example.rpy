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

    call screen map("example_map") with dissolve
    pause