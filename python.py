print("Завдання 1")
text = input("Введіть рядок: ")

for numbers in "0123456789":
    text = text.replace(numbers, "")  

print("Рядок без цифр:", text)

print("")
print("Завдання 2")