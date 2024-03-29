from features import (Organization,
                      get_all_organizations,
                      get_organization,
                      save_organization)
from features import (Customers,
                      get_all_customers,
                      get_customer,
                      save_customers)


def start_app():
    print('Pozdrav iz start_app() funkcije')
    org = Organization('Algebra d.o.o.', '123456789658')
    cus = Customers('Pero Zderic', 'perozderic@gmail.com', '0919088852 ') 
    save_organization(org) 
    save_customers(cus)
    
    get_all_customers()
    get_all_organizations()
    organization_from_file = get_organization()
    print('\nOrganizacija iz datoteke')
    print(organization_from_file)
    print()
    customer_from_file = get_customer()
    print('\nKupac iz baze')
    print(customer_from_file)
    print()
    
if __name__ == '__main__':
    start_app()