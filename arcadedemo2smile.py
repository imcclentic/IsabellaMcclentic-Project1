import arcade

arcade.open_window(800, 800, "Smile")
arcade.set_background_color(arcade.color.DEEP_SPACE_SPARKLE)
arcade.start_render()
title = arcade.Text("Jack-o-lantern", 300, 600, arcade.color.PUMPKIN, 20)
arcade.draw_circle_filled(400, 400, 200, arcade.color.ORANGE)
arcade.draw_xywh_rectangle_filled(200, 580, 400, 50, arcade.color.BLACK)
arcade.draw_xywh_rectangle_filled(350, 630, 100, 100, arcade.color.BLACK)
arcade.draw_arc_filled(300, 450, 120, 150, arcade.color.BLACK, 0, 180)
arcade.draw_arc_filled(500, 450, 120, 150, arcade.color.BLACK, 0, 180)
arcade.draw_triangle_filled(375, 375, 425, 375, 400, 425, arcade.color.BLACK)
arcade.draw_arc_outline(400, 350, 250, 100, arcade.color.BLACK, -180, 0, 50)
title.draw()
arcade.finish_render()

arcade.run()

#drawing text - create a text object before start render
#arcade.text | text, start_x, start_y, color, font size (default 12), font.name='FONT', THEN draw it w/ my_text.draw

#Selection - using the keyword 'if'
    #if <condition>
    #boolean: is a way of saying a value can be either true of false (but nothing else)