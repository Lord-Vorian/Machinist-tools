"""
If milling an internal corner, feedrate must be reduced due to the increased
radial engagement.
Ref:
https://www.harveyperformance.com/in-the-loupe/speeds-and-feeds-101/
"""


def feed_reduction(cr,tr):
    cr, tr = float(cr), float(tr)
    return (cr-tr)/cr

if __name__ == "__main__":
    while True:
        cr = input("\nRadius of internal corner: ")
        tr = input("\nRadius of tool: ")
        print("\n\nMultiply feed by:", round(feed_reduction(cr, tr), 3), "\n\n")

