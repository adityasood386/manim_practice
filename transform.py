from manim import *

# class circle_to_square(Scene):
#     def construct(self):
#         circle = Circle()  # create a circle
#         square = Square()  # create a square
#         self.play(Create(circle))  # show the circle on screen
#         self.wait(4)  # wait for a second
#         self.play(Transform(circle, square))  # transform the circle into a square
#         self.wait(4)  # wait for a second

class circle_to_square(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set color and transparency

        square = Square()  # create a square
        square.rotate(PI / 4)  # rotate a certain amount
        self.play(Create(square))  # animate the creation of the square
        self.wait(4)  # wait for a second
        self.play(Transform(square, circle))  # interpolate the square into the circle
        self.wait(4)  # wait for a second
        self.play(FadeOut(square))  # fade out animation