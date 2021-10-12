# Функция шифровки сообщения шифром Цезаря
# message - сообщение, x - смещение
key = {} # Ключ
def displace(message, x):

    temp_list = []
    for symbol in message:
        if ord('A') <= ord(symbol) <= ord('Z'):
            if ord(symbol) + x > ord('Z'):
                temp_list.append(chr(ord(symbol) + x - ord('Z') + ord('A') - 1))
                key[symbol] = chr(ord(symbol) + x - ord('Z') + ord('A') - 1)
            elif ord(symbol) + x < ord('A'):
                temp_list.append(chr(ord(symbol) + x + ord('Z') - ord('A') + 1))
                key[symbol] = chr(ord(symbol) + x + ord('Z') - ord('A') + 1)
            else:
                temp_list.append(chr(ord(symbol) + x))
                key[symbol] = chr(ord(symbol) + x)
        elif ord('a') <= ord(symbol) <= ord('z'):
            if ord(symbol) + x > ord('z'):
                temp_list.append(chr(ord(symbol) + x - ord('z') + ord('a') - 1))
                key[symbol] = chr(ord(symbol) + x - ord('z') + ord('a') - 1)
            elif ord(symbol) + x < ord('a'):
                temp_list.append(chr(ord(symbol) + x + ord('z') - ord('a') + 1))
                key[symbol] = chr(ord(symbol) + x + ord('z') - ord('a') + 1)
            else:
                temp_list.append(chr(ord(symbol) + x))
                key[symbol] = chr(ord(symbol) + x)
        elif ord('А') <= ord(symbol) <= ord('Я'):
            if ord(symbol) + x > ord('Я'):
                temp_list.append(chr(ord(symbol) + x - ord('Я') + ord('А') - 1))
                key[symbol] = chr(ord(symbol) + x - ord('Я') + ord('А') - 1)
            elif ord(symbol) + x < ord('А'):
                temp_list.append(chr(ord(symbol) + x + ord('Я') - ord('А') + 1))
                key[symbol] = chr(ord(symbol) + x + ord('Я') - ord('А') + 1)
            else:
                temp_list.append(chr(ord(symbol) + x))
                key[symbol] = chr(ord(symbol) + x)
        elif ord('а') <= ord(symbol) <= ord('я'):
            if ord(symbol) + x > ord('я'):
                temp_list.append(chr(ord(symbol) + x - ord('я') + ord('а') - 1))
                key[symbol] = chr(ord(symbol) + x - ord('я') + ord('а') - 1)
            elif ord(symbol) + x < ord('а'):
                temp_list.append(chr(ord(symbol) + x + ord('я') - ord('а') + 1))
                key[symbol] = chr(ord(symbol) + x + ord('я') - ord('а') + 1)
            else:
                temp_list.append(chr(ord(symbol) + x))
                key[symbol] = chr(ord(symbol) + x)
        else:
            temp_list.append(symbol)
        new_str = ''.join(temp_list)
    return new_str


input_file = open('Input.txt', 'r')
msg = input_file.read()
output_file = open('Output.txt', 'w')
key_file = open("Key.txt", 'w')

x = input('Введите смещение: ')
print('Текст с шифром Цезаря: ')
print(displace(msg, int(x)))
output_file.write(displace(msg, int(x)))
print(displace(displace(msg, int(x)), -int(x)))


list_keys = list(key.keys())
list_keys.sort()

for item in list_keys:
    key_file.write(f'{item} : {key[item]}\n')
