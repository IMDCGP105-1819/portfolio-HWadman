my_fakename = "Harry Wadman"
my_realage = 18
my_heightwhenstanding = 9999 # inches
my_weightwhenonmars = 9999 # pounds
my_thirdeye = "Blue"
my_wig = "Blond"

is_heavyonmars = my_weightwhenonmars > 3000

print(f"Let's talk about {my_fakename}.")
print(f"He is {my_heightwhenstanding} inches tall.")
print(f"He is {my_weightwhenonmars} pounds heavy.")
print(f"It is {is_heavyonmars} that he is overweight.")
print(f"He's got {my_thirdeye} eyes and {my_wig} hair.")

total = my_realage + my_heightwhenstanding + my_weightwhenonmars
print(f"If I add {my_realage}, {my_heightwhenstanding} and {my_weightwhenonmars} I get {total}")

my_heightwhenstandingcentimetre = my_heightwhenstanding * 2.54
my_weightwhenonmarskilogram = my_weightwhenonmars * 0.453592

print(f"His height in centimetres is {my_heightwhenstandingcentimetre}")
print(f"His weight in kilograms is {my_weightwhenonmarskilogram}")
