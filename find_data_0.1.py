import xlrd
season_name = "game of Thrones"
season_name = season_name.split(" ")


season_number = "01"
if season_number[0] != 's' or season_number[0] != 'S':
	season_number = "S"+season_number
episode_number = "01"
if episode_number[0] != 's' or episode_number[0] != 'S':
	episode_number = "S"+episode_number


sheet = ()

def open_file(path):
	wb = xlrd.open_workbook(path)
	sheet = wb.sheet_by_index(0)

for row_num in range(sheet.nrows):
		row_value = sheet.row_values(row_num)
		if row_value[1] == season_name[1]:
			print (row_value)

if __name__ == "__main__":
    path = "all_links.xlsx"
    open_file(path)