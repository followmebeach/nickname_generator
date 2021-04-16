import random

print('Генератор паролей | Trofimchuk27')
while True:
    chars = list('abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890_')
    length = int(input('Укажите длину никнейма?'+ "\n"))
    random.shuffle(chars)
    pasw = ''.join([random.choice(chars) for x in range(length)])
    print(f'Ваш сгенерированный никнейма - {pasw}')
