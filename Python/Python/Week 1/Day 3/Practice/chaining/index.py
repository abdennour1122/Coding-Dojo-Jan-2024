class user:
    def __init__(self, first_name, last_name, email,age,rewards_member=False,gold_card_points=0):
        self.first_name = first_name
        self.last_name =last_name
        self.email = email
        self.age = age
        self.rewards_member= rewards_member
        self.gold_card_points= gold_card_points
        
        
        
    
    def display_info(self):
        print(f"first_name: {self.first_name},last_name:{self.last_name},email:{self.email},age:{self.age},is a {self.rewards_member},and {self.gold_card_points}")

        return self

    def enroll(self):
        self.rewards_member=True
        self.gold_card_points=200
    
  
    def spend_points(self,amount):
        self.gold_card_points-=amount
        print(f"and the amount is {self.gold_card_points}")

User1=user("abdennour","ayedi","a@.com",19,)
User1.display_info().enroll().spend_points(50).display_info()
