class TkDataStore:
	def __init__(self, root):
		self.tkroot = root
		self.data = {}

	def set(self, key, value, lockkey):
		""" Method to add data to the DataStore or update any existing data.

		>>> TkDataStore().set("key", "43").__dict__["key"]
		43
		"""
		if not self.data[key]["locked"]:
			self.data[key] = value
		else:
			raise ArgumentError("You cannot change the value of locked data.")

	def quickset():
		

	@staticmethod
	def builder(data):
		store = TkDataStore()

		if type(data) == dict:
			store.quickset(data(
