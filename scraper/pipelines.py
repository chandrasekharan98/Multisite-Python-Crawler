# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

#NOTE : FEED_FORMAT need not be set in the settings as a seperate JSON file is being created 
# through the pipeline

'''
Format of JSON :
{
	"pages" : [
		{
			"page" : "...."
			"content" : "...."
		},
		{
			"page" : "..."
			"content" : "..."
		}
	.
	.
	.
	]
}
'''
import json
import os

class JsonPipeline(object):
	processedItemCount = 0

	def open_spider(self, spider):
		self.file = open('crawledData.json', 'w', encoding = "utf-8")
		self.file.write('{\n\t"pages" : [\n\t')

	def close_spider(self, spider):
		self.file.seek(0,os.SEEK_END)
		self.file.seek(self.file.tell() - 3, os.SEEK_SET)
		self.file.write(" \n\t]\n}")
		self.file.close()
		print("Crawled and parsed {} pages.".format(self.processedItemCount))

	def process_item(self, item, spider):
		line = json.dumps(
			dict(item),
			ensure_ascii=False,
			sort_keys=False,
			indent=8,
			separators=(',', ': ')
		) + ",\n"

		self.file.write(line)
		self.processedItemCount += 1
		return item