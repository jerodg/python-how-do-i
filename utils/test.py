# my_list = [['a', None, 'c'], [None, None, None], ['g', None, 'i'], ['j', None, 'None']]
# output_check = [['a', 'c'], ['g', 'i'], ['j', 'None']]
#
# new_list = [[x, z] for x, y, z in my_list if x]
#
# assert output_check == new_list
#
# print(new_list)

# new_list = []
#
# for x in my_list:
# 	if all(_ is None for _ in x):
# 		pass
# 	else:
# 		new_list.append(x)
#
# assert output_check == new_list
# print(new_list)

# new_list = [x for x in my_list if not all(_ is None for _ in x)]
# from PIL import Image
#
# image = Image.open("flowers.jpg")
# image.show("flowers")

from csv import writer

import requests
from recipe_scrapers import scrape_html

with open("recipe.csv", "w", encoding="utf8", newline="") as file:
    thewriter = writer(file)
    thewriter.writerow(
        ["Title", "Ingredients", "Instructions", "Nutrition_Facts", "image", "links"]
    )  # Header

    with open("data.txt", "r") as inf:
        for line in inf:
            html = requests.get(line).content
            scraper = scrape_html(html=html, org_url=line)

            thewriter.writerow(
                [
                    scraper.title(),
                    scraper.ingredients(),
                    scraper.instructions(),
                    scraper.nutrients(),
                    scraper.image(),
                    scraper.links(),
                ]
            )
