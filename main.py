import pyperclip

#alcuni esempi, personalizza questo oggetto con i tuoi dati personali
password = {
    'facebook': 'pippo',
    'instagram_nome': 'Maurizio',
    'instagram_password': 'paperino',
    'google_email': 'pippoepaperino',
}


while True:
    print("Quale password ti interessa?")
    for sito in password:
        print(f" - {sito}")
    
    sito_scelto = input()
    
    try:
        password_scelta = password[sito_scelto]
        pyperclip.copy(password_scelta)
        print("\nPassword trovata, sei pronta ad incollarla.")
        input("Premi Enter per continuare...")
    except KeyError:
        #scrivi nello stesso modo in cui leggi, se leggi istagram_nome scrivi istagram_nome
        print("Password non trovata. Scrivi meglio.")