from ..models import Organization


def get_all_organizations():
    print('Pozdrav iz get_all_organization funkcije')
    


def get_organization():
    try:
         with open('data\\organizations.txt', 'r') as file_reader:
            return file_reader.read()

    except Exception as ex:
        print(f'Dogodila se greska {ex}')

def save_organization(organization: Organization):
    # umjesto u datoteku spremi u bazu
    #print('Pozdrav iz save_organization funkcije')
    #print(f'Organizacija {str(organization)} je spremljena u bazu')
    try:
        with open('data\\organizations.txt', 'a') as file_writer:
            file_writer.write(str(organization) + '\n')
            
        #file_writer = open('organizations.txt', 'w')
        #dio koda koji zelimo izvrsiti
        #file_writer.write(str(organization))               ovako moze ici! ali je lakse gornji kod
        #file_writer.close()
    
    except Exception as ex:
        print(f'Dogodila se greska {ex}')
