# -*- coding: utf-8 -*-
class ThirdTask:
    def __init__(self, data, options):
        self.data = data
        self.options = options

    def findWorstEAT(self):
        worstOption = {"EAT": 0}
        for val in self.options:
            if val["EAT"] > worstOption["EAT"]:
                worstOption = val
        print "WORST EAT"
        print "RAM Amount: " + worstOption["RamAmount"]
        print "Disk Type: " + worstOption["DiskType"]
        return worstOption

    def findBestEAT(self):
        bestOption = {"EAT": 9999999}
        for val in self.options:
            if val["EAT"] < bestOption["EAT"]:
                bestOption = val
        print "BEST EAT"
        print "RAM Amount: " + bestOption["RamAmount"]
        print "Disk Type: " + bestOption["DiskType"]
        return bestOption

    def calculateDegredation(self, option):
        print "Degredation = (EAT - Base Access Time)/Base Access Time"
        print "Degredation = (" + str(option["EAT"]) + " - " + str(self.data["a"]) + " / " + str(self.data["a"])
        print "Degredation = " + str((option["EAT"]-self.data["a"])/self.data["a"])
        print "\n"
        return (option["EAT"]-self.data["a"])/self.data["a"]

    def convertDegredation(self, degredation):
        return degredation * 100

    def clearOutput(self):
        for val in self.options:
            print "RAM Amount: " + val["RamAmount"] + " GiB"
            print "RAM Cost: £" + str(val["RamCost"])
            print "Disk Type: " + val["DiskType"]
            print "Disk Cost: £" + str(val["DiskCost"])
            print "Disk Speed: " + str(val["DiskSpeed"]) + " MiB/sec"
            print "Total Cost: £" + str(val["TotalCost"])
            print "EAT: " + str(val["EAT"]) + " Nanoseconds"
            if "BestOption" in val:
                print "BEST EAT"
                print "Degredation: " + str(val["BestOption"]["Degredation"]) + "%"
            elif "WorstOption" in val:
                print "WORST EAT"
                print "Degredation: " + str(val["WorstOption"]["Degredation"]) + "%"
            print "\n"

    def run(self):
        bestOption = self.findBestEAT()
        bestDegredation = self.calculateDegredation(bestOption)
        worstOption = self.findWorstEAT()
        worstDegredation = self.calculateDegredation(worstOption)
        for val in self.options:
            if val == bestOption:
                val.update({
                    "BestOption": {
                        "Degredation": self.convertDegredation(bestDegredation)
                    }
                })
            elif val == worstOption:
                val.update({
                    "WorstOption": {
                        "Degredation": self.convertDegredation(worstDegredation)
                    }
                })
        return self.options
