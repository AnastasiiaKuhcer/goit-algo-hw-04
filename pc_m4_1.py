def write_to_file(path, data):
    try:
        with open(path, 'w', encoding='utf-8') as file:
            file.write('\n'.join(data))
        print(f"Дані успішно записані у файл {path}")
    except Exception as e:
        print(f"Під час запису виникла помилка: {e}")

def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            total = 0
            count = 0
            for line in file:
                try:
                    name, salary = line.strip().split(',')
                    total += int(salary)
                    count += 1
                except ValueError:
                    print(f"Некоректні дані у рядку: {line.strip()}")
            if count == 0:
                return 0, 0
            average = total / count
            return total, average
    except FileNotFoundError:
        print("Файл не знайдено.")
        return 0, 0
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return 0, 0

data = ["Alex Korp,3000", "Nikita Borisenko,2000", "Sitarama Raju,1000"]
write_to_file("salary_file.txt", data)

total, average = total_salary("salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")