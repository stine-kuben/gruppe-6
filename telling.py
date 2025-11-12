def HvorMangeඞ(tekst, symbol):
    AmongUsMeter = 0
    
    for letter in tekst:
        if letter == symbol:
            AmongUsMeter += 1
    
    print(f'Det er {AmongUsMeter} {symbol} i teksten: \n"{tekst}"')

word = "dette er en ඞ tekst ඞ fr ඞ"
HvorMangeඞ(word, "ඞ")