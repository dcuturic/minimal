import flet as ft

def create_changelog_generator_component(page: ft.Page):
    return ft.Column(
        controls=[
            ft.Text("Changelog Generator", size=24, weight=ft.FontWeight.BOLD),
            ft.Text("This is the Changelog Generator component."),
        ]
    )
