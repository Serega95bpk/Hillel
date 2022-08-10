stroka = str(input())
stroka_revers = stroka[::-1]

def polindrom (stroka_1, stroka_2):
    if stroka_1 == stroka_2:
      return True
    else:
      return False

print(polindrom(stroka, stroka_revers))