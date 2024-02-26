# R1 = 150000
# Rt = 115000

# R2 = Rt/(1-Rt/R1)

# print(R2)


R1 = 150000
R2 = 510000
Rt = 1/(1/R1 + 1/R2)

print(Rt)

R1 = 115
R2 = 22.1
VCC = 5

Vout = R2/(R1+R2)
print(Vout)