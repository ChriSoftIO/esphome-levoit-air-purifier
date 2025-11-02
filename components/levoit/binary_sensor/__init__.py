from esphome.components import binary_sensor
import esphome.config_validation as cv
import esphome.codegen as cg
from esphome.const import ICON_RESTART
from .. import levoit_ns, CONF_LEVOIT_ID, Levoit

DEPENDENCIES = ["levoit"]
CODEOWNERS = ["@acvigue"]

LevoitBinarySensor = levoit_ns.class_("LevoitBinarySensor", cg.Component, binary_sensor.BinarySensor)

CONFIG_SCHEMA = (
    cv.Schema({
        cv.GenerateID(CONF_LEVOIT_ID): cv.use_id(Levoit),
        cv.Optional("out_of_water"): binary_sensor.binary_sensor_schema(LevoitBinarySensor),
    })
)

async def to_code(config):
    var = await cg.get_variable(config[CONF_LEVOIT_ID])

    if "out_of_water" in config:
        oow = await binary_sensor.new_binary_sensor(config["out_of_water"])
        cg.add(var.set_button(oow))