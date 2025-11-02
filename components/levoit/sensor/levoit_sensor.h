#pragma once

#include "esphome/core/component.h"
#include "esphome/components/levoit/levoit.h"
#include "esphome/components/sensor/sensor.h"
#include "esphome/components/binary_sensor/binary_sensor.h"

namespace esphome {
namespace levoit {

enum LevoitSensorPurpose : uint8_t { PM25, AIR_QUALITY, HUMIDITY };

class LevoitSensor : public Component{
 public:
  LevoitSensor(Levoit *parent, LevoitSensorPurpose purpose) : parent_(parent), purpose_(purpose) {}
  void setup() override;
  void dump_config() override;

  void set_button(binary_sensor::BinarySensor* button) {
    this->button_ = button;
  }

 protected:
  Levoit *parent_;
  LevoitSensorPurpose purpose_;
  binary_sensor::BinarySensor* button_{nullptr};
};

}  // namespace levoit
}  // namespace esphome
