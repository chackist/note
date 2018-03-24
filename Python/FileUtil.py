#coding=utf8
import shutil
import os

path = "/Users/evan/Desktop/test/"

class FileUtil:
	TYPE_FILE = 1
	TYPE_DIR = 2
	TYPE_UNKNOW = 0

	@classmethod
	def delete(cls, path):
		if not cls.exist(path):
			return False
		typePath = cls.type(path)
		if typePath == 0:
			return False

		if typePath == 1:
			return os.remove(path)
		else:
			return shutil.rmtree(path)

	@classmethod
	def exist(cls, path):
		return os.path.exists(path)

	@classmethod
	def join(cls, root, *dirs):
	    for item in dirs:
	        path = os.path.join(root, item)
	    return path

	@classmethod
	def type(cls, path):
		if os.path.isdir(path):
			return FileUtil.TYPE_DIR
		elif os.path.isfile(path):
			return FileUtil.TYPE_FILE
		else:
			return FileUtil.TYPE_UNKNOW

	@classmethod
	def mk(cls, path):
		if not cls.exist(path):
			os.mkdir(path)

	#ab+ add wb+ cover
	@classmethod
	def write(cls, path, data, model):
		outFp = open(path, model)
		outFp.write(data)
		outFp.close()

	@classmethod
	def remove(cls, srcPath, desPath):
		cls.copy(srcPath ,desPath)
		cls.delete(srcPath)

	@classmethod
	def copy(cls, srcPath, desPath):
		if not cls.exist(srcPath):
			return False
		typePath = cls.type(srcPath)
		if typePath == 1:
			return shutil.copy(srcPath, desPath)
		else:
			return shutil.copytree(srcPath, desPath)
	
	@classmethod
	def list(cls, path):
		array = []
		for item in os.listdir(path):
			itemPath = cls.join(path, item)
			if os.path.isfile(itemPath):
				array.append(itemPath)
			else:
				array.append(itemPath)
				array = array + cls.list(itemPath)
		return array

	@classmethod
	def cmd(cls, cmd):
		output = os.popen(cmd)
		return output.read()

#typePath = FileUtil.typePath(path + "1")
FileUtil.write(path + "1/3.txt", "123", "ab+	")
FileUtil.write(path + "3.txt", "456", "ab+")
FileUtil.mk(path + "1")
FileUtil.remove(path + "1.txt",path + "2.txt")
print(FileUtil.list(path))
print(FileUtil.cmd("ifconfig"))
#FileUtil.delete(path + "1")