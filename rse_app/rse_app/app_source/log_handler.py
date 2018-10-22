import json 
import hashlib
import time
import os
import datetime
from operator import itemgetter
import config


class QueryLog(object):
	"""docstring for ClassName"""
	def __init__(self):
		with open(config.LOG_PATH, "r") as log_file:
			self.query_list = json.loads(log_file.read())

	def append_query(self, query, file_name, file_path):
		last_time = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
		file_size = os.stat(os.path.join(config.BASE, file_path)).st_size
		new_query = {"query": query, "file_name": file_name, "file_path": file_path, "last_time": last_time, 
					 "file_size": file_size}

		self.query_list.append(new_query)
		self.query_list = sorted(self.query_list, key=itemgetter('last_time'))
		print self.query_list

	def check_storage(self):
		files_to_delete = []
		sum_size_files = sum(item['file_size'] for item in self.query_list)
		if sum_size_files >= config.MAX_SIZE:
			storage_enough = False
			while sum_size_files >= config.MAX_SIZE:
				files_to_delete.append(self.query_list[0])
				del self.query_list[0]
				sum_size_files = sum(item['file_size'] for item in self.query_list)
		else:
			storage_enough = True
		return storage_enough, files_to_delete

	def write_log(self):
		query_json = json.dumps(self.query_list, indent=4, sort_keys=True)
		with open(config.LOG_PATH, "w") as log_file:
			log_file.write(query_json)

	
	def query_exists(self, query):
		exists = False
		query_searh = ''
		for query_item in self.query_list:
			if query_item["query"] == query:
				exists = True
				query_searh = query_item
				last_time = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
				query_item["last_time"] = last_time
				self.write_log()
				break
		return exists, query_searh