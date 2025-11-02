from esphome.components import binary_sensor
import esphome.config_validation as cv
import esphome.codegen as cg
from esphome.const import ICON_RESTART
from .. import levoit_ns, CONF_LEVOIT_ID, Levoit

DEPENDENCIES = ["levoit"]
CODEOWNERS = ["@acvigue"]

CONFIG_SCHEMA = (
    cv.Schema({
        cv.GenerateID(CONF_LEVOIT_ID): cv.use_id(Levoit),
        cv.Optional("out_of_water"): binary_sensor.binary_sensor_schema(),
    })
)

async def to_code(config):
    parent = await cg.get_variable(config[CONF_LEVOIT_ID])
    if out_of_water := config.get("out_of_water"):
        var = await binary_sensor.new_binary_sensor(config("out_of_water"))
        cg.add(parent.set_up_bsensor(var))