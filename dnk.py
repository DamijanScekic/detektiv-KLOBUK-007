#Barva las:
las_Crna = "CCAGCAATCGC"
las_Rjava = "GCCAGTGCCG"
las_Korencek = "TTAGCTATCGC"

#Oblika obraza:
Kvadraten = "GCCACGG"
Okrogel = "ACCACAA"
Ovalen = "AGGCCTCA"

#Barva oci:
oci_Modra = "TTGTGGTGGC"
oci_Zelena = "GGGAGGTGGC"
oci_Rjava = "AAGTAGTGAC"

#Spol:
Moski = "TGCAGGAACTTC"
Zenska = "TGAAGGACCTTC"

#Rasa:
Belec = "AAAACCTCA"
Crnec = "CGACTACAG"
Azijec = "CGCGGGCCG"

datoteka = open("txtSCEKIC", "r")
DNA = datoteka.read()

print("Detektiv KLOBUK 007 je na delu!")

if DNA.find(Moski) and DNA.find(Belec) and DNA.find(las_Korencek) and DNA.find(oci_Rjava)\
        and DNA.find(Okrogel) != -1:
    print("Sladoled je ukradel Ziga!")

elif DNA.find(Moski) and DNA.find(Belec) and DNA.find(las_Crna) and DNA.find(oci_Modra)\
        and DNA.find(Ovalen) != -1:
    print("Sladoled je ukradel Matej!")

elif DNA.find(Moski) and DNA.find(Belec) and DNA.find(las_Rjava) and DNA.find(oci_Zelena)\
        and DNA.find(Kvadraten) != -1:
    print("Sladoled je ukradel Miha!")
else:
    print("Nihce ni ukradel sladoleda!")

print("Klobuku resnice se je nemogoce izogniti!")

datoteka.close()
