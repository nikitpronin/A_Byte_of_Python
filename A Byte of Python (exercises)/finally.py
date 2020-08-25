import time

try:
    f = open('poem.txt')
    while True: #наш обычный способ чтения файла
        line = f.readline()
        if len(line) == 0:
            break
        print(line, end = ' ')
        time.sleep(2) #ожидает некоторое время
except KeyboardInterrupt:
    print('!! Вы отменили чтение файла.')
finally:
    f.close()
    print('(Очистка: Закрытие файла)')
