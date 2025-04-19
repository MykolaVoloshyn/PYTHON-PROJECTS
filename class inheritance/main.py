class Gadget:
    def __init__(self, screen_size, battery_capacity, usb_type):
        self.screen_size = screen_size
        self.battery_capacity = battery_capacity
        self.usb_type = usb_type


class SmartWatch(Gadget):
    def __init__(self, screen_size, battery_capacity, usb_type, has_heart_rate_monitor, ecg_sensors):
        super().__init__(screen_size, battery_capacity, usb_type)
        self.has_heart_rate_monitor = has_heart_rate_monitor
        self.ecg_sensors = ecg_sensors


class SmartPhone(Gadget):
    def __init__(self, screen_size, battery_capacity, usb_type, processor, main_camera, nfc_module):
        super().__init__(screen_size, battery_capacity, usb_type)
        self.processor = processor
        self.main_camera = main_camera
        self.nfc_module = nfc_module
