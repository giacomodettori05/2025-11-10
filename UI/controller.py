

import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self.K = 0
        self.s = ""



    def handleCreaGrafo(self, e):
        grafo = self._model.crea_grafo(self.K, self.s)
        counter = 1
        self._view.txt_result.controls.clear()
        Archi = self._model.getTop3Archi()
        for i in Archi:
            if counter <=3:
                self._view.txt_result.controls.append(ft.Text(f"peso = {i[2]['weight']} dal nodo  {i[0].order_id} al {i[1].order_id}"))
                counter += 1
            else:
                counter = 1
                break


        self._view.txt_result.controls.append(ft.Text(f"numero nodi = {len(grafo.nodes)}"))
        self._view.txt_result.controls.append(ft.Text(f"numero archi = {len(grafo.edges)}"))

        e.page.update()


    def handleCerca(self, e):
        pass

    def handleRicorsione(self, e):
        pass

    def popola_dd(self, dd: ft.Dropdown()):

        stores = self._model.stores

        if dd.label == "Store":
            for s in stores:
                dd.options.append(ft.dropdown.Option(text=s.store_name,
                                             data=s,
                                             on_click=self.read_s))
    def read_s(self, e):
        s = e.control.data
        self.s = s.store_id
    def handleIntK(self, e):

        k = e.control.value
        try:
            self.K = int(k)
            self._view.txt_result.controls.clear()


        except ValueError:
            self._view.txt_result.controls.append(ft.Text(f"Devi mettere un numero intero valido!"))
        e.page.update()




