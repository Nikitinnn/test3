from base_request import BaseApi

class UserApi(BaseApi):
    endpoint = "user"

    def create_user(self, user_data):
        return self.send_request("post", self.endpoint, data=user_data)

    def get_user_by_username(self, username):
        return self.send_request("get", f"{self.endpoint}/{username}")

    def update_user(self, username, updated_data):
        return self.send_request("put", f"{self.endpoint}/{username}", data=updated_data)

    def delete_user(self, username):
        return self.send_request("delete", f"{self.endpoint}/{username}")

