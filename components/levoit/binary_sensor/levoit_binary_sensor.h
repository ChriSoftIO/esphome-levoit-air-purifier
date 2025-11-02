#pragma once

#include "esphome/core/component.h"
#include "esphome/components/levoit/levoit.h"
#include "esphome/components/binary_sensor/binary_sensor.h"

namespace esphome {
namespace levoit {


class LevoitSBinarySensor : public Component, public binary_sensor::BinarySensor {
 public:
  LevoitSBinarySensor(Levoit *parent) : parent_(parent) {}
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
