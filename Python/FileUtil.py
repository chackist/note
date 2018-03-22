import shutil
import os

path = "/Users/evan/Desktop/test/"

class FileUtil:
	TYPE_FILE = 1
	TYPE_DIR = 2
	TYPE_UNKNOW = 0

	@classmethod
	def deletePath(cls, path):
		os.remove(path)

	@classmethod
	def typePath(cls, path):
		typePath = TYPE_UNKNOW
		if os.path.isdir(path):
			typePath = TYPE_DIR
		elif os.path.isfile(path):
			typePath = TYPE_FILE
		return typePath
	
	def removePath(cls, srcPath, desPath):
		pass

	def copyPath(cls, srcPath, desPath):
		pass

	def copyPath(cls, srcPath, desPath):
		pass


FileUtil.deletePath(path + "1")