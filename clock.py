###################################################
#                    !WICHTIG!                    #
# Diese Version der Uhr ist fuer den Emulater des #
#                SenseHats ausgelegt!             #
#     Falls Sie die Uhr fuer ein normales Hat     #
# benutzen wollen aender Sie Zeile 11 einfach in: #
#                                                 #
#         from sense_hat import SenseHat          #
###################################################

from sense_emu import SenseHat											#import des Emulatormoduls
from time import sleep													#import der Wartefunktion des Moduls time
from time import strftime												#import der strftime-Funktion des Moduls time
																		#"""strftime erzeugt eine Liste mit von den Teilen der Zeit""" bsp:%H, %M, %S, usw.
																		#mehr in den python-docs

sense = SenseHat()														#erzeugen des Emulators
sense.clear()															#zuruecksetzen der vorigen Session des Emulators

black = (0, 0, 0)														#Farben werden festgelegt """Syntax: (rot-Wert, gruen-Wert, blau-Wert)"""
edge = (255, 255, 255)
paper = (150, 150, 150)
h_col = (0, 0, 255)
m_col = (0, 200, 100)
point = (0, 200, 200)

#belegen der einzelnen Segmente der Anzeige
"""m steht fuer Minute und h fuer Stunde"""
m_quarter = [['00', '01', '02'], ['03', '04', '05'], ['06', '07', '08'], ['09', '10', '11'], ['12', '13', '14']]
m_half = [['15', '16', '17'], ['18', '19', '20'], ['21', '22', '23'], ['24', '25', '26'], ['27', '28', '29']]
m_quarterto = [['30', '31', '32'], ['33', '34', '35'], ['36', '37', '38'], ['39', '40', '41'], ['42', '43', '44']]
m_oclock = [['45', '46', '47'], ['48', '49', '50'], ['51', '52', '53'], ['54', '55', '56'], ['57', '58', '59']]

h_quarter = ['00', '01', '02', '12', '13', '14']
h_half =  ['03', '04', '05', '15', '16', '17']
h_quarterto = ['06', '07', '08', '18', '19', '20']
h_oclock = ['09', '10', '11', '21', '22', '23']

mid = [['57', '58', '59', '00', '01', '02', '03'], ['04', '05', '06', '07', '08', '09'], ['10', '11'], ['12', '13', '14', '15', '16', '17', '18'], ['19', '20', '21', '22', '23', '24'], ['25', '26'], ['27', '28', '29', '30', '31', '32', '33'], ['34', '35', '36', '37', '38', '39'], ['40', '41'], ['42', '43', '44', '45', '46', '47', '48'], ['49', '50', '51', '52', '53', '54'], ['55', '56']]

#Definitionen
def m0(m):																#innerster Ring des Minutenzeigers
	if m in m_quarter[0]:
		clock[28] = 1
	if m in m_quarter[1]:
		clock[28] = 1
	if m in m_quarter[2]:
		clock[28] = 1
	if m in m_quarter[3]:
		clock[28] = 1
	if m in m_oclock[4]:
		clock[28] = 1

	if m in m_half[0]:
		clock[36] = 1
	if m in m_half[1]:
		clock[36] = 1
	if m in m_half[2]:
		clock[36] = 1
	if m in m_half[3]:
		clock[36] = 1
	if m in m_quarter[4]:
		clock[36] = 1

	if m in m_quarterto[0]:
		clock[35] = 1
	if m in m_quarterto[1]:
		clock[35] = 1
	if m in m_quarterto[2]:
		clock[35] = 1
	if m in m_quarterto[3]:
		clock[35] = 1
	if m in m_half[4]:
		clock[35] = 1

	if m in m_oclock[0]:
		clock[27] = 1
	if m in m_oclock[1]:
		clock[27] = 1
	if m in m_oclock[2]:
		clock[27] = 1
	if m in m_oclock[3]:
		clock[27] = 1
	if m in m_quarterto[4]:
		clock[27] = 1

def m1(m):																#Mitte des Minutenzeigers
	if m in mid[0]:
		clock[20] = 1
	if m in mid[1]:
		clock[21] = 1
	if m in mid[2]:
		clock[29] = 1
	if m in mid[3]:
		clock[37] = 1
	if m in mid[4]:
		clock[45] = 1
	if m in mid[5]:
		clock[44] = 1
	if m in mid[6]:
		clock[43] = 1
	if m in mid[7]:
		clock[42] = 1
	if m in mid[8]:
		clock[34] = 1
	if m in mid[9]:
		clock[26] = 1
	if m in mid[10]:
		clock[18] = 1
	if m in mid[11]:
		clock[19] = 1

def m2(m):																#ausserer Ring des Minutenzeigers
	if m in m_quarter[0]:
		clock[12] = 1
	if m in m_quarter[1]:
		clock[13] = 1
	if m in m_quarter[2]:
		clock[14] = 1
	if m in m_quarter[3]:
		clock[22] = 1
	if m in m_quarter[4]:
		clock[30] = 1

	if m in m_half[0]:
		clock[38] = 1
	if m in m_half[1]:
		clock[46] = 1
	if m in m_half[2]:
		clock[54] = 1
	if m in m_half[3]:
		clock[53] = 1
	if m in m_half[4]:
		clock[52] = 1

	if m in m_quarterto[0]:
		clock[51] = 1
	if m in m_quarterto[1]:
		clock[50] = 1
	if m in m_quarterto[2]:
		clock[49] = 1
	if m in m_quarterto[3]:
		clock[41] = 1
	if m in m_quarterto[4]:
		clock[33] = 1

	if m in m_oclock[0]:
		clock[25] = 1
	if m in m_oclock[1]:
		clock[17] = 1
	if m in m_oclock[2]:
		clock[9] = 1
	if m in m_oclock[3]:
		clock[10] = 1
	if m in m_oclock[4]:
		clock[11] = 1


def h0(h):																#innerster Ring des Stundezeigers
	if h in h_quarter:
		if clock[28]==1:												#"""Falls dort schon der Minutenzeiger ist, """
			clock[28] = 3												#"""wird dort eine 3 erzeugt welche spaeter die """
		else: clock[28] = 2												#"""Farbe point ergibt."""

	if h in h_half:
		if clock[36]==1:
			clock[36] = 3
		else:
			clock[36] = 2

	if h in h_quarterto:
		if clock[35]==1:
			clock[35] = 3
		else:
			clock[35] = 2


	if h in h_oclock:
		if clock[27]==1:
			clock[27] = 3
		else:
			clock[27] = 2

def h1(h):																#ausserer Ring des Stundenzeigers
	if h==h_quarter[0]:
		if clock[20]==1:
			clock[20] = 3
		else:
			clock[20] = 2
	if h==h_quarter[1]:
		if clock[21]==1:
			clock[21] = 3
		else:
			clock[21] = 2
	if h==h_quarter[2]:
		if clock[29]==1:
			clock[29] = 3
		else:
			clock[29] = 2
	if h==h_quarter[3]:
		if clock[20]==1:
			clock[20] = 3
		else:
			clock[20] = 2
	if h==h_quarter[4]:
		if clock[21]==1:
			clock[21] = 3
		else:
			clock[21] = 2
	if h==h_quarter[5]:
		if clock[29]==1:
			clock[29] = 3
		else:
			clock[29] = 2
	
	if h==h_half[0]:
		if clock[37]==1:
			clock[37] = 3
		else:
			clock[37] = 2
	if h==h_half[1]:
		if clock[45]==1:
			clock[45] = 3
		else:
			clock[45] = 2
	if h==h_half[2]:
		if clock[44]==1:
			clock[44] = 3
		else:
			clock[44] = 2
	if h==h_half[3]:
		if clock[37]==1:
			clock[37] = 3
		else:
			clock[37] = 2
	if h==h_half[4]:
		if clock[45]==1:
			clock[45] = 3
		else:
			clock[45] = 2
	if h==h_half[5]:
		if clock[44]==1:
			clock[44] = 3
		else:
			clock[44] = 2
	
	if h==h_quarterto[0]:
		if clock[43]==1:
			clock[43] = 3
		else:
			clock[43] = 2
	if h==h_quarterto[1]:
		if clock[42]==1:
			clock[42] = 3
		else:
			clock[42] = 2
	if h==h_quarterto[2]:
		if clock[34]==1:
			clock[34] = 3
		else:
			clock[34] = 2
	if h==h_quarterto[3]:
		if clock[43]==1:
			clock[43] = 3
		else:
			clock[43] = 2
	if h==h_quarterto[4]:
		if clock[42]==1:
			clock[42] = 3
		else:
			clock[42] = 2
	if h==h_quarterto[5]:
		if clock[34]==1:
			clock[34] = 3
		else:
			clock[34] = 2
	
	if h==h_oclock[0]:
		if clock[26]==1:
			clock[26] = 3
		else:
			clock[26] = 2
	if h==h_oclock[1]:
		if clock[18]==1:
			clock[18] = 3
		else:
			clock[18] = 2
	if h==h_oclock[2]:
		if clock[19]==1:
			clock[19] = 3
		else:
			clock[19] = 2
	if h==h_oclock[3]:
		if clock[26]==1:
			clock[26] = 3
		else:
			clock[26] = 2
	if h==h_oclock[4]:
		if clock[18]==1:
			clock[18] = 3
		else:
			clock[18] = 2
	if h==h_oclock[5]:
		if clock[19]==1:
			clock[19] = 3
		else:
			clock[19] = 2

#OUTPUT
while True:															#beginn der eigentlichen Uhr
	
	l1 = [5, 9, 9, 9, 9, 9, 9, 5]										#zerlegte Liste in das 8x8-Feld zur Uebersichtlichkeit
	l2 = [9, 0, 0, 0, 0, 0, 0, 9]
	l3 = [9, 0, 0, 0, 0, 0, 0, 9]
	l4 = [9, 0, 0, 0, 0, 0, 0, 9]
	l5 = [9, 0, 0, 0, 0, 0, 0, 9]
	l6 = [9, 0, 0, 0, 0, 0, 0, 9]
	l7 = [9, 0, 0, 0, 0, 0, 0, 9]
	l8 = [5, 9, 9, 9, 9, 9, 9, 5]
	
	#Funktion zum zusammenfuegen der 8 Listen zu einer
	lines = [l1, l2, l3, l4, l5, l6, l7, l8]
	clock = []
	
	for i in range(8):
		line = lines[i]
		for c in range(8):
			clock.append(line[c])
	
	#ausfuehren der Definitionen mit der Systemzeit durch strftime()
	"""%M = Minute, %H = Stunde"""
	m0(strftime("%M"))
	m1(strftime("%M"))
	m2(strftime("%M"))
	
	h0(strftime("%H"))
	h1(strftime("%H"))
	
	#belegen der Zahlen in der Liste mit den vordefinierten Farben
	pixels = [edge if clock[i]==9 else paper if clock[i]==0 else h_col if clock[i]==2 else m_col if clock[i]==1 else point if clock[i]==3 else black for i in range(64)]
	
	#Ausgabe der Liste
	sense.set_pixels(pixels)
	
	#1 sec warten vor der Wiederhohlung der Uhr-Schleife
	sleep(1)
