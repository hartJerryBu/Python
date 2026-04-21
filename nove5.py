users = {
    "pepa": 1234,
    "josef": "heslo",
    "marie": "Pepa1234_*"
}

attempts = 3

while attempts :
    attempts -= 1
    user_name = input(" Vložte uživatelské jméno: ")
    password = input(" Vložte heslo: ")
    
    if user_name not in users:
            print(" Neplatné uživatelské jméno! ")
            continue
    
    if str(users[user_name]) != password:
            print(" Neplatné heslo! ")
        
    print (" přístup povolen ")

    
    
    break
    
else:
        

    print(" Přihlášení se nezdařilo. Počet pokusů vyčerpán. ")
    
