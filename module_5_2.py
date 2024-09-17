class House:
    # Метод __init__ для инициализации объекта с именем и количеством этажей
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    # Метод go_to для перемещения на новый этаж
    def go_to(self, new_floor):
        if 1 <= new_floor <= self.number_of_floors:
            for floor in range(1, new_floor + 1):
                print(floor)
        else:
            print("Такого этажа не существует")

    # Магический метод __len__ возвращает количество этажей
    def __len__(self):
        return self.number_of_floors

    # Магический метод __str__ возвращает строку с названием и количеством этажей
    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)  # Ожидаемый результат: "Название: ЖК Эльбрус, кол-во этажей: 10"
print(h2)  # Ожидаемый результат: "Название: ЖК Акация, кол-во этажей: 20"

# __len__
print(len(h1))  # Ожидаемый результат: 10
print(len(h2))  # Ожидаемый результат: 20
