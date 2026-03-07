import reflex as rx


class CondState(rx.State):
    show: bool = True

    def change(self):
        self.show = not (self.show)

def login_button():
	return rx.vstack(
        rx.button(
            # The label changes based on the condition
            rx.cond(CondState.show, "Hide", "Show"),
            on_click=CondState.change,
        ),
        # The visibility of this text also changes
        rx.cond(
            CondState.show,
            rx.text("Login", color="blue"),
            rx.text("Account", color="red"),
        ),
    )
