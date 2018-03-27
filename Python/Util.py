#coding=utf8
import shutil
import os
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
		return True

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
			return True
		return False

	#ab+ add wb+ cover
	@classmethod
	def write(cls, path, data, model):
		try:
			fp = open(path, model)
			fp.write(data)
			fp.close()
		except BaseException:
			return False
		else:
			fp.close()
		return True
		

	@classmethod
	def read(cls, path, model):
		try:
			fp = open(path, model)
			#fp.readlines()
			data = ""
			for x in fp:
				data += x
			return data
		except BaseException:
		    return ""
		else:
		    fp.close()

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

class CommandUtil:
	# \033[显示方式;前景色;背景色m
	#显示方式 0 终端默认 1 高亮 4 下划线 5 闪缩 6 反白 7 不可见
	# 前景色 30-37 背景色 40-47 黑 红 绿 黄 蓝 紫红 青蓝 白
	def __init__(self, config):
		self.config = config
		self.tips = ""
		self.command = {}
		self.colors = ['\033[1;31m','\033[1;34m']
		
		index = 0
		for v in self.config:
			for subV in v:
				self.tips += self.colors[index % len(self.colors)] +  "[" + subV["commond"] + "]: " + subV["name"] + " "
				self.command[subV["commond"]] = subV["fun"]
				index += 1
			self.tips += "\n"


		self.tips += self.colors[index % len(self.colors)] + "[quit]: quit\n"
		self.tips += "\033[1;0;0mInput: "

	@classmethod
	def cmd(cls, cmd, returnInfo):
		if returnInfo:
			output = os.popen(cmd)
			return output.read()
		else:
			os.system(cmd)


	def run(self):
		while True:
			opare = raw_input(self.tips)
			if "quit" == opare :
				break
			else:
				try:
					commandItem = self.command[opare]
					commandItem()
				except Exception as e:
					print(e)
				finally:
					pass






