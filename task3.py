# Создайте классы для представления структуры магазина техники.

# Требования:

# Базовый класс Device, который будет представлять общие атрибуты
# для любой техники:

# атрибуты: brand, model, price.
# метод get_info(), который возвращает строку с кратким описанием устройства.
# Дочерние классы:

# Laptop с дополнительными атрибутами ram и storage.
# Smartphone с атрибутами camera_megapixels и battery_capacity.

# Каждый из классов должен переопределить метод get_info()
# для включения специфичной информации.
# Создайте класс Store, содержащий список устройств:

# Метод add_device(device), который добавляет устройство в магазин.
# Метод list_devices(), который выводит информацию обо всех устройствах.
class Device:
    def __init__(self, brand: str, model: str, price: int):
        self.brand = brand
        self.model = model
        self.price = price

    def get_info(self):
        return f"brand: {self.brand}, model: {self.model}, price: {self.price}"

    def __repr__(self):
        return f"brand: {self.brand}, model: {self.model}, price: {self.price}"


class Laptop(Device):
    def __init__(self, brand, model, price, ram: int, storage: int):
        super().__init__(brand, model, price)
        self.ram = ram
        self.storage = storage

    def get_info(self):
        return f"{super().get_info()}" \
               f" ram: {self.ram}, storage: {self.storage}"

    def __repr__(self):
        return f"{super().__repr__()}," \
               f" ram: {self.ram}, storage: {self.storage}"


class Smartphone(Device):
    def __init__(self, brand, model, price, camera_megapixels: int, battery_capacity: int):
        super().__init__(brand, model, price)
        self.camera_megapixels = camera_megapixels
        self.battery_capacity = battery_capacity

    def get_info(self):
        return f"{super().get_info()}," \
               f" camera_megapixels: {self.camera_megapixels}," \
               f" battery_capacity: {self.battery_capacity}"

    def __repr__(self):
        return f"{super().__repr__()}," \
               f" camera_megapixels: {self.camera_megapixels}," \
               f" battery_capacity: {self.battery_capacity}"


class Store:
    def __init__(self, devices=None):
        if devices is None:
            devices = []
        self.devices = devices

    def add_device(self, device):
        if not isinstance(device, (Smartphone, Laptop, Device)):
            raise ValueError
        self.devices.append(device)

    def list_devices(self):
        list_of_devices = []
        for i in self.devices:
            list_of_devices.append(i)
        return list_of_devices


if __name__ == "__main__":
    device1 = Device("Nokia", "3310", 100)
    laptop1 = Laptop("Apple", "Mac", 1500, 32, 2000)
    smartphone1 = Smartphone("Apple", "Iphone 16", 1000, 48, 16000)

    devices_list = []
    store = Store(devices_list)

    store.add_device(smartphone1)
    store.add_device(device1)
    store.add_device(laptop1)

    print(store.list_devices())
