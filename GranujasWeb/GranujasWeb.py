import reflex as rx
import random

from rxconfig import config

class State(rx.State):
    docho: int = 0
    dveinte: int =0
    bono3: int = 0
    bono2: int  = 0
    bono2plus: int = 0
    lugar3: int =0
    lugar2: int=0
    list_caract  = ["FUE","DES","CON","INT","SAB","CAR"]
    list_bonos = [1,1,1,1,1,1]
    def dadoveinte(self):
        self.dveinte =random.randint(1, 20)
    def dadoocho(self):
        self.docho =random.randint(1, 8)
    def tiraCAR(self):
        for i in range (0,6):
            self.list_bonos[i] = 1
        bono3 = random.randint(0, 5)
        self.list_bonos[bono3] =  3
        lugar3 = bono3   
        bono2 = random.randint(0, 5)
        while bono2 == lugar3:
            bono2 = random.randint(0, 5)
        self.list_bonos[bono2] =  2
        lugar2 = bono2
        bono2plus = random.randint(0, 5)
        while (bono2plus == lugar2) or (bono2plus == lugar3):
            bono2plus = random.randint(0, 5)
        self.list_bonos[bono2plus] =  2


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Creador de personajes para Granujas RPG", size="8"),
            rx.button("Tira Características",color_scheme="green",on_click=State.tiraCAR),
            spacing="5",
            justify="center",
            min_height="10vh",
        ),
        rx.vstack(
            rx.heading(State.list_caract[0]," [+",State.list_bonos[0],"]"," Defensa:",State.list_bonos[0]+10,font_size="1.5em"),
            rx.heading(State.list_caract[1]," [+",State.list_bonos[1],"]"," Defensa:",State.list_bonos[1]+10,font_size="1.5em"),
            rx.heading(State.list_caract[2]," [+",State.list_bonos[2],"]"," Defensa:",State.list_bonos[2]+10,font_size="1.5em"),
            rx.heading(State.list_caract[3]," [+",State.list_bonos[3],"]"," Defensa:",State.list_bonos[3]+10,font_size="1.5em"),
            rx.heading(State.list_caract[4]," [+",State.list_bonos[4],"]"," Defensa:",State.list_bonos[4]+10,font_size="1.5em"),
            rx.heading(State.list_caract[5]," [+",State.list_bonos[5],"]"," Defensa:",State.list_bonos[5]+10,font_size="1.5em"),
            spacing="5",
            justify="center",
            min_height="25vh",
            align="end",
            width="80%",
        ),
        rx.vstack(
            rx.heading("Espacios de equipo: ",State.list_bonos[3]+10, font_size="2em"),
            rx.button("Tirar 1d20",color_scheme="yellow",on_click=State.dadoveinte),
            rx.heading(State.dveinte, font_size="2em"),
            rx.button("Tirar puntos de golpe (1d8)",color_scheme="red",on_click=State.dadoocho),
            rx.heading(State.docho, font_size="2em"),
            spacing="5",
            justify="center",
            min_height="35vh",
        ),
        rx.dialog.root(
    rx.dialog.trigger(rx.button("Guía paso a paso")),
    rx.dialog.content(
        rx.dialog.title("Como crear tu personaje:"),
        rx.dialog.description(
            rx.list.item("Reparte los siguientes bonos: (+3), (+2), (+2), (+1), (+1) y (+1)"),
            rx.list.item("de forma aleatoria entre las distintas características:",list_style_type="none"),
            rx.list.item(rx.text.strong("FUE DES CON INT SAB CAR"),list_style_type="none"),
            rx.list.item(rx.text.kbd("Puedes intercambiar dos de los valores si así lo deseas."),list_style_type="none"),
            rx.list.item("Suma 10 a cada bono para conseguir su",rx.text.strong(" Defensa.")),
            rx.list.item("Elige una", rx.text.strong(" Raza "), "en la página 5."),
            rx.list.item("Empiezas con una semana de", rx.text.strong(" raciones.")),
            rx.list.item("Selecciona un ",rx.text.strong("arma "), "en la página 8."),
            rx.list.item("Tira 1d20 para el ", rx.text.strong(" equipo inicial "), "en la página 4."),
            rx.list.item("- Tira para la armadura y mira sus estadísticas en la página 8.",list_style_type="none"),
            rx.list.item("- Sin armadura es 11+ (1/2 bono de DES) redondeando arriba.",list_style_type="none"),
            rx.list.item("- Tira dos veces para el equipo de mazmorreo.",list_style_type="none"),
            rx.list.item("- Tira una vez en las tablas de equipo general 1 y 2.",list_style_type="none"),
            rx.list.item("Tienes tantos ", rx.text.strong("espacios de equipo ")," como Defensa de CON."),
            rx.list.item("Tira 1d8 para determinar los ", rx.text.strong(" puntos de golpe "),"máximos."),
            rx.list.item("Tu velocidad de exploración es 120 pies / 36m."),
            rx.list.item("Tu velocidad en combate es 40 pies / 12m."),
            rx.list.item("Elige una ",rx.text.strong("habilidad de aventurero "),"en la página 10."),
            rx.list.item(rx.text.kbd("Puedes renunciar a esta habilidad para poner los PG Máx. a 8."),list_style_type="none"),
            rx.list.item("Elige o tira para determinar los ",rx.text.strong(" Rasgos "),"en la página 3."),
            
        ),
        rx.dialog.close(
            rx.button("Cerrar la guía", size="3"),
        ),
    ),
)
    )

'''Levantar la web'''
app = rx.App()
app.add_page(index)
