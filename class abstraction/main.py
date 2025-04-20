from abc import ABC, abstractmethod


class AuthSystem(ABC):
    def __init__(self, username):
        self.username = username

    @abstractmethod
    def authenticate(self, password):
        pass

    def greet_user(self):
        print(f"Welcome, {self.username}!")


class PasswordAuth(AuthSystem):
    def __init__(self, username, stored_password):
        super().__init__(username)
        self._stored_password = stored_password  # Protected attribute

    def authenticate(self, password):
        if password == self._stored_password:
            print("Authentication successful.")
        else:
            print("Authentication failed.")


user = PasswordAuth("johndoe", "secure@123")
user.authenticate("secure@123")
user.greet_user()
