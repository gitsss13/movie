contacts = {}

def add_contact(name,phone):
    contacts[name] = phone

def search_contact(name):
    return contacts.get(name,"not found")

if __name__=="__main__":
    add_contacts("Arun", "6380734544")
    add_contaccts("Sureh","9488979608")
    print("Arun's number: ",search_contact("Arun"))
    print("search kabil: ",search_contact("kabil"))
