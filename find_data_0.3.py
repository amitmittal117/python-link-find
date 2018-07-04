from xlrd import open_workbook
book = open_workbook("all_links.xlsx")

season_name = "Game of Thrones"
season_name = season_name.split(" ")


season_number = "01"
if season_number[0] != 's' or season_number[0] != 'S':
	season_number = "S"+season_number
episode_number = "01"
if episode_number[0] != 's' or episode_number[0] != 'S':
	episode_number = "E"+episode_number

number = 0
def collect_data():
	if season_number[number] in cell.value and number != len(season_name):
		number = number+1
		collect_data()
	else:
		return (cell.value)

for sheet in book.sheets():
	for rowidx in range(sheet.nrows):
		row = sheet.row(rowidx)
		for colidx, cell in enumerate(row):
			print(collect_data)
			# if "Game" in cell.value:
			# 	if "of" in cell.value:
			# 		if "Thrones" in cell.value:
			# 			print(cell.value)
						
# if season_number in cell.value:
# 	if episode_number in cell.value:
# 		pass