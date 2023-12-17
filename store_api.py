from base_request import BaseApi

class StoreApi(BaseApi):
    endpoint = "store"

    def get_inventory(self):
        return self.send_request("get", f"{self.endpoint}/inventory")

    def place_order(self, order_data):
        return self.send_request("post", f"{self.endpoint}/order", data=order_data)

    def get_order_by_id(self, order_id):
        return self.send_request("get", f"{self.endpoint}/order/{order_id}")

    def delete_order(self, order_id):
        return self.send_request("delete", f"{self.endpoint}/order/{order_id}")
