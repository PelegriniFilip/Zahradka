import tkinter #vkladam knižnicu
import random #vlkadam možnosť vytvárat náhody
canvas = tkinter.Canvas(width = 1000, height = 600, bg = 'white') #robím plátno
canvas.pack() #kreslím plátno

def muchotravka(): #funkcia na muchotrávku
    canvas.create_oval(50, 300, 200, 450, fill = 'red', outline = 'red') #klobúčik pre muchotrávku
    canvas.create_rectangle(40, 400, 210, 450, fill = 'white', outline = 'white') #zrezanie spodnej časti klobúka
    canvas.create_rectangle(100, 400, 150, 500, fill = 'brown', outline = 'brown') #nožička muchotrávky
    canvas.create_oval(100, 480, 150, 520, fill = 'brown', outline = 'brown') #zaoblenie nožičky muchotrávky
    a = 60 #do a som vložil číslo 60
    b = 80 #do b som vložil číslo 80
    
    for i in range (4): #príkaz na to aby sa všetko čo je vňom napísané, zopakovalo 4-krát
        canvas.create_oval(a, 370, a + 20, 390, fill = 'white', outline = 'white') #kreslenie 4-och  spodných bielich bodiek na muchotrávke
        a = a + 37 #do a sa vloží hodnota a a pripocíta sa knemu číslo 37
        
    for i in range (3): #príkaz na to aby sa príkazy napísane vtomto príkaze topakovali 3-krát
        canvas.create_oval(b, 330, b + 20, 350, fill = 'white', outline = 'white') #príkaz na kreslenie 3-och vrchných bodiek na muchotrávke
        b = b + 35 #do b sa vloží hodnota b a pripočíta sa knemu číslo 35

def travnik(): #funkcia pre kreslenie trávnika
    canvas.create_rectangle(-100, 570, 1100, 700, fill = 'green', outline = 'green') #príkaz na obdľžnik v spodnej časti plátna
    a = 5 #do a sa vkladá hodnota 5
    
    for i in range (150): #cyklus ktorý zopakuje všetko co je vnom napísané 150-krát
        canvas.create_line(a, 560, a, 600, fill = 'green', width = 3) #príkaz ktorí vykreslí zelenú čiaročku
        a = a + 7 #do a sa vkladá hodnota a a pripočítava sa knej čislo 7

def slnko(): #funkacia na kreslenie slnka
    for i in range(40): #cyklus ktorý zopakuje všetko co je vnom napísané 40-krát
        x = random.randint(1, 200) #do x sa vkladá náhodne vygenerované čislo od 1 po 200
        y = random.randint(1, 200) # do y sa vlkadá náhodne vygenerované čislo od 1po 200
        canvas.create_line(0, 0, x, y, fill = 'yellow', width = 3) #vykrelí sa lúč slnka

def pozemky(): #funkaci na kreslenie pozemkov
    n = 700 #do písmena n sa vkladá číslo 700
    m = 50 #do pismena m sa vkladá číslo 50
    b = 700 #do písmena b sa vkladá číslo 700
    v = 700 #do písmena v  sa vkladá číslo 700
    
    for i in range (5): #cyklus v ktorom sa zopakujú všetky príkazy vtom cykle 5-krát
        x = random.randint(20, 50) #do písmena x sa vkladá náhodne vygenerované číslo od 20 po 50
        y = random.randint(20, 50) #do písmena y sa vkladá náhodne vygenerované čislo od 20 po 50
        canvas.create_rectangle(n, m, n + x, m + y) #príkaz na vykreslenie štvorca (jedného pozemku)
        n = n + 60 #do písmena n sa vkladá hodnota z na a pripočítava sa číslo 60
        
    for i in range (5): #cyklus v ktorom sa zopakujú všetky príkazy vtom cykle 5-krát
        x = random.randint(20, 50) #do písmena x sa vkladá náhodne vygenerované číslo od 20 po 50
        y = random.randint(20, 50) #do písmena y sa vkladá náhodne vygenerované číslo od 20 po 50
        canvas.create_rectangle(b, m + 60, b + x, m + 60 + y) #príkaz na vykreslenie štvorca (jedného pozemku)
        b = b + 60 #do písmena n sa vkladá hodnota z na a pripočítava sa číslo 60
        
    for i in range (5): #cyklus v ktorom sa zopakujú všetky príkazy vtom cykle 5-krát
        x = random.randint(20, 50) #do písmena x sa vkladá náhodne vygenerované číslo od 20 po 50
        y = random.randint(20, 50) #do písmena y sa vkladá náhodne vygenerované číslo od 20 po 50
        canvas.create_rectangle(v, m + 120, v + x, m + 120 + y) #príkaz na vykreslenie štvorca (jedného pozemku)
        v = v + 60 #do písmena n sa vkladá hodnota z na a pripočítava sa číslo 60
        
    
def voda(): #funkcia na kreslenie jazierka
    x = 830 #do písmena x sa vkladá čislo 830
    y = 430 #do písmena y sa vkladá číslo 430
    n = 800 #do písmena n sa vkladá čislo 800
    m = 400 #do písmena m sa vkladá číslo 400
    
    for i in range (20): #cyklus v ktorom sa zopakuju všetky príkazy ktore sú vňom 20-krát
        canvas.create_oval(x, y, n, m, outline = 'blue', width = 2) #vykreslí sa krúžok
        x = x + 5 #do x sa vloží hodnota z x a pripočíta sa knemu číslo 5
        y = y + 5 #do y sa vloží hodnota z y a pripočíta sa knemu číslo 5
        n = n - 5 #do n sa vloží hodnota z n a pripočíta sa knemu číslo 5
        m = m - 5 #do m sa vloží hodnota z m a pripočíta sa knemu číslo 5
    

muchotravka() #volá sa funkcia muchotrávka, aby ju program mohol vykresliť
travnik() #volá sa funkcia trávnik, aby ju program mohol vykresliť
slnko() #volá sa funkcia slnko, aby ju program mohol vykresliť
pozemky() #volá sa funkcia pozemky, aby ju program mohol vykresliť
voda() #volá sa funkcia voda, aby ju program mohol vykresliť
