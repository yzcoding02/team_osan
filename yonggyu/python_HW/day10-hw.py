for i in range(0,10):
    fruits={'Dattelpalme':697,'Pflaume':17,'Granatapfel':68, 'dattelpalme':697, 'pflaume':17, 'granatapfel':68}
    fruit=input("Das ist ein Obstladen. Wonach suchst du?")
    if fruit in fruits:
        print(f"wir sind haben {fruit}, {fruits[fruit]} bleiben")    
    else :
        print(f"Entschuldigen Sie, Sir, aber in unserem Shop finden Sie{fruit}, Es ist nicht mehr da. Bitte kommen Sie nächstes Mal wieder.")