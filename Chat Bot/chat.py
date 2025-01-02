import time


def odgovor_na_pitanje(pitanje):
    kljucne_reci = {
        'zdravo': 'Zdravo! Kako mogu da vam pomognem?',
        'vreme': f'Trenutno vreme je: {time.strftime("%H:%M:%S")}',
        'sati': f'Trenutno vreme je: {time.strftime("%H:%M:%S")}',
        'kako si': 'Ja sam dobro,kako si ti?',
        'pomoc': 'Pitanja koja mogu da razumem: "Koliko je sati?", "Koje je vreme?", "Kako si?", "Pomoc"',
    }

    pitanje = pitanje.lower()

    for kljucna_rec, odgovor in kljucne_reci.items():
        if kljucna_rec in pitanje:
            return odgovor

    return 'Izvinite, nisam razumeo vase pitanje.'

def chat():
    print("Dobrodosli! Pitajte bilo sta ili napisite '0' da biste zavrsili.")
    while True:
        korisnicki_unos = input("Vi: ")

        if korisnicki_unos.lower() == '0':
            print("Bot: Dovidjenja!")
            break

        odgovor = odgovor_na_pitanje(korisnicki_unos)
        print(f"Bot: {odgovor}")


chat()