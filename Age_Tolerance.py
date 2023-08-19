# Программа допуска на атракцион
# Детям до 14 лет вход запрещён. 
# С 14 лет до 18 лет, только с родителями.
# С 18 лет и старше, вход разрешён

age = int(input("Введите ваш возраст "))
print(age)

def age_tolerance():
    if age > 18:
        print("Вход разрешён")
    elif age >= 14 and age < 18:
        print("Вход только с родителями")
    else:
        print("Вход запрещён") 
        
def main():
    age_tolerance()
    return 0

if __name__ == '__main__':
	main()

