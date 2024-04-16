import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff

        self._page = page
        self._page.title = "Analizza vendite"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.DARK
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._dd_retailer = None
        self._dd_brand = None
        self._dd_anno = None
        self._read_retailer = None

    def load_interface(self):
        # title
        self._title = ft.Text("Analizza vendite", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW with some controls
        self._dd_anno = ft.Dropdown(label="anno")
        self._fill_anno()
        self._dd_brand = ft.Dropdown(label="brand")
        self._fill_brand()
        self._dd_retailer = ft.Dropdown(label = "retailer", on_click=self._read_retailer)
        self._fill_retailer()

        row1 = ft.Row([self._dd_anno, self._dd_brand, self._dd_retailer],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)
        ## row2
        self._btn_top_vendite = ft.ElevatedButton(text="Top vendite")
        self._btn_analizza_vendite = ft.ElevatedButton(text="Analizza vendite")
        row2 = ft.Row([self._btn_top_vendite, self._btn_analizza_vendite], alignment=ft.MainAxisAlignment.CENTER)

        self._page.controls.append(row2)

        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()

    def _fill_anno(self):
        lista = self._controller.fill_anno()
        self._dd_anno.options.append(ft.dropdown.Option(text="Nessun filtro"))
        for i in lista:
            self._dd_anno.options.append(ft.dropdown.Option(text = i))

    def _fill_brand(self):
        lista = self._controller.fill_brand()
        self._dd_brand.options.append(ft.dropdown.Option(text="Nessun filtro"))
        for i in lista:
            self._dd_brand.options.append(ft.dropdown.Option(text=i))

    def _fill_retailer(self):
        lista = self._controller._model._diz_retailers.values()
        self._dd_retailer.options.append(ft.dropdown.Option(text="Nessun filtro"))
        for i in lista:
            self._dd_retailer.options.append(ft.dropdown.Option(key=i.retailer_code, text=i.retailer_name, data=i, on_click=self.read_retailer))

    def read_retailer(self, e):
        retailer = e.control.data
