from manim import *

class NameAnimation(Scene):
    def construct(self):
        # 1. Create the name with a color gradient
        name = Text("Aditya Sood", font_size=96, weight=BOLD)
        name.set_color_by_gradient(BLUE, PURPLE, PINK)

        # 2. Create a matching underline below the name
        underline = Line(LEFT, RIGHT)
        underline.match_width(name)
        underline.next_to(name, DOWN, buff=0.25)
        underline.set_color_by_gradient(BLUE, PURPLE, PINK)

        # 3. Animate!
        self.play(Write(name), run_time=2)
        self.play(Create(underline), run_time=0.8)
        self.play(Indicate(name, scale_factor=1.08, color=WHITE), run_time=0.8)
        self.wait(1.5)

        # 4. Clean exit
        self.play(FadeOut(name, shift=UP), FadeOut(underline, shift=DOWN))
        self.wait(0.5)