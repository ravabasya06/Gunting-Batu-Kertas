import random

def ulang():
    inputJ = input("Gunting, Batu, atau Kertas? : ")
    kompJ = ["gunting", "batu", "kertas"]
    kompR = random.randint(0, 2)
    
    if inputJ.lower() == "gunting" and kompJ[kompR] == "kertas":
        print("Komputer mengeluarkan "+kompJ[kompR]+"!")
        print("Anda menang!")
    elif inputJ.lower() == "batu" and kompJ[kompR] == "gunting":
        print("Komputer mengeluarkan "+kompJ[kompR]+"!")
        print("Anda menang!")
    elif inputJ.lower() == "kertas" and kompJ[kompR] == "batu":
        print("Komputer mengeluarkan "+kompJ[kompR]+"!")
        print("Anda menang!")
    elif inputJ.lower() == kompJ[kompR]:
        print("Komputer mengeluarkan "+kompJ[kompR]+"!")
        print("Anda seri!")
    else:
        print("Komputer mengeluarkan "+kompJ[kompR]+"!")
        print("Anda kalah! AWOKAWOAWK")
        
    pengulangan = input("Lakukan perhitungan lagi? ya / tidak : ")
    if pengulangan == "ya":
        ulang()
    elif pengulangan == "tidak":
        print("Ok")
    else:
        print("Saya tidak mengerti perintah anda, saya akan menganggap anda menjawab tidak.")
ulang()
