from Sensor import TempuratureSensor, LightSensor

temp = TemperatureSensor("Temp1")
light = LightSensor("Light")

print(f"Temp: {temp.read()}")
print(f"Light: {Light.read()}")
