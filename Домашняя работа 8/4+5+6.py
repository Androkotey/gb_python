# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.
# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
# определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других
# данных, можно использовать любую подходящую структуру, например словарь.
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, для
# указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на
# уроках по ООП.
from abc import ABC, abstractmethod


class EquipmentWarehouse:
    __warehouse_id = 0

    def __init__(self, name=None):
        """Автоматически присваивает id созданному складу (в порядке создания). Если складу не присвоено имя, создаёт
        его по шаблону. Также создаёт словарь для хранения оборудования с доступом (ключём) по id-оборудования. Для
        удобства получения списка id-шников, хранящегося на складе оборудования, используется свойство id"""

        EquipmentWarehouse.__warehouse_id += 1

        self.warehouse_id = EquipmentWarehouse.__warehouse_id
        if name:
            self.name = name
        else:
            self.name = 'EquipmentWarehouse ' + str(self.warehouse_id)

        self._storage = {}

    def warehousing(self, *equipments):
        """Добавляет всё поданное на вход оборудование на данный склад. При необходимости изымает оборудование с
        прежнего склада."""

        for equipment in equipments:
            if equipment.info['id'] not in self._storage.keys():
                if equipment._storage_object:
                    equipment._storage_object._storage.pop(equipment.info['id'])
                    equipment._storage_object = self
                else:
                    equipment._storage_object = self
                self._storage[equipment.info['id']] = equipment
                equipment.info['storage location'] = self.name
            else:
                print(f'Оборудование {equipment.name} не добавлено на склад. На складе уже имеется оборудование с '
                      f'таким id.')

    @property
    def ids(self):
        return {i for i in self._storage.keys()}

    def count(self, equipment_type):
        i = 0
        for equipment in self._storage.values():
            if equipment_type in equipment.info['equipment type']:
                i += 1
        return i

    def __str__(self):
        import pandas as pd

        if self.ids:
            data = {'id': [equipment.info['id'] for equipment in self._storage.values()],
                    'name': [equipment.info['name'] for equipment in self._storage.values()],
                    'equipment type': [equipment.info['equipment type'] for equipment in self._storage.values()],
                    'special': [equipment.info['special'] for equipment in self._storage.values()]}

            return f"===========================================================\n" \
                   f"\t\t\t\t\t\33[1m{self.name}\33[0m \n" \
                   f"___________________________________________________________\n" \
                   f"{pd.DataFrame(data=data).set_index('id').to_string()}\n" \
                   f"___________________________________________________________\n" \
                   f"Всего единиц оборудования на складе: {len(self.ids)}\n" \
                   f"===========================================================\n"

        else:
            return f"===========================================================\n" \
                   f"Склад \33[1m{self.name}\33[0m пуст \n" \
                   f"===========================================================\n"

    @property
    def data(self):
        """Возвращает кортеж ('Название склада', DataFrame, количество записей)"""

        import pandas as pd

        if self.ids:
            data = {'id': [equipment.info['id'] for equipment in self._storage.values()],
                    'name': [equipment.info['name'] for equipment in self._storage.values()],
                    'equipment type': [equipment.info['equipment type'] for equipment in self._storage.values()],
                    'special': [equipment.info['special'] for equipment in self._storage.values()]}

            return self.name, pd.DataFrame(data=data).set_index('id').to_string(), len(self.ids)

    def write_off(self, equipment):
        self._storage.pop(equipment.info['id'])
        equipment._storage_object = None
        equipment.info['storage location'] = None


class Equipment(ABC):
    __equipment_ids = []

    @abstractmethod
    def __init__(self, equipment_name=None, equipment_id=None):
        self._storage_object = None  # ссылка на объект склада
        self.equipment_type = 'other'

        if equipment_id:
            if equipment_id in Equipment.__equipment_ids:
                self.id = max(Equipment.__equipment_ids + [0]) + 1
                print(f'Предотвращена попытка перезаписи существущего id, оборудованию присвоен id{self.id}.')
                print(f'Для добавления оборудования с id{equipment_id}, сперва спишите оборудование с таким id.')
            else:
                self.id = equipment_id
        else:
            self.id = max(Equipment.__equipment_ids + [0]) + 1
        Equipment.__equipment_ids.append(self.id)

        if equipment_name:
            self.name = equipment_name
            self._validate_name()
        else:
            self.name = 'Equipment ' + str(self.id)

        self.info = {'name': self.name,
                     'id': self.id,
                     'special': {},
                     'storage location': None}

    def __str__(self):
        return '\n'.join(f"{key}: {self.info[key]}" for key in self.info)

    def send_to_warehouse(self, warehouse: EquipmentWarehouse):
        warehouse.warehousing(self)

    def write_off(self):
        if self._storage_object:
            self._storage_object.write_off(self)
        else:
            return None

    def _validate_name(self):
        """Не позволяет назвать принтер сканнером, сканнер принтером и т.д."""

        all_types = {'printer', 'scanner', 'xerox'}
        this_type = (isinstance(self, Printer) * 'printer' +
                     isinstance(self, Scanner) * 'scanner' +
                     isinstance(self, Xerox) * 'xerox')
        all_types.discard(this_type)

        for subtype in all_types:
            if subtype in self.name:
                raise EquipmentNameError(f'Нельзя оборудование {this_type} назвать {self.name}')


class Printer(Equipment):
    def __init__(self, equipment_name=None, equipment_id=None, equipment_type=None, multicolor=None):
        super().__init__(equipment_name, equipment_id)

        if equipment_type == 1:
            self.equipment_type = 'jet printer'
        elif equipment_type == 2:
            self.equipment_type = 'laser printer'
        else:
            self.equipment_type = 'printer'

        self.multicolor = multicolor

        self.info['equipment type'] = self.equipment_type
        self.info['special']['multicolor'] = self.multicolor


class Scanner(Equipment):
    def __init__(self, equipment_name=None, equipment_id=None, equipment_type=None, automatic_feeder=None):
        super().__init__(equipment_name, equipment_id)

        if equipment_type == 1:
            self.equipment_type = 'broaching scanner'
        elif equipment_type == 2:
            self.equipment_type = 'flatbed scanner'
        elif equipment_type == 3:
            self.equipment_type = 'hand scanner'
        else:
            self.equipment_type = 'scanner'

        self.automatic_feeder = automatic_feeder

        self.info['equipment type'] = self.equipment_type
        self.info['special']['automatic feeder'] = self.automatic_feeder


class Xerox(Equipment):
    def __init__(self, equipment_name=None, equipment_id=None, equipment_type=None):
        super().__init__(equipment_name, equipment_id)

        if equipment_type == 1:
            self.equipment_type = 'desktop xerox'
        elif equipment_type == 2:
            self.equipment_type = 'portable xerox'
        else:
            self.equipment_type = 'xerox'

        self.info['equipment type'] = self.equipment_type


class OtherEquipment(Equipment):
    def __init__(self, equipment_name=None, equipment_id=None, equipment_type='other'):
        super().__init__(equipment_name, equipment_id)
        self.equipment_type = equipment_type
        self.info['equipment type'] = self.equipment_type


class Department(EquipmentWarehouse):
    """Не хочется переопределять все методы, поэтому предположим, что в подразделении тоже есть свой небольшой склад. В
    дальнейшем, можно реализовать перемещение между регистрами (склад подразделения (регистр 1), офис подразделения
    (регистр 2). """

    __department_id = 0

    def __init__(self, name=None):
        Department.__department_id += 1

        self.department_id = Department.__department_id
        if name:
            self.name = name
        else:
            self.name = 'Department ' + str(self.department_id)

        self._storage = {}


class EquipmentNameError(Exception):
    pass


# создание экземпляров оборудования
printer_1 = Printer(equipment_name='HP 123', equipment_type=1, multicolor=True)
printer_2 = Printer(equipment_type=2)
scanner_1 = Scanner()
scanner_2 = Scanner()
xerox_1 = Xerox()
xerox_2 = Xerox()
other_1 = OtherEquipment()

# создание экземпляров подразделений и складов
department_1 = Department()
department_2 = Department()
warehouse_1 = EquipmentWarehouse()
warehouse_2 = EquipmentWarehouse()

# складирование оборудования
warehouse_1.warehousing(printer_1, scanner_1, xerox_1)
other_1.send_to_warehouse(warehouse_1)
warehouse_2.warehousing(printer_2, scanner_2, xerox_2)

print(warehouse_1)
print(warehouse_2)
print(department_1)
print(department_2)
print(':::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')

# списывание оборудования
warehouse_1.write_off(other_1)  # эквивалентно other_1.write_off()
# перемещение оборудования на 2-ой склад
printer_1.send_to_warehouse(warehouse_2)
scanner_1.send_to_warehouse(warehouse_2)
xerox_1.send_to_warehouse(warehouse_2)

print(warehouse_1)
print(warehouse_2)
print(department_1)
print(department_2)
print(':::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')

# проверка информации об оборудовании
print(printer_1)
print(':::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')

# распределение продукции по подразделениям
printer_1.send_to_warehouse(department_1)
printer_2.send_to_warehouse(department_2)

print(warehouse_1)
print(warehouse_2)
print(department_1)
print(department_2)
print(printer_1)

print(':::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')

# Ручной ввод с валидацией (для 5-го задания)

while True:
    number_of_printers = input('Введите количество принтеров для добавления на склад: ')
    number_of_scanners = input('Введите количество сканнеров для добавления на склад: ')
    number_of_xeroxes = input('Введите количество ксероксов для добавления на склад: ')
    try:
        number_of_printers = int(number_of_printers)
        number_of_scanners = int(number_of_scanners)
        number_of_xeroxes = int(number_of_xeroxes)
    except ValueError as err:
        print(f'Ошибка ввода ({err})')
    else:
        for _ in range(number_of_printers):
            warehouse_1.warehousing(Printer())
        for _ in range(number_of_scanners):
            warehouse_1.warehousing(Scanner())
        for _ in range(number_of_xeroxes):
            warehouse_1.warehousing(Xerox())
        break

print(warehouse_1)
print(':::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')

# попытка назвать принтер сканнером
# printer_1 = Printer(equipment_name='multicolor scanner')
