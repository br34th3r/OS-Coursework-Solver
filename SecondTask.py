# -*- coding: utf-8 -*-
class SecondTask:
    def __init__(self, data, options):
        self.data = data
        self.options = options

    def secondsToNanoseconds(self, value):
        return value * 1000000000

    def calculatePageFault(self, ram):
        print "p = pMin + r/R"
        print "p = " + str(self.data["p"]["pMin"]) + " + " + str(self.data["p"]["r"]) + " / " + str(ram)
        print "p = " + str(self.data["p"]["pMin"] + self.data["p"]["r"]/ram) + "\n"
        return self.data["p"]["pMin"] + self.data["p"]["r"]/ram

    def calculateServiceTime(self, diskSpeed):
        print "s = sMin + d/D"
        print "s = " + str(self.data["p"]["sMin"]) + " + " + str(self.data["p"]["d"]) + " / " + str(diskSpeed)
        print "s = " + str(self.data["p"]["sMin"] + self.data["p"]["d"]/diskSpeed) + "\n"
        return self.data["p"]["sMin"] + self.data["p"]["d"]/diskSpeed

    def calculateEAT(self, p, s):
        print "EAT = a + p x s"
        print "EAT = " + str(self.data["a"]) + " + " + str(p) + " x " + str(s)
        print "EAT = " + str(round(self.data["a"] + p * s, 3)) + " Nanoseconds"
        print "\n"
        return round(self.data["a"] + p * s, 3)

    def clearOutput(self):
        for val in self.options:
            print "RAM Amount: " + val["RamAmount"] + " GiB"
            print "RAM Cost: £" + str(val["RamCost"])
            print "Disk Type: " + val["DiskType"]
            print "Disk Cost: £" + str(val["DiskCost"])
            print "Disk Speed: " + str(val["DiskSpeed"]) + " MiB/sec"
            print "Total Cost: £" + str(val["TotalCost"])
            print "EAT: " + str(val["EAT"]) + " Nanoseconds"
            print "\n"

    def run(self):
        for val in self.options:
            print "For Values: " + str(val["RamAmount"]) + " GiB of RAM and " + val["DiskType"] + " Disk:"
            p = self.calculatePageFault(int(val["RamAmount"]))
            s = self.calculateServiceTime(val["DiskSpeed"])
            s = self.secondsToNanoseconds(s)
            EAT = self.calculateEAT(p, s)
            val.update({"EAT": EAT})
        return self.options
