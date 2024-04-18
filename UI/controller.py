from time import strftime

import flet as ft



class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._model.initialize()

    def handle_hello(self, e):
        name = self._view.txt_name.value
        if name is None or name == "":
            self._view.create_alert("Inserire il nome")
            return
        self._view.txt_result.controls.append(ft.Text(f"Hello, {name}!"))
        self._view.update_page()

    def fill_anno(self):
        return self._model._years
    def fill_brand(self):
        return self._model._product_brands

    def get_top_vendite(self, e):
        anno = self._view._dd_anno.value
        brand = self._view._dd_brand.value
        retailer = self._view._dd_retailer.value
        result = self._model.get_top_vendite(anno, brand, retailer)
        for i in result:
            self._view.txt_result.controls.append(ft.Text(f"Data: {i[0].strftime("%y-%m-%d")}; Ricavo: {i[1]}; Retailer: {i[3]}; Product: {i[3]}"))
        self._view.update_page()

    def get_analisi_vendite(self, e):
        anno = self._view._dd_anno.value
        brand = self._view._dd_brand.value
        retailer = self._view._dd_retailer.value
        result = self._model.get_analisi_vendite(anno, brand, retailer)
        for i in result:
            self._view.txt_result.controls.append(ft.Text(f"{i}"))
        self._view.update_page()
