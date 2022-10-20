import arcade

#Adding a library to a project
    #File --> Settings --> Project Name --> Python Interperator --> Hit + and add nessessary package

#Import statements
    #import <package>
    #from <package> import <thing>
    #IMPORT FILE BEFORE YOU USE THE THING -- IMPORT AT TOP OF FILE!!


my_window = arcade.open_window(1000, 900, "Graph Paper")
arcade.set_background_color(arcade.color.SILVER)

arcade.start_render()
#All other drawing goes here
for xloc in range(50, 1000, 50):
    arcade.draw_line(xloc, 50, xloc, 800, arcade.color.JET, 5)
for yloc in range(50, 900, 50):
    arcade.draw_line(50, yloc, 900, yloc, arcade.color.JET, 5)

arcade.finish_render()

arcade.run() #() Are important or else it will open and close immediately after

#To change the background color there are many ways to do so |RGB, HSV, HSL ect
# BUT arcade has many colors already defined using -set.background_color(arcade.color.COLOR)

#Lines (Put between start and finish)
    #Arcade.draw_line to draw a single line
        #Arcade.draw_line(Start x, start y x, end x, end y, color, line width)