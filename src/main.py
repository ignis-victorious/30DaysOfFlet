#
#  Import LIBRARIES
import flet as ft

#  Import FILES
# ...


#! The main function def main(page: ft.Page):
def main(page: ft.Page) -> None:
    page.title = "30 Days of Flet - 04. User Input"
    page.window.width = 1000  # ! Custom windo
    page.window.height = 500  # ! Custom windo

    # Getting user name
    name = ft.TextField(label="Your name", hint_text="Enter your name...")

    # * function to handle on click event
    def handle_on_click(event) -> None:
        name_value: str | None = name.value
        if name_value:
            event.text = f"Hi, {name_value.strip()}"

    # Creating simple buttons
    btn = ft.ElevatedButton(text="Click", on_click=handle_on_click)

    # page.add(row)
    page.add(name, btn)


# Run the UI
if __name__ == "__main__":
    ft.app(target=main)
