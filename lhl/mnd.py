instuctionSteps = [
    "turn left",
    "go straight for 2 blocks",
    "turn right",
    "keep going until you see the dog statue",
    "turn right",
    "turn right again",
    "park right on the sidewak"
]

instructions = "Frist, "

for nextInstruction in instuctionSteps:
    instructions = instructions + nextInstruction + ", then "

print(instructions + "you're there!")

instructionStepsButScreemed = []

for nextInstruction in instuctionSteps:
    upperInstrustion = nextInstruction.upper()
    instructionStepsButScreemed.append(upperInstrustion)

print(instructionStepsButScreemed)