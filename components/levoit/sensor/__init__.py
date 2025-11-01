import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor, binary_sensor
from esphome.const import (
    CONF_OUTPUT_ID,
    CONF_PM_2_5,
    UNIT_MICROGRAMS_PER_CUBIC_METER,
    ICON_BLUR,
    DEVICE_CLASS_PM25,
    DEVICE_CLASS_AQI,
    STATE_CLASS_MEASUREMENT,
    DEVICE_CLASS_HUMIDITY,
    UNIT_PERCENT
)

from .. import levoit_ns, CONF_LEVOIT_ID, Levoit

AUTO_LOAD = [ "binary_sensor", "sensor" ]

DEPENDENCIES = ["levoit"]
CODEOWNERS = ["@acvigue"]

CONF_AIR_QUALITY = "air_quality"

LevoitSensor = levoit_ns.class_("LevoitSensor", cg.Component, sensor.Sensor)
LevoitSensorPurpose = levoit_ns.enum("LevoitSensorPurpose")

CONFIG_SCHEMA = (
    cv.Schema({
        cv.GenerateID(CONF_LEVOIT_ID): cv.use_id(Levoit),
        cv.Optional(CONF_PM_2_5): sensor.sensor_schema(LevoitSensor, unit_of_measurement=UNIT_MICROGRAMS_PER_CUBIC_METER, icon=ICON_BLUR, accuracy_decimals=1, device_class=DEVICE_CLASS_PM25, state_class=STATE_CLASS_MEASUREMENT),
        cv.Optional(CONF_AIR_QUALITY): sensor.sensor_schema(LevoitSensor, icon=ICON_BLUR, accuracy_decimals=0, device_class=DEVICE_CLASS_AQI, state_class=STATE_CLASS_MEASUREMENT),
        cv.Optional("humidity"): sensor.sensor_schema(LevoitSensor, unit_of_measurement=UNIT_PERCENT, accuracy_decimals=0, device_class=DEVICE_CLASS_HUMIDITY, state_class=STATE_CLASS_MEASUREMENT),
        cv.Optional("out_of_water"): binary_sensor.binary_sensor_schema(),
    })
)


async def to_code(config):
    parent = await cg.get_variable(config[CONF_LEVOIT_ID])

    if pm25 := config.get(CONF_PM_2_5):
        var = await sensor.new_sensor(pm25, parent, LevoitSensorPurpose.PM25)
        await cg.register_component(var, pm25)

    if air_quality := config.get(CONF_AIR_QUALITY):
        var = await sensor.new_sensor(air_quality, parent, LevoitSensorPurpose.AIR_QUALITY)
        await cg.register_component(var, air_quality)

    if humidity := config.get("humidity"):
        var = await sensor.new_sensor(humidity, parent, LevoitSensorPurpose.HUMIDITY)
        await cg.register_component(var, humidity)

    if out_of_water := config.get("out_of_water"):
        sens = await binary_sensor.new_binary_sensor(config["out_of_water"])
        cg.add(parent.set_up_bsensor(sens))
