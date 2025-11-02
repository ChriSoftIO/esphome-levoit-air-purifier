#pragma once

#include "esphome/core/component.h"
#include "esphome/components/levoit/levoit.h"
#include "esphome/components/binary_sensor/binary_sensor.h"

namespace esphome {
namespace levoit {


class LevoitBinarySensor : public Component, public binary_sensor::BinarySensor {
 public:
  LevoitBinarySensor(Levoit *parent) : parent_(parent) {}
  void set_up_bsensor(binary_sensor::BinarySensor* sensor) { up_bsensor_ = sensor; }
 protected:
  Levoit *parent_;t
  binary_sensor::BinarySensor* up_bsensor_{nullptr};
};

}  // namespace levoit
}  // namespace esphome
