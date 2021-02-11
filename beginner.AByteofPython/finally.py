import time
try:
    f = open('poem.txt')
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line, end='')
        time.sleep(2)
except KeyboardInterrupt:
    print('!! You canceled the operation reading file')
finally:
    f.close()
    print('(Clean: Closing file)')