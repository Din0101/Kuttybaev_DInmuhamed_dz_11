
import traceback


class MyException(Exception):
    def __init__(self, txt):
        self.txt = txt

    def __str__(self):
        return self.txt


class CheckAndAdd:

    def __init__(self):
        self.__result = []
        while True:
            data = input('Число: ')
            try:
                self.__result.append(int(data))
            except ValueError as e:
                if data == 'stop':
                    break
                print('Ошибка с моим обработчиком:\n', traceback.format_exc())
            except Exception as e:
                if data == 'stop':
                    break
                raise MyException('Какая-то другая ошибка')

    def __str__(self):
        return ', '.join(map(str, self.__result))


if __name__ == '__main__':
    c = CheckAndAdd()
    print(c)
    d = CheckAndAdd()
    print(d)