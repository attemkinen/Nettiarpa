import random

def arvo_numerot():
    arvotut = random.sample(range(1, 21), 7)
    lisanumero = random.choice([n for n in range(1, 21) if n not in arvotut])
    return set(arvotut), lisanumero

def tarkista_voitto(pelaajan_numerot, arvotut_numerot, lisanumero, panos):
    pelaajan_numerot = set(map(int, pelaajan_numerot.split()))
    arvotut_numerot = set(map(int, arvotut_numerot.split()))
    lisanumero = int(lisanumero)
    panos = float(panos)

    oikein = len(pelaajan_numerot & arvotut_numerot)
    osui_lisanumeroon = lisanumero in pelaajan_numerot
    
    voitot = {
        (7, False): 1000000,
        (6, True): 100000,
        (6, False): 2000,
        (5, False): 50,
        (4, False): 10,
        (3, True): 2,
        (0, True): 5
    }
    
    voitto = voitot.get((oikein, osui_lisanumeroon), 0) * panos
    return voitto

# Luokka Robot Frameworkia varten
class NettiLotto:
    def tarkista_voitto(self, pelaajan_numerot, arvotut_numerot, lisanumero, panos):
        return tarkista_voitto(pelaajan_numerot, arvotut_numerot, lisanumero, panos)




def pelaa_lotto():
    raha = 10.0
    print("Tervetuloa nettilottoon! Valitse 7 numeroa väliltä 1-20.")
    
    while raha > 0:
        try:
            print(f"Sinulla on {raha:.2f}€ rahaa.")
            panos = float(input("Aseta panos (0.50€ tarkkuudella): "))
            if panos < 0.50 or panos > raha or panos % 0.50 != 0:
                raise ValueError("Virheellinen panos. Aseta panos 0.50€ tarkkuudella ja enintään nykyisen rahamäärän verran.")
            
            valinnat = set(map(int, input("Syötä 7 eri numeroa väliltä 1-20 pilkulla erotettuna: ").split(",")))
            if len(valinnat) != 7 or not all(1 <= n <= 15 for n in valinnat):
                raise ValueError("Valitse tarkalleen 7 eri numeroa väliltä 1-20.")
        
        except ValueError as e:
            print(e)
            continue
        
        raha -= panos
        arvotut, lisanumero = arvo_numerot()
        print(f"Arvotut numerot: {sorted(arvotut)} ja lisänumero: {lisanumero}")
        
        voitto = tarkista_voitto(valinnat, arvotut, lisanumero, panos)
        raha += voitto
        print(f"Voitit {voitto:.2f}€! Sinulla on nyt {raha:.2f}€ rahaa.")
        
        if raha >= 500:
            print("Onneksi olkoon, olet voittanut pelin!")
            break
        elif raha <= 0:
            valinta = input("Varasi ovat loppuneet, lisää rahaa (K/E)? ").strip().lower()
            if valinta == "k":
                raha = float(input("Kuinka paljon lisäät rahaa? "))
            else:
                print("Peli päättyy, kiitos pelaamisesta!")
                break

if __name__ == "__main__":
    pelaa_lotto()
