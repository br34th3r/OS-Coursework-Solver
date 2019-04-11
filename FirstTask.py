# -*- coding: utf-8 -*-
class FirstTask:
    def __init__(self, data):
        self.affordable = []
        self.data = data

    def getAffordable(self):
        return self.affordable

    def clearOutput(self):
        for val in self.affordable:
            print "RAM Amount: " + val["RamAmount"] + " GiB"
            print "RAM Cost: £" + str(val["RamCost"])
            print "Disk Type: " + val["DiskType"]
            print "Disk Cost: £" + str(val["DiskCost"])
            print "Disk Speed: " + str(val["DiskSpeed"]) + " MiB/sec"
            print "Total Cost: £" + str(val["TotalCost"])
            print "\n"

    def run(self):
        for ramOption, ramCost in self.data["ram"].iteritems():
            for diskName, diskInfo in self.data["disks"].iteritems():
                if diskInfo["cost"] + ramCost < self.data["p"]["budget"]:
                    self.affordable.append(
                        {
                            "RamAmount": ramOption,
                            "RamCost": ramCost,
                            "DiskType": diskName,
                            "DiskCost": diskInfo["cost"],
                            "DiskSpeed": diskInfo["speed"],
                            "TotalCost": ramCost + diskInfo["cost"]
                        }
                    )
        return self.affordable
