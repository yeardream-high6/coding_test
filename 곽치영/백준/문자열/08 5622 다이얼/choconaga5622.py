dials = {
    2: "ABC",
    3: "DEF",
    4: "GHI",
    5: "JKL",
    6: "MNO",
    7: "PQRS",
    8: "TUV",
    9: "WXYZ",
}
chr_to_num = {}
for i, s in dials.items():
    for c in s:
        chr_to_num[c] = i

line = input()
print(sum(chr_to_num[c] + 1 for c in line))