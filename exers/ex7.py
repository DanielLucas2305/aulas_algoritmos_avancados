area = float(input("Insira a area a ser pintada em metros quadrados: "))

# quanti_lata = []
# quanti_galao = []

lata = 18
galao = 3.6
lata_price = 80
galao_price = 25

quantidade_tinta = round((area / 6) + ((area / 6) * 0.1))
tinta_falta = 0

print(f"Voce precisara de {quantidade_tinta} litros de tinta!")

if (quantidade_tinta - lata) < 0:
    print(lata_price)
else:
    while quantidade_tinta > 0:
        tinta_falta = quantidade_tinta - lata
        if tinta_falta < lata:
            tinta_falta = tinta_falta - galao
            
            