from database.DB_connect import DBConnect
from model.order import Order

from model.store import Store


class DAO():
    @staticmethod
    def getAllStores():
        conn = DBConnect.get_connection()

        results = []

        cursor = conn.cursor(dictionary=True)
        query = "SELECT * from stores"

        cursor.execute(query)

        for row in cursor:
            results.append(Store(**row))

        cursor.close()
        conn.close()
        return results

    @staticmethod
    def getAllOrders(store_id):
        conn = DBConnect.get_connection()

        results = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT o.*, SUM(oi.quantity) as quantity
                    from  orders o, order_items oi 
                    where o.store_id = %s and o.order_id = oi.order_id 
                    group by o.order_id 
                    having SUM(oi.quantity)
                    """

        cursor.execute(query,(store_id,))

        for row in cursor:
            results.append(Order(**row))

        cursor.close()
        conn.close()
        return results