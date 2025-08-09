import requests
import flet as ft
from assets import get_temp



def main(page: ft.Page):
    page.title = "teste"
    page.theme_mode = "light"

    page.appbar = ft.AppBar(
        bgcolor=ft.Colors.BLUE_500,
        title=ft.Row([ft.Text("Aplicativo de clima", size=35, color="white")], alignment="center", expand=True)
    )
    layout2 = ft.Container(
        width=400,
        height=300,
        bgcolor=ft.Colors.BLUE_500,
        border_radius=5 ,
        expand=True,
        content=ft.Row([ft.Column([ft.Text("Nome: __", size=45, color="white"), ft.Text("Temperatura atual: ", color="white", size=20), ft.Text("Velocidade do vento: ", color="white", size=20), ft.Text("Úmidade: __", color="white", size=20)])], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
        padding=20
    )

    def btn_click(e):
        temps = get_temp.get_temp(city.value)
        wind_velocity = temps["wind"]["speed"]
        print(temps["main"]["temp"])
        temp = temps["main"]["temp"]
        umity = temps["main"]["humidity"]
        layout2.content.controls[0].controls[0].value = f"Nome: {city.value}"
        layout2.content.controls[0].controls[1].value = f"Temperatura atual: {temp}"
        layout2.content.controls[0].controls[2].value = f"Velocidade do vento: {wind_velocity}"
        layout2.content.controls[0].controls[3].value = f"Úmidade: {umity}"
        print(temps["weather"][0]["main"])
        if temps["weather"][0]["main"] == "Clear":
            del layout2.content.controls[1]
            layout2.content.controls.append(ft.Image(src="clear.png"))
            page.update()
        elif temps["weather"][0]["main"] == "Clouds":
            del layout2.content.controls[1]
            layout2.content.controls.append(ft.Image(src="cloud.png"))
            page.update()
        page.update()

    city = ft.TextField(label="ex, Nova York, Londres", border_radius=15,border_color="grey")
    layout1 = ft.Container(
        width=400,
        height=400,
        border_radius=10,
        content=ft.Column([ft.Text("Digite o nome de um CEP", size=25, weight="bold"), city, ft.ElevatedButton("Procurar", on_click=btn_click, bgcolor=ft.Colors.BLUE_500, elevation=0, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5)), color="white", width=400)], height=400, spacing=20)
    )
    page.add(ft.Row([layout1, layout2], spacing=200, vertical_alignment=ft.CrossAxisAlignment.START))

ft.app(main, assets_dir="assets")
