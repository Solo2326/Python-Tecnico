#Creare una lista di n numeri decimali, sommarli e fare la media. Dopo l'inserimento sommarl e visualizzare in output la somma e la media.

def sum_and_average():
    numbers = []
    n = int(input("Enter the number of decimal numbers: "))
    print("Enter the decimal numbers:")
    for _ in range(n):
        number = float(input())
        numbers.append(number)
    total = sum(numbers)
    average = total / n
    return total, average


sum_, average_ = sum_and_average()
print(f"The sum of the numbers is: {sum_:.2f}")
print(f"The average of the numbers is: {average_:.2f}")