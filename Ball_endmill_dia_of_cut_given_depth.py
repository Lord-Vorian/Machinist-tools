from math import sqrt

def depth_dia(tool_dia, DOC):
    "Returns the diameter cut a ball endmill will leave given a Depth Of Cut"
    radius = float(tool_dia) / 2
    DOC = float(DOC)
    return 2 * sqrt(radius**2 - (radius - DOC)**2)

if __name__ == "__main__":
    while True:
        tool_dia = input("\nDiameter of ball EM: ")
        DOC = input("\nDepth of cut: ")
        dia_of_cut = round(depth_dia(tool_dia, DOC),5)
        print("\nDiameter of cut at this depth:\n", dia_of_cut,"\n\n")
