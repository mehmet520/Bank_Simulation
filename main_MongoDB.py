import pymongo
client = pymongo.MongoClient("mongodb+srv://mehmet:mehmet@mehmetbankkonto.8ktnn.mongodb.net/bank_simulation?retryWrites=true&w=majority")
# db = client.test
db = client['bank_simulation']
collection= db ['bankData']

def konto_erstellen():
    kontoNummer= collection.find_one({'_id': 0})['counter']
    collection.update_one({'_id': 0}, {'$set':{'counter': kontoNummer+1}}) 
    
    vorname= input('Wie heisen Sie mit der Vorname?\n')
    name= input('Wie heisen Sie mit der Nachname?\n')
    passwort= input('Geben Sie eine Passwort ein:\n')
    id_info={'_id': kontoNummer, 'vorname': vorname, 'nachname': name, 'passwort': passwort, 'geldbetrag': 0}
    collection.insert_one(id_info)
    
    print (f'\nIhre Kontonummer lautet: {kontoNummer}\nIhre Passwort lautet: {passwort}\nBitte notieren Sie es!\n\n')
    anfang()
def geld_abheben ():
    id=int(input('Geben Sie Ihre Kontonummer ein:\n'))
    passwort=input('\nGeben Sie Ihre Passwort ein:\n')
    id_info= collection.find_one({'_id': id})
    passwortTrue= id_info['passwort']

    if passwortTrue==passwort:
        while True:
            geld_betrag= float(input('\nGeben Sie den Geldbetrag ein, den Sie abheben moechten:\n'))
            if geld_betrag <0:
                print('Bitte geben Sie eine pozitive Zahl ein.')
                continue

            if geld_betrag > id_info['geldbetrag']:
                print (f'\nSie haben nur {id_info["geldbetrag"]}€ auf Ihrem Konto.')
                continue
            break
        collection.update_one({'_id': id}, {'$set':{'geldbetrag': id_info['geldbetrag']-geld_betrag}})
        print (f'Restbetrag auf Ihrem Konto: {id_info["geldbetrag"]-geld_betrag}')
        anfang()
    else:
        print('Ihre Kontonummer oder Passwort ist Falsh')
        antwort= input('Geben Sie 1 ein, um es erneut zu versuchen;\nGeben Sie 2 ein, um ein neues Konto zu eroeffnen.\nGeben Sie was anders ein, um zum Anfang zurueckzukehren.\n')
        if antwort=='1':
            geld_abheben()
        elif antwort=='2':
            konto_erstellen()
        else:
            anfang()

def geld_einzahlen():
    id=int(input('Geben Sie Ihre Kontonummer ein:\n'))
    passwort=input('\nGeben Sie Ihre Passwort ein:\n')
    id_info= collection.find_one({'_id': id})
    passwortTrue= id_info['passwort']

    if id_info["passwort"]==passwort:
        while True:
            geld_betrag= float(input('\nGeben Sie den Geldbetrag ein, den Sie einzahlen moechten:\n'))
            if geld_betrag <0:
                print('Bitte geben Sie eine pozitive Zahl ein.')
                continue

            if geld_betrag > 10000:
                print (f'Sie koenen nicht mehr als 10000€ auf ein mal auf Ihrem Konto einzahlen.')
                continue
            break
        collection.update_one({'_id': id}, {'$set':{'geldbetrag': id_info['geldbetrag']+geld_betrag}})    
        print (f'\nNeubetrag auf Ihrem Konto: {id_info["geldbetrag"]+geld_betrag}\n')
        anfang()
    else:
        print('Ihre Kontonummer oder Passwort ist Falsh')
        antwort= input('Geben Sie 1 ein, um es erneut zu versuchen;\nGeben Sie 2 ein, um ein neues Konto zu eroeffnen.\nGeben Sie was anders ein, um zum Anfang zurueckzukehren.\n')
        if antwort=='1':
            geld_einzahlen()
        elif antwort=='2':
            konto_erstellen()
        else:
            anfang()
def geld_ueberweisen ():
    id=int(input('Geben Sie Ihre Kontonummer ein:\n'))
    passwort=input('\nGeben Sie Ihre Passwort ein:\n')
    id_info= collection.find_one({'_id': id})
    passwortTrue= id_info['passwort']

    if passwortTrue==passwort:
        while True:
            ueberweisung_konto= int(input ('Bitte geben Sie die Kontonummer ein, die Sie ueberweisen moechten:\n'))

            try:
                collection.find_one({'_id': ueberweisung_konto})
            except:
                weiter=input('Konto nicht gefunden. Geben Sie 1 ein, um es erneut zu versuchen;\nGeben Sie was anders ein, um zum Anfang zurueckzukehren.\n')
                if weiter=='1':
                    continue
                else:
                    anfang()
                    quit()

            geld_betrag= float(input('Geben Sie den Geldbetrag ein, den Sie ueberweisen moechten:\n'))
            if geld_betrag <0:
                print('Bitte geben Sie eine pozitive Zahl ein.')
                continue

            if geld_betrag > id_info['geldbetrag']:
                print (f'Sie haben nur {id_info["geldbetrag"]}€ auf Ihrem Konto.')
                continue
            break
        collection.update_one({'_id': id}, {'$set':{'geldbetrag': id_info['geldbetrag']-geld_betrag}})  
        ueberweisung_konto_geldbetrag=collection.find_one({'_id': ueberweisung_konto})['geldbetrag']  
        collection.update_one({'_id': ueberweisung_konto}, {'$set':{'geldbetrag': ueberweisung_konto_geldbetrag + geld_betrag}})    
        
        d=id_info['geldbetrag']-geld_betrag

        print (f'Restbetrag auf Ihrem Konto: {d}\n')
        anfang()
    else:
        print('Ihre Kontonummer oder Passwort ist Falsh')
        antwort= input('Geben Sie 1 ein, um es erneut zu versuchen;\nGeben Sie 2 ein, um ein neues Konto zu eroeffnen.\nGeben Sie was anders ein, um zum Anfang zurueckzukehren.\n')
        if antwort=='1':
            geld_abheben()
        elif antwort=='2':
            konto_erstellen()
        else:
            anfang()

def anfang():
    antwort= input('Was kann ich fuer Sie tun?\n1. Konto erstellen.\n2. Geld abheben.\n3. Geld einzahlen.\n4. Geld ueberweisen.\nWaehlen Sie bitte eine Nummer: ')
    if antwort=="1":
        konto_erstellen()

    elif antwort=='2':
        geld_abheben()

    elif antwort=='3':
        geld_einzahlen()

    elif antwort=='4':
        geld_ueberweisen()

anfang()