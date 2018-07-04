from xlrd import open_workbook
import urllib.request as req

book = open_workbook("all_links.xlsx")

season_name = "Game of Thrones"
season_name = season_name.split(" ")


season_number = "01"
if season_number[0] != 's' or season_number[0] != 'S':
	season_number = "S"+season_number
episode_number = "01"
if episode_number[0] != 's' or episode_number[0] != 'S':
	episode_number = "E"+episode_number



for sheet in book.sheets():
	for rowidx in range(sheet.nrows):
		row = sheet.row(rowidx)
		for colidx, cell in enumerate(row):
			if "Game" in cell.value:
				if "of" in cell.value:
					if "Thrones" in cell.value:
						if season_number in cell.value:
							if episode_number in cell.value:
									size= req.urlopen(cell.value).headers['Content-Length']
									print (cell.value + " "+ str(round(int(size)/(1024*1024))) + "MB")
