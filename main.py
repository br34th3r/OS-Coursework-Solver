# -*- coding: utf-8 -*-
from FirstTask import FirstTask
from SecondTask import SecondTask
from ThirdTask import ThirdTask

def separate():
    print "###############################################\n"

def main():
    data = {
        "a": 200,
        "p": {
            "budget": 310,
            "pMin": 0.0000017,
            "r": 0.000042,
            "sMin": 0.00013,
            "d": 0.24
        },
        "disks": {
            'HD': {
                "cost": 45,
                "speed": 120
            },
            'SSD': {
                "cost": 110,
                "speed": 300
            },
            'XSSSD': {
                "cost": 245,
                "speed": 420
            }
        },
        "ram": {
            '4': 60,
            '8': 120,
            '16': 240
        }
    }

    separate()

    # Task 1 - OUTPUT
    print "TASK 1\n"
    task1 = FirstTask(data)
    affordable = task1.run()
    task1.clearOutput()
    separate()

    # Task 2 - OUTPUT
    print "TASK 2\n"
    task2 = SecondTask(data, affordable)
    affordable = task2.run()
    separate()

    # Task 3 - OUTPUT
    print "TASK 3\n"
    task3 = ThirdTask(data, affordable)
    affordable = task3.run()
    task3.clearOutput()
    separate()

if __name__ == "__main__" : main()
