from tkinter import Tk
from .tkinter import TkDataStore

import json


class Application(Tk):
	def __init__(self, data):
		Tk.__init__(self, data)

		if type(data) == DataStore:
			self.datastore = datastore
		else:
			self.datastore = DataStore.builder(data)

		self.create_widgets()

	def create_widgets():
		for item in self.datastore.retrieve(


	def create_list_item():
		pass


def load_json(filename="defs.json"):
	data = json.load(filename)
	return data

if __name__ == "__main__":
	data = load_json()

	app = Application()
	app.mainloop()
