#Si deve realizzare un sistema per un ristorante per gestire i clienti e i tavoli
#con il relativo numero di posti , le prenotazioni (effettuate dai clienti per un certo giorno e ora,
#e per un certo numero di persone). Alle prenotazioni vengono assegnati uno o più tavoli
#(divisi in fumatori/non fumatori) , i camerieri che servono i clienti al tavolo e il conto,
#composto dalle singole portate ordinate.
#Dei clienti interessano il nome e numero di telefono , mentre dei camerieri interessano
#il nome e gli anni di servizio. Ogni portata ha un costo unitario previsto dal listino e al cliente
#viene presentato il conto dove vengono indicate le singole portate con il nome, il prezzo unitario
#e la quantità ordinata che permette di calcolare il totale per portate e il conto totale per gruppo.

L=[]
#chiamata al cellulare
n=1
i=0
print("é in atto una chiamata al ristorante allo scopo di effettuare una prenotazione.")
print("-------------------------------------------------------------------------------")
print("Benvenuto nel ristorante 'Da Zama'!")
print("Seleziona la voce desiderata")
print("1: voglio effettuare una prenotazione.")
print("2: chiedo le informazioni sul ristorante")
print("3: voglio vedere la lista delle prenotazioni")
print("0: chiudi la chiamata")
while i==0:
    scelta=int(input("Seleziona la voce desiderata"))
    if scelta==1:
        print("-------------------------------------------------------------------------------")        
        nome=input("Inserisci il tuo nome:")
        num=input("Inserisci il numero di posti:(è pregato di inserire anche la parola 'posti'(es:3posti)")
        print("la tua prenotazione è la numero", n)
        L.append(nome)
        L.append(num)
        L.append(n)
        n=n+1
    elif scelta==2:
        print("-------------------------------------------------------------------------------")
        print("Il nostro ristorante ha origini italiane, pur essendo ora a new york, il nostro")
        print("primo ristorante è stato aperto a Codigoro, in Italia, nel 1965, e questo ristorante")
        print("invece è stato aperto nel 1972 a seguito della migrazione della nostra famiglia")
    elif scelta==3:
        print("-------------------------------------------------------------------------------")
        print(L)
    elif scelta==0:
        i=1

print("Ora si è passati al ristorante.")
print("-------------------------------------------------------------------------------")
A=[]
print("benvenuti nel nostro ristorante:")
print("1: ho effettuato una prenotazione")
print("2: devo dichiarare delle allergie")
print("3: voglio vedere le allergie che ho denunciato")
d=0
while d==0:
    sce=int(input("Inserisci la voce che fa al caso tuo:"))
    if sce==1:
        print("-------------------------------------------------------------------------------")
        p=int(input("Inserisci il numero della prenotazione"))
        k=0
        c=0
        while c==0:
            if L[k]==p:
                print("bene, la accompagno al suo tavolo.")
                c=c+1
            else:
                k=k+1
    elif sce==2:
        print("-------------------------------------------------------------------------------")
        x=0
        while x==0:
            sc=input("desideri esprimere un allergia?(si o no)")
            if sc=="si":
                allergia=input("a cosa sei allergico:")
                A.append(allergia)
            else:
                x=1
    elif sce==3:
        print("-------------------------------------------------------------------------------")
        print(A)
        A=[]
    elif sce==0:
        d=1
    
