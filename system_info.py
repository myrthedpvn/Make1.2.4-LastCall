# import
import platform

__author__ = "Myrthe Diepeveen"
__email__ = "myrthe.diepeveen@student.kdg.be"
__status__ = "Development"


def main():
    # Architecture
    print("Architecture: " + platform.architecture()[0])

    # machine
    print("Machine: " + platform.machine())

    # node
    print("Node: " + platform.node())

    # system
    print("System: " + platform.system())

    print("Processors: ")
    with open("/proc/cpuinfo", "r") as f:
        info = f.readlines()                                                                 #To give information

    cpuinfo = [x.strip().split(":")[1] for x in info if "model name" in x]
    for index, item in enumerate(cpuinfo):
        print("    " + str(index) + ": " + item)

if __name__ == '__main__':  # code to execute if called from command-line
    main()
