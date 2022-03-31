answers = [65, 66, 67, 68, 69]

def on_button_pressed_a():
    radio.send_value("answer", answers[0])
    radio.received_packet(RadioPacketProperty.SERIAL_NUMBER)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    radio.send_value("answer", answers[1])
    radio.received_packet(RadioPacketProperty.SERIAL_NUMBER)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_pin_pressed_p0():
    radio.send_value("answer", answers[2])
    radio.received_packet(RadioPacketProperty.SERIAL_NUMBER)
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

def on_pin_pressed_p1():
    radio.send_value("answer", answers[3])
    radio.received_packet(RadioPacketProperty.SERIAL_NUMBER)
input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)

def on_pin_pressed_p2():
    radio.send_value("answer", answers[4])
    radio.received_packet(RadioPacketProperty.SERIAL_NUMBER)
input.on_pin_pressed(TouchPin.P2, on_pin_pressed_p2)