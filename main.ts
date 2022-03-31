let answers = [65, 66, 67, 68, 69]
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    radio.sendValue("answer", answers[0])
    radio.receivedPacket(RadioPacketProperty.SerialNumber)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    radio.sendValue("answer", answers[1])
    radio.receivedPacket(RadioPacketProperty.SerialNumber)
})
input.onPinPressed(TouchPin.P0, function on_pin_pressed_p0() {
    radio.sendValue("answer", answers[2])
    radio.receivedPacket(RadioPacketProperty.SerialNumber)
})
input.onPinPressed(TouchPin.P1, function on_pin_pressed_p1() {
    radio.sendValue("answer", answers[3])
    radio.receivedPacket(RadioPacketProperty.SerialNumber)
})
input.onPinPressed(TouchPin.P2, function on_pin_pressed_p2() {
    radio.sendValue("answer", answers[4])
    radio.receivedPacket(RadioPacketProperty.SerialNumber)
})
