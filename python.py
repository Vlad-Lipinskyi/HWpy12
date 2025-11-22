print("Завдання 1")
text = input("Введіть рядок: ")

for numbers in "0123456789":
    text = text.replace(numbers, "")  

print("Рядок без цифр:", text)

print("")
print("Завдання 2")
surname = "Ліпінський"
lowerCase = surname.lower()

mostLetter = None
mostCount = 0

for letters in lowerCase:        # перебираємо кожен символ
    count = lowerCase.count(letters)   # рахуємо, скільки разів він зустрічається
    if count > mostCount:
        mostCount = count
        mostLetter = letters

print(f"Прізвище - {surname}")
print(f"Найчастіша літера: '{mostLetter}', зустрічається {mostCount} раз(и).")
