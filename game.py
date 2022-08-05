import random

digits = 4
mainList = list()
possibleAnswers = list()

# Bir sayının tüm rakamları farklı mı ona bakar
def isAllDifferent(n):
    nStr = str(n) # Convert number to string
    for i in range(digits):
        for j in range(digits):
            if nStr[i] == nStr[j] and i != j:
                return False
    return True

# Olası tüm cevapları bul ve kaydet
def findAllPossibleAnswers():
    global possibleAnswers
    if len(mainList) == 0:
        start = 10**(digits - 1)
        end = 10**digits
        for i in range(start, end):
            if isAllDifferent(i):
                mainList.append(i)
    possibleAnswers = mainList.copy()

# Basamak sayısını değiştirir
def setDigit(n):
    digits = n
    mainList.clear()
    findAllPossibleAnswers()

# Rastgele bir sayı seç
def ai_pickRandom():
    return random.choice(possibleAnswers)

# Oyuncunun tahminindeki eksileri bul
def ai_findMinus(ai_pick, user_guess):
    result = 0
    pick_str = str(ai_pick)
    guess_str = str(user_guess)

    for i in range(digits):
        for j in range(digits):
            if i != j and pick_str[i] == guess_str[j]:
                result += 1
    return result

# Oyuncunun tahminindeki artıları bul
def ai_findPlus(ai_pick, user_guess):
    result = 0
    pick_str = str(ai_pick)
    guess_str = str(user_guess)

    for i in range(digits):
        if pick_str[i] == guess_str[i]:
            result += 1
    return result

# Eski kodumdan aldığım ve ne işe yaradığını bilmediğim fonksiyon #1
def ai_rtrn(num, ai_guess):
    result = 0
    num_str = str(num)
    guess_str = str(ai_guess)

    for i in range(digits):
        for j in range(digits):
            if num_str[i] == guess_str[j]:
                result += 1
                break
    return result

# Eski kodumdan aldığım ve ne işe yaradığını bilmediğim fonksiyon #2
def ai_rtrnPlus(num, ai_guess):
    result = 0
    num_str = str(num)
    guess_str = str(ai_guess)
    for i in range(digits):
        if num_str[i] == guess_str[i]:
            result += 1
    return result

# Olmayacak cevapları eler
def ai_solve(ai_guess, minus, plus):
    global possibleAnswers
    acceppted_ones = list()

    for i in possibleAnswers:
        rt = ai_rtrn(i, ai_guess)
        rtpl = ai_rtrnPlus(i, ai_guess)

        if minus == 0 and rt > plus:
            continue
        elif rt != (plus + minus) or rtpl != plus:
            continue
        acceppted_ones.append(i)
    possibleAnswers = acceppted_ones.copy()


def main():
    findAllPossibleAnswers()

    while len(possibleAnswers) > 0:
        ai_guess = ai_pickRandom()
        print(f"Tahminim: {ai_guess}")

        user_minus = int(input("-"))
        user_plus = int(input("+"))
        if user_plus == digits:
            break
        ai_solve(ai_guess, user_minus, user_plus)

    if len(possibleAnswers) > 0:
        print("Buldum!")
    else:
        print("Bir hata yaptınız.")

if __name__ == '__main__':
    main()