



class Customers:
    def __init__(self, name: str, e_mail : str, phone_num : str) ->None:
        self.name = name
        self.e_mail = e_mail
        self.phone_num = phone_num
        
    def __str__(self) -> str:
        return f'{self.name} ({self.e_mail}) {self.phone_num} '