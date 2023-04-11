from ..models import Customers


def get_customer():
    try:
         with open('data\\customers.txt', 'r') as file_reader:
            return file_reader.read()

    except Exception as ex:
        print(f'Dogodila se greska {ex}')
        
        
def save_customers(customers : Customers):
        try:
            with open('data\\customers.txt', 'a') as file_writer:
                file_writer.write(str(customers) + '\n')
        except Exception as ex:
            print(f'Dogodila se greska {ex}')
            
def get_all_customers():
    pass

    