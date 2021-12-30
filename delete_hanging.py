from pyEarnapp import EarnApp
AUTH_TOKENS = []

for auth in AUTH_TOKENS:
    api = EarnApp(auth)
    devices_info = api.get_devices_info()
    for device in devices_info.devices:
        print(device.uuid, device.banned.is_banned)
