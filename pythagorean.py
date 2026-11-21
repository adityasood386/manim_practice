from manim import *

class PythagoreanProof(Scene):
    def construct(self):
        # Signature 3Blue1Brown-style dark charcoal background
        self.camera.background_color = "#141414"

        # Side lengths of the right triangle (a + b = 4.0)
        a = 1.5
        b = 2.5
        L = a + b
        half = L / 2
        offset = LEFT * 2.0  # Shift diagram left to leave room for equations on the right

        # 1. Title
        title = Text("Aditya Sood", font_size=40, color=WHITE).to_edge(UP, buff=0.4)
        self.play(Write(title))

        # 2. Outer framing square of side (a + b)
        outer_square = Square(side_length=L, color=WHITE, stroke_width=3).shift(offset)

        # 3. Four congruent right triangles (legs a and b, hypotenuse c)
        def make_tri(p1, p2, p3):
            return Polygon(
                p1, p2, p3,
                color=BLUE_B,
                fill_color=BLUE_D,
                fill_opacity=0.85,
                stroke_width=2
            ).shift(offset)

        # Bottom-left, bottom-right, top-right, top-left
        t1 = make_tri([-half, -half, 0], [-half + b, -half, 0], [-half, -half + a, 0])
        t2 = make_tri([half, -half, 0], [half, -half + b, 0], [half - a, -half, 0])
        t3 = make_tri([half, half, 0], [half - b, half, 0], [half, half - a, 0])
        t4 = make_tri([-half, half, 0], [-half, half - b, 0], [-half + a, half, 0])

        triangles = VGroup(t1, t2, t3, t4)

        # 4. Inner tilted square (Area = c²)
        c_square = Polygon(
            [-half + b, -half, 0],
            [half, -half + b, 0],
            [half - b, half, 0],
            [-half, half - b, 0],
            color=YELLOW,
            fill_color=YELLOW,
            fill_opacity=0.25,
            stroke_width=3
        ).shift(offset)

        c_label = Text("c²", font_size=44, color=YELLOW).move_to(c_square.get_center())

        # Animate initial setup
        self.play(Create(outer_square), run_time=1)
        self.play(LaggedStart(*[FadeIn(t, scale=0.9) for t in triangles], lag_ratio=0.15))
        self.play(FadeIn(c_square), Write(c_label))
        self.wait(1)

        # Show "c²" on the right side as the start of our equation
        eq_c = Text("c²", font_size=52, color=YELLOW).shift(RIGHT * 2.3)
        self.play(TransformFromCopy(c_label, eq_c))
        self.wait(0.8)

        # 5. Fade out c² highlight and slide triangles into two rectangles
        self.play(FadeOut(c_square), FadeOut(c_label))

        # Slide top-right triangle (t3) down-left to pair with t1
        self.play(t3.animate.shift(LEFT * a + DOWN * b), run_time=1.4, rate_func=smooth)
        # Slide top-left triangle (t4) down-right to pair with t2
        self.play(t4.animate.shift(RIGHT * b + DOWN * a), run_time=1.4, rate_func=smooth)
        self.wait(0.5)

        # 6. Highlight the two newly formed empty squares: b² and a²
        b_square = Square(
            side_length=b,
            color=TEAL,
            fill_color=TEAL,
            fill_opacity=0.3,
            stroke_width=3
        ).move_to([-half + b / 2, half - b / 2, 0] + offset)

        a_square = Square(
            side_length=a,
            color=MAROON_B,
            fill_color=MAROON_B,
            fill_opacity=0.3,
            stroke_width=3
        ).move_to([half - a / 2, half - a / 2, 0] + offset)

        b_label = Text("b²", font_size=44, color=TEAL).move_to(b_square.get_center())
        a_label = Text("a²", font_size=40, color=MAROON_B).move_to(a_square.get_center())

        self.play(FadeIn(a_square), Write(a_label), FadeIn(b_square), Write(b_label))
        self.wait(0.8)

        # 7. Complete the equation: c² = a² + b²
        eq_rest = Text(" = a² + b²", font_size=52, color=WHITE).next_to(eq_c, RIGHT, buff=0.15)
        eq_rest[1:3].set_color(MAROON_B)  # color a²
        eq_rest[4:6].set_color(TEAL)      # color b²

        self.play(Write(eq_rest))

        # Final highlight box around the theorem
        full_eq = VGroup(eq_c, eq_rest)
        box = SurroundingRectangle(full_eq, color=GOLD, buff=0.25, corner_radius=0.1)
        self.play(Create(box))
        self.wait(2.5)