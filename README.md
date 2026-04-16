# Signals

Physical signaling experiments on MicroPython—binary transmission over GPIO, pulse-based light patterns, and button-driven “dialer” input.

## What’s in this repo

| File | Role |
|------|------|
| `Binary Incoder.py` | **Transmitter:** encodes a string to 8-bit ASCII and sends it bit-by-bit on a **clock** + **data** line (GPIO 16 clock out, GPIO 15 data out). |
| `Binary Decoder.py` | **Receiver:** samples on clock edges, rebuilds bytes, and prints the message after a short idle period. |
| `Light Number.py` | Drives a laser (or LED) on **GPIO 17** with timed pulse bursts—useful for visible-light signaling demos. |
| `Phone.py` / `Receving Light.py` | Button on GPIO counts taps into digits (multi-tap style) and prints a `Calling: …` line when input settles. |

Hardware assumptions match the scripts (e.g. encoder/decoder use pins **15** and **16**; adjust `Pin(...)` if your wiring differs).

## Requirements

- A board running **MicroPython** with the `machine` module (e.g. Raspberry Pi Pico).
- Optional: laser module or LED, push button(s), jumper wires.

## How to run

1. Flash MicroPython onto your board ([Raspberry Pi documentation](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html)).
2. Copy the `.py` file you want onto the device (Thonny, `mpremote`, or drag-and-drop on supported boards).
3. Open **Run** / REPL—or rename `main.py` on the device if you want it to start on boot.

Use **either** the encoder **or** the decoder on two boards (or loopback with care) so clock/data directions stay consistent.

## Project name ideas

If you want a public-facing title beyond **Signals**, these also fit the same work:

- **Signals** — short, matches the repo; covers light, electricity, and “calling.”
- **GPIO Beacon** — emphasizes visible/pin-level output.
- **Pulse Lab** — highlights timing, lasers, and clocked bits.

---

*Portfolio piece: embedded Python, timing, and simple protocols without a network stack.*
