from manim import *
import numpy as np

class ScalingLawsScene(Scene):
    def construct(self):
        # Simulación de datos basada en las scaling laws del paper
        compute = np.logspace(7, 12, num=20)  # Presupuesto de cómputo de 1e7 a 1e12
        loss = 1e-2 * compute ** -0.2          # La pérdida disminuye como compute^-0.2
        features = 1e5 * compute ** 0.6        # Las características escalan como compute^0.6
        steps = 1e4 * compute ** 0.4            # Los pasos de entrenamiento escalan como compute^0.4

        # Convertir a escala logarítmica
        compute_log = np.log10(compute)
        loss_log = np.log10(loss)
        features_log = np.log10(features)
        steps_log = np.log10(steps)

        # Crear ejes para Pérdida vs. Cómputo
        axes_loss = Axes(
            x_range=[7, 12, 1],
            y_range=[-5, -2, 1],
            x_length=5,
            y_length=3,
            axis_config={"include_numbers": True},
            tips=False,
        )
        axes_loss.to_corner(UL)
        axes_loss_labels = VGroup(
            Text("Log Cómputo").scale(0.5).next_to(axes_loss.x_axis, RIGHT, buff=0.5),
            Text("Log Pérdida").scale(0.5).next_to(axes_loss.y_axis, UP, buff=0.5)
        )

        # Graficar Pérdida vs. Cómputo
        loss_dots = VGroup(*[
            Dot(axes_loss.coords_to_point(compute_log[i], loss_log[i]), radius=0.05, color=BLUE)
            for i in range(len(compute))
        ])
        # Línea de ajuste para Pérdida
        coeffs_loss = np.polyfit(compute_log, loss_log, 1)
        fit_line_loss = axes_loss.plot(
            lambda x: coeffs_loss[0]*x + coeffs_loss[1],
            x_range=[7, 12],
            color=RED
        )

        # Crear ejes para Características vs. Cómputo
        axes_features = Axes(
            x_range=[7, 12, 1],
            y_range=[5, 10, 1],
            x_length=5,
            y_length=3,
            axis_config={"include_numbers": True},
            tips=False,
        )
        axes_features.next_to(axes_loss, DOWN, buff=1)
        axes_features_labels = VGroup(
            Text("Log Cómputo").scale(0.5).next_to(axes_features.x_axis, RIGHT, buff=0.5),
            Text("Log Características").scale(0.5).next_to(axes_features.y_axis, UP, buff=0.5)
        )

        # Graficar Características vs. Cómputo
        features_dots = VGroup(*[
            Dot(axes_features.coords_to_point(compute_log[i], features_log[i]), radius=0.05, color=GREEN)
            for i in range(len(compute))
        ])
        # Línea de ajuste para Características
        coeffs_features = np.polyfit(compute_log, features_log, 1)
        fit_line_features = axes_features.plot(
            lambda x: coeffs_features[0]*x + coeffs_features[1],
            x_range=[7, 12],
            color=RED
        )

        # Crear ejes para Pasos vs. Cómputo
        axes_steps = Axes(
            x_range=[7, 12, 1],
            y_range=[4, 8, 1],
            x_length=5,
            y_length=3,
            axis_config={"include_numbers": True},
            tips=False,
        )
        axes_steps.next_to(axes_features, DOWN, buff=1)
        axes_steps_labels = VGroup(
            Text("Log Cómputo").scale(0.5).next_to(axes_steps.x_axis, RIGHT, buff=0.5),
            Text("Log Pasos").scale(0.5).next_to(axes_steps.y_axis, UP, buff=0.5)
        )

        # Graficar Pasos vs. Cómputo
        steps_dots = VGroup(*[
            Dot(axes_steps.coords_to_point(compute_log[i], steps_log[i]), radius=0.05, color=ORANGE)
            for i in range(len(compute))
        ])
        # Línea de ajuste para Pasos
        coeffs_steps = np.polyfit(compute_log, steps_log, 1)
        fit_line_steps = axes_steps.plot(
            lambda x: coeffs_steps[0]*x + coeffs_steps[1],
            x_range=[7, 12],
            color=RED
        )

        # Animar la creación de los ejes y etiquetas
        self.play(Create(axes_loss), Write(axes_loss_labels))
        self.wait(0.5)
        self.play(Create(axes_features), Write(axes_features_labels))
        self.wait(0.5)
        self.play(Create(axes_steps), Write(axes_steps_labels))
        self.wait()

        # Animar los puntos de Pérdida
        for dot in loss_dots:
            self.play(FadeIn(dot), run_time=0.05)
        self.wait()
        # Animar la línea de ajuste de Pérdida
        self.play(Create(fit_line_loss))
        equation_loss = Text("Pérdida ∝ Cómputo⁻⁰․²").scale(0.5).next_to(axes_loss, RIGHT)
        self.play(Write(equation_loss))
        self.wait()

        # Animar los puntos de Características
        for dot in features_dots:
            self.play(FadeIn(dot), run_time=0.05)
        self.wait()
        # Animar la línea de ajuste de Características
        self.play(Create(fit_line_features))
        equation_features = Text("Características ∝ Cómputo⁰․⁶").scale(0.5).next_to(axes_features, RIGHT)
        self.play(Write(equation_features))
        self.wait()

        # Animar los puntos de Pasos
        for dot in steps_dots:
            self.play(FadeIn(dot), run_time=0.05)
        self.wait()
        # Animar la línea de ajuste de Pasos
        self.play(Create(fit_line_steps))
        equation_steps = Text("Pasos ∝ Cómputo⁰․⁴").scale(0.5).next_to(axes_steps, RIGHT)
        self.play(Write(equation_steps))
        self.wait(2)

        # Añadir un título a la animación
        title = Text("Leyes de Escalado en Claude 3 Sonnet").scale(1.2)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(2)
