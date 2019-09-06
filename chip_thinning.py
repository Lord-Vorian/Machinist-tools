from math import sqrt
from time import sleep

CT = float(input("\nDesired chip thickness:"))
D = float(input("\nTool Diameter:"))
RDOC = float(input("\nRadial depth of cut:"))

feed_per_tooth = (CT * D) / (2 * sqrt((D * RDOC) - RDOC*RDOC))

print("\nFeed per tooth:\n\n",round(feed_per_tooth,5),"\n")

sleep(30)
