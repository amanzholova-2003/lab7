n = int(input())
phone_book = {}
for i in range(n):
    phone, name = input().split()
    phone_book[name] = phone
query = input()
if query in phone_book:
    print(phone_book[query])
else:
    print("Нет в телефонной книге")


