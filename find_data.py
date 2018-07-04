import xlrd
season_name = "game of Thrones"
season_name = season_name.split(" ")


season_number = "01"
if season_number[0] != 's' or season_number[0] != 'S':
	season_number = "S"+season_number
episode_number = "01"
if episode_number[0] != 's' or episode_number[0] != 'S':
	episode_number = "S"+episode_number



# def generate_lines_that_equal(string, fp):
#     for line in fp:
#         if line == string:
#             print(line)


# generate_lines_that_equal(season_name[-1], 'links.txt')

for every_line in open('all_links.xlsx').read():
	print(every_line)
	if season_name[0] in every_line:
		print (every_line)

# if season_name[0] in open('links.txt').read():
# 	print ()
# 	# if season_name[1] in open('links.txt').read():
# 	# 	if season_name[2] in open('links.txt').read():
