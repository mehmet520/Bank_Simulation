import json

def konto_erstellen():
    with open("bankData.json","r+") as jdata:
        pdata=json.load(jdata)
        print(pdata)
        id=pdata['id']
        pdata['id']=id+1
        # jdata.seek(0)      
        # json.dump(pdata,jdata,indent=4)
        # jdata.truncate()
        # print(id)
        vorname= input('Wie heisen Sie mit der Vorname?\n')
        name= input('Wie heisen Sie mit der Nachname?\n')
        passwort= input('Geben Sie eine Passwort ein:\n')
        id_info={'vorname': vorname, 'nachname': name, 'passwort': passwort, 'geldbetrag': 0}
        pdata[id]=id_info
        print(pdata)
        jdata.seek(0)   
        json.dump(pdata,jdata,indent=4)
        jdata.truncate()     
    print (f'Ihre ID Nummer lautet: {id}\nIhre Passwort lautet: {passwort}\nBitte notieren Sie es!\n\n')
    anfang()
def geld_abheben ():
    id=input('Geben Sie Ihre ID Nummer ein:\n')
    passwort=input('Geben Sie Ihre Passwort ein:\n')
    with open ('bankData.json','r') as jdata:
        pdata=json.load (jdata)
    # id_info=pdata[id]
    # if id_info[passwort]==passwort:
    if pdata[id]["passwort"]==passwort:
        while True:
            geld_betrag= float(input('Geben Sie den Geldbetrag ein, den Sie abheben moechten:\n'))
            if geld_betrag <0:
                print('Bitte geben Sie eine pozitive Zahl ein.')
                continue

            if geld_betrag > pdata[id]['geldbetrag']:
                print (f'Sie haben nur {pdata[id]["geldbetrag"]}€ auf Ihrem Konto.')
                continue
            break
        pdata[id]["geldbetrag"]= pdata[id]["geldbetrag"]-geld_betrag
        with open ('bankData.json', 'w') as jdata:
            jdata.write(json.dumps(pdata, indent=4))
        print (f'Restbetrag auf Ihrem Konto: {pdata[id]["geldbetrag"]}')
    else:
        print('Ihre ID oder Passwort ist Falsh')
        antwort= input('Geben Sie 1 ein, um es erneut zu versuchen;\nGeben Sie 2 ein, um ein neues Konto zu eroeffnen.\nGeben Sie was anders ein, um zum Anfang zurueckzukehren.\n')
        if antwort=='1':
            geld_abheben()
        elif antwort=='2':
            konto_erstellen()
        else:
            anfang()

def geld_einzahlen():
    id=input('Geben Sie Ihre ID Nummer ein:\n')
    passwort=input('Geben Sie Ihre Passwort ein:\n')
    with open ('bankData.json','r') as jdata:
        pdata=json.load (jdata)
    if pdata[id]["passwort"]==passwort:
        while True:
            geld_betrag= float(input('Geben Sie den Geldbetrag ein, den Sie einzahlen moechten:\n'))
            if geld_betrag <0:
                print('Bitte geben Sie eine pozitive Zahl ein.')
                continue

            if geld_betrag > 10000:
                print (f'Sie koenen nicht mehr als 10000€ auf ein mal auf Ihrem Konto einzahlen.')
                continue
            break
        pdata[id]["geldbetrag"]= pdata[id]["geldbetrag"]+geld_betrag
        with open ('bankData.json', 'w') as jdata:
            jdata.write(json.dumps(pdata, indent=4))
        print (f'Neubetrag auf Ihrem Konto: {pdata[id]["geldbetrag"]}')
    else:
        print('Ihre ID oder Passwort ist Falsh')
        antwort= input('Geben Sie 1 ein, um es erneut zu versuchen;\nGeben Sie 2 ein, um ein neues Konto zu eroeffnen.\nGeben Sie was anders ein, um zum Anfang zurueckzukehren.\n')
        if antwort=='1':
            geld_einzahlen()
        elif antwort=='2':
            konto_erstellen()
        else:
            anfang()
def geld_ueberweisen ():
    id=input('Geben Sie Ihre ID Nummer ein:\n')
    passwort=input('Geben Sie Ihre Passwort ein:\n')
    with open ('bankData.json','r') as jdata:
        pdata=json.load (jdata)
    if pdata[id]["passwort"]==passwort:
        while True:
            ueberweisung_konto= input ('Bitte geben Sie die Kontonummer ein, die Sie ueberweisen moechten:\n')
            
            geld_betrag= float(input('Geben Sie den Geldbetrag ein, den Sie abheben moechten:\n'))
            if geld_betrag <0:
                print('Bitte geben Sie eine pozitive Zahl ein.')
                continue

            if geld_betrag > pdata[id]['geldbetrag']:
                print (f'Sie haben nur {pdata[id]["geldbetrag"]}€ auf Ihrem Konto.')
                continue
            break
        pdata[id]["geldbetrag"]= pdata[id]["geldbetrag"]-geld_betrag
        with open ('bankData.json', 'w') as jdata:
            jdata.write(json.dumps(pdata, indent=4))
        print (f'Restbetrag auf Ihrem Konto: {pdata[id]["geldbetrag"]}')
    else:
        print('Ihre ID oder Passwort ist Falsh')
        antwort= input('Geben Sie 1 ein, um es erneut zu versuchen;\nGeben Sie 2 ein, um ein neues Konto zu eroeffnen.\nGeben Sie was anders ein, um zum Anfang zurueckzukehren.\n')
        if antwort=='1':
            geld_abheben()
        elif antwort=='2':
            konto_erstellen()
        else:
            anfang()

def geld_investieren ():
    pass
def anfang():
    antwort= input('Was kann ich fuer Sie tun?\n1. Konto erstellen.\n2. Geld abheben.\n3. Geld einzahlen.\n4. Geld ueberweisen.\n5. Geld investieren.\nWaehlen Sie bitte eine Nummer: ')
    if antwort=="1":
        konto_erstellen()

    elif antwort=='2':
        geld_abheben()

    elif antwort=='3':
        geld_einzahlen()

    elif antwort=='4':
        geld_ueberweisen()

    elif antwort=='5':
        geld_investieren()

anfang()

