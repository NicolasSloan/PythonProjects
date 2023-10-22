import datetime
import pytz

PortlandTz = pytz.timezone("America/Los_Angeles")
PortlandTime = datetime.datetime.now(PortlandTz)

LondonTz = pytz.timezone("Europe/London")
LondonTime = datetime.datetime.now(LondonTz)

NYCTz = pytz.timezone("America/New_York")
NYCTime = datetime.datetime.now(NYCTz)


print("Current Local Times:")
print("\nPortland: " + PortlandTime.strftime("%I:%M%p"))
print("\nLondon: " + LondonTime.strftime("%I:%M%p"))
print("\nNew York City: " + NYCTime.strftime("%I:%M%p"))

print(PortlandTime)
