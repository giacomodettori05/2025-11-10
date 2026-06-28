import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self.stores = DAO.getAllStores()
        self.orders = []
        self.grafo = nx.DiGraph()

    def handle_stores(self):
        return self.stores
    def handle_orders(self):
        return self.orders
    def crea_grafo(self, K, store_id):
        self.orders = DAO.getAllOrders(store_id)
        self.grafo.add_nodes_from(self.orders)
        lista_date = {}
        for i in self.orders:
            lista_date[i.order_date]=i
        for i in range(len(self.orders)):
            for j in range(i+1,len(self.orders)):
                data1 = self.orders[i].order_date
                data2 = self.orders[j].order_date
                if 0<(data2-data1).days <=K:
                    peso = (self.orders[i].quantity + self.orders[j].quantity)/(data2-data1).days
                    self.grafo.add_edge(self.orders[i], self.orders[j], weight=peso)
                elif 0< -(data2-data1).days <=K:
                    peso = (self.orders[i].quantity + self.orders[j].quantity) / -(data2-data1).days
                    self.grafo.add_edge(self.orders[j], self.orders[i], weight=peso)


        return self.grafo

    def getTop3Archi(self):
        return sorted(self.grafo.edges(data=True), key=lambda x: x[2].get('weight', 0), reverse=True)


