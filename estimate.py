import math

print("Project Estimator: This tool will help you estimate the time required for your project.")
print("Estimates are based on previous projects and may vary depending on project complexity.")
print("* Current scan averages are based on the use of 6 laptops and 5 scanners.")
print("* Actual times may vary depending on staffing, equipment, and document complexity.")
print()

# BOXES
bankerBoxes = int(input("How many banker boxes are you using? "))
legalBoxes = int(input("How many legal boxes are you using? "))

totalBoxes = bankerBoxes + legalBoxes

# STAFF
preppers = int(input("How many people will be prepping? "))
scanners = int(input("How many people will be scanning? "))

# CONTINGENCY
contingencyPerc = float(input("What contingency percentage would you like? "))
contingencyMult = 1 + (contingencyPerc / 100)

# PREP
# avg labor time per box: banker = 2hr, legal = 3hr
prepAvg = (bankerBoxes * 2) + (legalBoxes * 3)

prepTeam = prepAvg / preppers

# SCAN
# avg scan labor per box: banker = 1.5hr, legal = 2.5hr
scanAvg = (bankerBoxes * 1.5) + (legalBoxes * 2.5)

scanTeam = scanAvg / scanners

# CONTINGENCY
prepContingency = prepTeam * contingencyMult
scanContingency = scanTeam * contingencyMult

# PREP DAYS
projectDays4 = math.ceil(prepTeam / 4)
projectDays6 = math.ceil(prepTeam / 6)
projectDays8 = math.ceil(prepTeam / 8)

projectDays4Contingency = math.ceil(prepContingency / 4)
projectDays6Contingency = math.ceil(prepContingency / 6)
projectDays8Contingency = math.ceil(prepContingency / 8)

# SCAN DAYS
projectDays4Scan = math.ceil(scanTeam / 4)
projectDays6Scan = math.ceil(scanTeam / 6)
projectDays8Scan = math.ceil(scanTeam / 8)

projectDays4ScanContingency = math.ceil(scanContingency / 4)
projectDays6ScanContingency = math.ceil(scanContingency / 6)
projectDays8ScanContingency = math.ceil(scanContingency / 8)


print("\n*** PROJECT ESTIMATE ***")
print(f"Total Quantity of Boxes: {totalBoxes}")
print()

print("-- PREP --")
print(f"Total Prep Labor Required: {math.ceil(prepAvg)} hours")
print(f"....With {preppers} Prep Staff: {math.ceil(prepTeam)} hours Each")
print(f"....With {contingencyPerc:.0f}% contingency: {math.ceil(prepContingency)} hours Each")
print()

print("-- SCAN --")
print(f"Total Scan Labor Required: {math.ceil(scanAvg)} hours")
print(f"....With {scanners} Scan Staff: {math.ceil(scanTeam)} hours Each")
print(f"....With {contingencyPerc:.0f}% contingency: {math.ceil(scanContingency)} hours Each")
print()

print("-- ESTIMATED DURATION --")
print()
print(f"Prep Days With {contingencyPerc:.0f}% contingency:")
print(f"4-hour shift: {projectDays4Contingency} workdays")
print(f"6-hour shift: {projectDays6Contingency} workdays")
print(f"8-hour shift: {projectDays8Contingency} workdays")
print()
print(f"Scan Days With {contingencyPerc:.0f}% contingency:")
print(f"4-hour shift: {projectDays4ScanContingency} workdays")
print(f"6-hour shift: {projectDays6ScanContingency} workdays")
print(f"8-hour shift: {projectDays8ScanContingency} workdays")