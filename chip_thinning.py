from math import sqrt

def feed_per_tooth(CT, D, RDOC):
    "Returns inches per tooth given desired chip thickness and radial depth of cut."
    return(CT * D) / (2 * sqrt((D * RDOC) - RDOC*RDOC))

if __name__ == "__main__":
    while True:
        CT = float(input("\nDesired chip thickness:"))
        D = float(input("\nTool Diameter:"))
        RDOC = float(input("\nRadial depth of cut:"))
        print("\nFeed per tooth:\n\n", round(feed_per_tooth(CT, D, RDOC), 5), "\n")
