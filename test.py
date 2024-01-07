from CYK_Paser import Grammar

kalimat_baku_valid = 0
kalimat_baku_tidak_valid = 0

kalimat_tidak_baku_valid = 0
kalimat_tidak_baku_tidak_valid = 0

tidak_ada_rule = 0

print("Kalimat Baku Tidak Valid:")
for line in open("kalimat_baku.txt"):
  g = Grammar()
  try:
    if g.parse(line.lower()):
      kalimat_baku_valid += 1
    else:
      kalimat_baku_tidak_valid += 1
      print(line)
  except(ValueError):
    tidak_ada_rule += 1

print("============================================")
print("Kalimat Tidak Baku Valid:")
for line in open("kalimat_tidak_baku.txt"):
  g = Grammar()
  try:
    if g.parse(line.lower()):
      kalimat_tidak_baku_valid += 1
      print(line)
    else:
      kalimat_tidak_baku_tidak_valid += 1
  except(ValueError):
    tidak_ada_rule += 1

print(f"kalimat baku valid: {kalimat_baku_valid}")
print(f"kalimat baku tidak valid: {kalimat_baku_tidak_valid}")
print(f"kalimat tidak baku valid: {kalimat_tidak_baku_valid}")
print(f"kalimat tidak baku tidak valid: {kalimat_tidak_baku_tidak_valid}")
print(f"tidak ada rule: {tidak_ada_rule}")