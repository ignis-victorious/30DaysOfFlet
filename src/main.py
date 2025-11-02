#
#  Import LIBRARIES
import flet as ft

#  Import FILES
# ...


#! The main function def main(page: ft.Page):
def main(page: ft.Page) -> None:
    page.title = "30 Days of Flet - 03. Layout: Rows & Columns"

    # & Icon control
    icon = ft.Icon(name=ft.Icons.LINK_OUTLINED, size=24, color="#FFFDD0")
    icon2 = ft.Icon(name=ft.Icons.EMAIL_OUTLINED, size=24, color="#4C8EFF")
    icon3 = ft.Icon(name=ft.Icons.PLACE_OUTLINED, size=24, color="#4C8EFF")

    # & Text control
    text = ft.Text(value="github.com/coderadi-in", size=16, color="#FFFDD0")
    text2 = ft.Text(value="coder.adi.dev@gmail.com", size=16, color="#FFFFFF")
    text3 = ft.Text(value="India", size=16, color="#FFFFFF")

    link_ui = ft.Row(controls=[icon, text], spacing=10)
    email_ui = ft.Row(controls=[icon2, text2], spacing=10)
    place_ui = ft.Row(controls=[icon3, text3], spacing=10)

    # row = ft.Row(controls=[email_ui, place_ui, link_ui], spacing=10)
    column = ft.Column(controls=[email_ui, place_ui, link_ui], spacing=10)

    # page.add(row)
    page.add(column)


# Run the UI
if __name__ == "__main__":
    ft.app(target=main)
