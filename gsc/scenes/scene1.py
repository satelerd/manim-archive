from manim import Scene, Axes, Create, BLUE_C

class AxesScene(Scene):
    def construct(self):
        axes = Axes(
            x_range=[6, 13, 1],
            y_range=[9, 17, 1],
            axis_config={"color": BLUE_C},
        ).add_coordinates()
        
        self.wait(1)
        self.play(Create(axes), run_time=3)
        self.wait(1)