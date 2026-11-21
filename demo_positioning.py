from manim import *
from numpy import square

class demo(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        circle.stroke_color = WHITE  # set the stroke color

        square = Square()  # create a square
        square.set_fill(BLUE, opacity=0.5)  # set the color and transparency
        square.stroke_color = WHITE  # set the stroke color

        self.play(Create(circle), Create(square))  # animate the creation of both shapes
        self.wait(4)  # wait for a second

        self.play(circle.animate.shift(LEFT*2), square.animate.shift(RIGHT*2))  # animate the movement of both shapes
        
        circle_text = Text("Circle").next_to(circle, DOWN, buff=0.5)
        square_text = Text("Square").next_to(square, DOWN, buff=0.5)
        self.play(Write(circle_text), Write(square_text))

        self.wait(4)  # wait for a second
        