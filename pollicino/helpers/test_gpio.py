import unittest

import gpio

# BOARD = PHISICAL PIN NUMBER
# BCM = LOGICAL GPIO NUMBER
# ie. BOARD 3 == GPIO 2

PIN_BMC = 24
PIN_BOARD = 18
PIV_VALUE = 1


class TestGPIO(unittest.TestCase):
    def test_set_get_board_ok(self):
        gpio.set("BOARD", PIN_BOARD, PIV_VALUE)
        value = gpio.get("BOARD", PIN_BOARD)
        self.assertEqual(value, PIV_VALUE)

    def test_set_get_bmc_ok(self):
        gpio.set("BCM", PIN_BMC, PIV_VALUE)
        value = gpio.get("BCM", PIN_BMC)
        self.assertEqual(value, PIV_VALUE)

    def test_set_get_mix_1_ok(self):
        gpio.set("BOARD", PIN_BOARD, PIV_VALUE)
        value = gpio.get("BCM", PIN_BMC)
        self.assertEqual(value, PIV_VALUE)

    def test_set_get_mix_2_ok(self):
        gpio.set("BCM", PIN_BMC, PIV_VALUE)
        value = gpio.get("BOARD", PIN_BOARD)
        self.assertEqual(value, PIV_VALUE)


if __name__ == '__main__':
    unittest.main()
