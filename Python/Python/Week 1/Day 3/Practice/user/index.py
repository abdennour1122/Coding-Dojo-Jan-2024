class user:
    def __init__(self, first_name, last_name, email,age):
        self.first_name = first_name
        self.last_name =last_name
        self.email = email
        self.age = age
    
    def display_info(self):
        print(f"first_name: {self.first_name},last_name:{self.last_name},email:{self.email},age:{self.age}")

        return self

User1=user("abdennour","ayedi","a@.com",19)
User1.display_info()