
#scrapy runspider jaydonscraper.py -o output.json

import scrapy

class CheesyHoursSpider(scrapy.Spider):
    name = "cheesy_hours"
    start_urls = [
        "http://hours.team254.com"
    ]

    custom_settings = {
        'ROBOTSTXT_OBEY': False
    }

    def parse(self, response):

        i = 0
        student_ids = response.css("td:first-child::text").getall()

        for i in range(len(student_ids)):
            if student_ids[i] == "225287":
                print("Found Jaydon!")
                yield {
                    'jaydon': True
                }
                break
            else:
                continue

        yield {
            'jaydon': False
        }
