import xml.etree.ElementTree as ET

import json

root = ET.parse('ESLO1_ENT_002_C.trs').getroot()

from bs4 import BeautifulSoup  

xmlstr = ET.tostring(root, encoding='utf8', method='xml')


soup = BeautifulSoup(xmlstr)


numOfEuh = soup.text.count("euh")

turns = soup.findAll("turn")


print(len(turns))

dic = {}


i = 0 
for turn in turns:
	for occ in range(turn.text.count("euh")):

		if i >= 0:

			entry = {"loc": turn["speaker"], "contexte" : "entretient" ,"position_syntaxique" : "", "couplé_SD" : False, "couplé_dys" : False}

			try:

				print(turn["speaker"])
				print(turn)

				skip = input("skip ? (y/n)")

				if skip == 'y' :
					print('\n\n' + str(i) + ' out of ' + str(numOfEuh) + ' euh')
					i+=1
					continue

				posyn = input("Position syntaxique ?")
				entry["position_syntaxique"] = posyn
				ans = input("Couplé ac dysflence en début de segment ? (y/n")
				entry["couplé_SD"] = ans
				ans = input("Couplé ac dysflences? (y/n")
				entry["couplé_dys"] = ans
				dic[i] = entry

				i+=1

				print(entry)
			except:
				print("turn speaker not avaible")
				i+=1

			with open("CONSCMPP_713.json", 'w') as outfile:
				json.dump(dic, outfile, indent=4, separators=(',', ': '), sort_keys=True)

			outfile.close()

		print('\n\n' + str(i) + ' out of ' + str(numOfEuh) + ' euh')

