from manim import *

class DecodificarMensaje(Scene):
    def construct(self):
        # Título
        titulo = Text("Decodificación de Mensaje", font_size=48)
        self.play(Write(titulo))
        self.wait(2)
        self.play(FadeOut(titulo))
        
        # Paso 1: Mostrar el mensaje codificado
        mensaje_codificado = "oyekaijzdf aaptcg suaokybhai ouow aqht mynznvaatzacdfoulxxz"
        texto_codificado = Text("Mensaje Codificado:", font_size=36).to_edge(UP)
        texto_mensaje = Text(mensaje_codificado, font_size=24).next_to(texto_codificado, DOWN)
        self.play(Write(texto_codificado))
        self.play(Write(texto_mensaje))
        self.wait(3)
        
        # Paso 2: División en palabras y pares
        self.play(FadeOut(texto_codificado), FadeOut(texto_mensaje))
        division_text = Text("Paso 1: División en Palabras y Pares de Letras", font_size=36).to_edge(UP)
        self.play(Write(division_text))
        
        palabras = ["oyekaijzdf", "aaptcg", "suaokybhai", "ouow", "aqht", "mynznvaatzacdfoulxxz"]
        palabras_tex = VGroup(*[
            Text(palabra, font_size=24) for palabra in palabras
        ]).arrange(DOWN, aligned_edge=LEFT).next_to(division_text, DOWN, buff=1)
        self.play(Write(palabras_tex))
        self.wait(2)
        
        # Separar en pares
        pares = [
            ["oy", "ek", "ai", "jz", "df"],
            ["aa", "pt", "cg"],
            ["su", "ao", "ky", "bh", "ai"],
            ["ou", "ow"],
            ["aq", "ht"],
            ["my", "nz", "nv", "aa", "tz", "ac", "df", "ou", "lx", "xz"]
        ]
        
        # Animación de separación en pares
        for i, palabra in enumerate(palabras_tex):
            pares_palabra = pares[i]
            grupo_pares = VGroup(*[
                Text(par, font_size=24, color=BLUE) for par in pares_palabra
            ]).arrange(RIGHT, buff=0.2).next_to(palabra, DOWN, buff=0.5)
            self.play(Write(grupo_pares))
            self.wait(1)
        
        self.wait(2)
        self.play(FadeOut(division_text), FadeOut(palabras_tex))
        
        # Paso 3: Asignación de valores numéricos a cada letra
        asignacion_text = Text("Paso 2: Asignación de Valores Numéricos", font_size=36).to_edge(UP)
        self.play(Write(asignacion_text))
        
        # Tabla de valores alfabéticos
        tabla = Table(
            [["A", "1"], ["B", "2"], ["C", "3"], ["D", "4"], ["E", "5"], ["F", "6"],
             ["G", "7"], ["H", "8"], ["I", "9"], ["J", "10"], ["K", "11"], ["L", "12"],
             ["M", "13"], ["N", "14"], ["O", "15"], ["P", "16"], ["Q", "17"], ["R", "18"],
             ["S", "19"], ["T", "20"], ["U", "21"], ["V", "22"], ["W", "23"], ["X", "24"],
             ["Y", "25"], ["Z", "26"]],
            include_outer_lines=True
        ).scale(0.5).to_edge(DOWN)
        
        self.play(Create(tabla))
        self.wait(2)
        
        # Explicación breve
        explicacion = Text(
            "Cada letra se asigna a su posición en el alfabeto.\nLuego, para cada par, se suman los valores.",
            font_size=24
        ).next_to(tabla, UP, buff=0.5)
        self.play(Write(explicacion))
        self.wait(3)
        
        self.play(FadeOut(asignacion_text), FadeOut(tabla), FadeOut(explicacion))
        
        # Paso 4: Cálculo del valor original de cada letra
        calculo_text = Text("Paso 3: Cálculo del Valor Original", font_size=36).to_edge(UP)
        self.play(Write(calculo_text))
        
        # Ejemplo de un par: oy
        ejemplo_par = Text("Ejemplo: 'oy'", font_size=24).next_to(calculo_text, DOWN, buff=1)
        self.play(Write(ejemplo_par))
        self.wait(1)
        
        # Mostrar valores de 'o' y 'y'
        valor_o = Text("O = 15", font_size=24).next_to(ejemplo_par, DOWN, buff=0.5)
        valor_y = Text("Y = 25", font_size=24).next_to(valor_o, DOWN, buff=0.2)
        self.play(Write(valor_o), Write(valor_y))
        self.wait(1)
        
        # Suma de valores
        suma = Text("Suma: 15 + 25 = 40", font_size=24).next_to(valor_y, DOWN, buff=0.5)
        self.play(Write(suma))
        self.wait(1)
        
        # División por 2
        division = Text("Dividir por 2: 40 / 2 = 20", font_size=24).next_to(suma, DOWN, buff=0.5)
        self.play(Write(division))
        self.wait(1)
        
        # Obtener la letra original
        letra_original = Text("Letra Original: T (20)", font_size=24).next_to(division, DOWN, buff=0.5)
        self.play(Write(letra_original))
        self.wait(2)
        
        self.play(FadeOut(calculo_text), FadeOut(ejemplo_par),
                  FadeOut(valor_o), FadeOut(valor_y),
                  FadeOut(suma), FadeOut(division),
                  FadeOut(letra_original))
        
        # Mostrar todo el proceso para una palabra completa
        proceso_text = Text("Aplicando el Proceso a Todo el Mensaje", font_size=36).to_edge(UP)
        self.play(Write(proceso_text))
        
        # Repetir para cada palabra y par
        palabras_decodificadas = ["THERE", "ARE", "THREE", "R'S", "IN", "STRAWBERRY"]
        for i, palabra in enumerate(palabras_tex):
            pares_palabra = pares[i]
            palabra_decodificada = Text(palabras_decodificadas[i], font_size=24, color=GREEN).next_to(palabra, RIGHT, buff=1)
            
            # Crear objetos Text para cada par
            pares_texto = [Text(par, font_size=24) for par in pares_palabra]
            grupo_pares = VGroup(*pares_texto).arrange(RIGHT, buff=0.2).next_to(palabra, DOWN, buff=0.5)
            
            self.add(grupo_pares)
            
            for par_texto in pares_texto:
                self.play(
                    par_texto.animate.set_color(YELLOW),
                    run_time=0.5
                )
                self.wait(0.5)
            self.play(Write(palabra_decodificada))
            self.wait(1)
        
        self.wait(2)
        self.play(
            FadeOut(proceso_text),
            FadeOut(palabras_tex),
            *[FadeOut(Texto) for Texto in self.mobjects if isinstance(Texto, Text)]
        )
        
        # Paso 5: Mensaje Decodificado
        final_text = Text("Mensaje Decodificado:", font_size=36).to_edge(UP)
        mensaje_final = Text("THERE ARE THREE R'S IN STRAWBERRY", font_size=36, color=GREEN).next_to(final_text, DOWN, buff=1)
        self.play(Write(final_text))
        self.play(Write(mensaje_final))
        self.wait(3)
        
        # Finalizar
        self.play(FadeOut(final_text), FadeOut(mensaje_final))
        cierre = Text("¡Decodificación Completa!", font_size=36)
        self.play(Write(cierre))
        self.wait(2)

