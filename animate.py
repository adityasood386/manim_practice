from manim import *

class demo(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        square = Square()  # create a square

        self.play(Create(square))  # animate the creation of both shapes

        self.wait(4)  # wait for a second

        self.play(square.animate.rotate(PI / 2))
        self.wait(2)  # wait for a second
        self.play(square.animate.flip(UP*2))
        self.wait(2)  # wait for a second
        self.play(square.animate.shift(LEFT*2))
        self.wait(2)  # wait for a second
        self.play(square.animate.shift(RIGHT*2))
        self.wait(2)  # wait for a second
        self.play(square.animate.shift(UP*2))
        self.wait(2)
        self.play(square.animate.shift(DOWN*2))
        self.wait(2)  # wait for a second

        self.wait(4)  # wait for a second

        self.play(Transform(square, circle))  # interpolate the square into the circle

        self.wait(4)  # wait for a second

        self.play(square.animate.set_fill(PINK, opacity=0.5))  # change the color and transparency of the square