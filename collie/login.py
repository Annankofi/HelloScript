# -*- coding: UTF-8 -*-
# !!!WARNNING!!! This file was generated by collie tools.
# !!!WARNNING!!! Do not modify until you know what you are doing.

import pycollie

class Case(pycollie.TestCase):
    def setUp(self):
        self.dut_0 = self.get_device()

    def tearDown(self):
        pass

    def testCase(self):
        while True:
            #Touch (126, 138) Click
            self.dut_0.touch(126, 138)

            #Wait 4324ms
            pycollie.sleep(4324)

            #Touch (197, 721) Click
            self.dut_0.touch(197, 721)

            #Wait 2071ms
            pycollie.sleep(2071)

            #Touch (57, 53) Click
            self.dut_0.touch(57, 53)

            #Wait 1580ms
            pycollie.sleep(1580)

            #Touch (119, 136) Click
            self.dut_0.touch(119, 136)

            #Wait 1321ms
            pycollie.sleep(1321)

            #Touch (244, 877) Click
            self.dut_0.touch(244, 877)


if __name__ == "__main__":
    pycollie.main()