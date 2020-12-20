import json


with open("ent_0002.json") as json_file:
	jsonf = json.load(json_file)

cp1_sd_pure = 0
cp1_dys_nosd = 0
cp1_sd_nopure = 0
cp1_multiple_nosd = 0
multiple_sd = 0


syntagms = ["lex","sprep","sv","sn"]

for occ in jsonf:
	if jsonf[occ]["position_syntaxique"] == "sd" and jsonf[occ]["couplé_dys"] != 'y':
		cp1_sd_pure +=1

	if jsonf[occ]["position_syntaxique"] == "sd" and jsonf[occ]["couplé_dys"] == 'y':
		cp1_sd_nopure +=1

	if any(jsonf[occ]["position_syntaxique"] in s for s in syntagms)and jsonf[occ]["couplé_SD"] != 'y':
		cp1_dys_nosd +=1

	if jsonf[occ]["couplé_dys"] == 'y' and jsonf[occ]["couplé_SD"] == 'n':
		cp1_multiple_nosd +=1

	if jsonf[occ]["couplé_SD"] == 'y' and jsonf[occ]["couplé_dys"] == 'y':
		multiple_sd +=1

	if jsonf[occ]["couplé_dys"] == 'y' and jsonf[occ]["position_syntaxique"] == 'sd':
		multiple_sd +=1


print("multiple dys + no sd :" + str(cp1_multiple_nosd))
print("mulitple dys + sd: " + str(multiple_sd))


import scipy.stats as stats
oddsratio, pvalue = stats.fisher_exact([[27+64, 5+41], [0, 21+87]])
print(pvalue)