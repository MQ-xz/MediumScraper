#!/bin/python3.8
from datetime import date
import requests
import argparse
import json
import sys
import os

class Scraper:
	def __init__(self):
		self.today = date.today()
		self.years = [ i for i in range(2014, self.today.year + 1)]
		self.months = [ (f"{i:02d}") for i in range(1, 13)]

		print('''\033[92m___  ___         _ _                 _____
|  \/  |        | (_)               /  ___|
| .  . | ___  __| |_ _   _ _ __ ___ \ `--.  ___ _ __ __ _ _ __   ___ _ __
| |\/| |/ _ \/ _` | | | | | '_ ` _ \ `--. \/ __| '__/ _` | '_ \ / _ \ '__|
| |  | |  __/ (_| | | |_| | | | | | /\__/ / (__| | | (_| | |_) |  __/ |
\_|  |_/\___|\__,_|_|\__,_|_| |_| |_\____/ \___|_|  \__,_| .__/ \___|_|

						https://t.me/Xpykerz
\033[0m''')

		parser = argparse.ArgumentParser()
		parser.add_argument("-t", "--tag", dest="tag", required=True, help="Specify Tage {use - is there is space in tage (ex:bug-bounty)}")
		parser.add_argument("-y", "--year", dest="year", help="Which year you want, default is all.",default=None, required=False)
		parser.add_argument("-m", "--month", dest="month",help="Which month you want, default is all.", default=None, required=False)
		parser.add_argument("-d", "--day", dest="day", help="Which day you want, default is all.", default=None, required=False)
		self.args = parser.parse_args()
		if not self.args.tag:
			sys.exit(parser.print_help)

	def get_days(self, year, month):
		y = int(year)
		m = int(month)
		leap = 0
		if y% 400 == 0:
			leap = 1
		elif y % 100 == 0:
			leap = 0
		elif y% 4 == 0:
			leap = 1
		if m==2:
			return 28 + leap
		list = [1,3,5,7,8,10,12]
		if m in list:
			return 31
		return 30


	def scraper(self, tage, year, month, day):
		try:

			api = f"https://medium.com/tag/{tage}/archive/{year}/{month}/{day}"
			res = requests.get(api).text
			data = json.loads(res.split('window["obvInit"](')[1].split(')\n// ]]>')[0])

			for user,post in zip(data['references']['User'],data['references']['Post']):
				# print(json['references']['User'][i])
				username = data['references']['User'][user]['username']
				postdata = data['references']['Post'][post]
				postid = postdata['id']
				title = postdata['title']
				subtitle = postdata['content']['subtitle']
				url = f'https://medium.com/{username}/{postdata["uniqueSlug"]}'
				print(f'''\033[32;1m{title} by {username}
		\033[0m{subtitle}
		\033[34;4m{url}\033[0m
		''')
		except:
			sys.exit("\033[91m[!] Oops something went wrong!.\033[0m")

	def main(self):
		if self.args.year is not None:
			if self.args.month is not None:
				if self.args.day is not None:
					year = str(self.args.year)
					day = (f"{int(self.args.day):02d}")
					month = (f"{int(self.args.month):02d}")
					self.scraper(self.args.tag, year, month, day)
				else:
					for d in range(1, self.get_days(self.args.year, self.args.month) + 1):
						d = (f"{d:02d}")
						year = str(self.args.year)
						month = (f"{int(self.args.month):02d}")
						self.scraper(self.args.tag, year, month, d)
			else:
				if self.args.year == self.today.year:
					for m in [ (f"{i:02d}") for i in range(1, today.month +1)]:
						if int(m) == self.today.month:
							for d in range(1, get_days(year, m) + 1):
								d = (f"{d:02d}")
								self.scraper(self.args.tag, year, m, d)
						else:
							for d in range(1, get_days(year, m) + 1):
								d = (f"{d:02d}")
								self.scraper(self.args.tag, year, m, d)
				else:
					for m in self.months:
						for d in range(1, self.get_days(self.args.year, m) + 1):
							d = (f"{d:02d}")
							year = str(self.args.year)
							self.scraper(self.args.tag, year, m, d)
		else:
			for y in self.years:
				for m in self.months:
					for d in range(1, get_days(y, m) +1):
						year = str(self.args.year)
						d = (f"{d:02d}")
						self.scraper(self.args.tag, y, m, d)


if __name__ == "__main__":
	sc = Scraper()
	sc.main()
