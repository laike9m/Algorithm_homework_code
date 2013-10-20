from collections import OrderedDict

class GS_match():
	def __init__(self):
				
		self.boys = OrderedDict()
		self.girls = OrderedDict()

		with open('boys_rankings.txt') as b:
			lines = b.readlines()
			for line in lines:
				split_to_two_parts = line.split(':')
				boy_name,boy_ranking = split_to_two_parts[0],split_to_two_parts[1]
				boy_to_add = Boy()
				boy_to_add.name = boy_name
				boy_to_add.ranking = (rank for rank in boy_ranking.split())
				self.boys[boy_name] = boy_to_add

		with open('girls_rankings.txt') as g:
			lines = g.readlines()
			for line in lines:
				split_to_two_parts = line.split(':')
				girl_name,girl_ranking = split_to_two_parts[0],split_to_two_parts[1]
				girl_to_add = Girl()
				girl_to_add.name = girl_name
				girl_to_add.ranking = (rank for rank in girl_ranking.split())
				self.girls[girl_name] = girl_to_add
		
		for boy in self.boys.values():
			boy.ranking = (self.girls[girl] for girl in boy.ranking)
		
		for girl in self.girls.values():
			girl.ranking = [self.boys[boy] for boy in girl.ranking]
		
		self.xianchong_boys = []
		self.single_boys = [boy for boy in self.boys.values()]

	def match(self):
		while self.single_boys:
			new_single_boy = self.single_boys[0].proposal()
			add_to_xianchong = self.single_boys.pop(0)
			self.xianchong_boys.append(add_to_xianchong)
			if new_single_boy:
				self.xianchong_boys.remove(new_single_boy)
				self.single_boys.append(new_single_boy)
			
		# test
		for boy in self.xianchong_boys:
			if not boy.current_gf:
				pass
		
		for boy in self.single_boys:
			if boy.current_gf:
				pass
			
		for girl in self.girls.values():
			print('%s\'s bf is %s\n' % (girl.name, girl.current_bf.name))
		
		for boy in self.boys.values():
			print('%s\'s gf is %s\n' % (boy.name, boy.current_gf.name))
		
		
class Boy():
	#排名用列表,维护一个当前约会者的index,每次找下一个
	def __init__(self):
		self.ranking = None
		self.current_gf = None
		
	def proposal(self):
		for girl in self.ranking:
			result = girl.compare_two_boys(self)
			if result:
				#print(self.name  ' got a gf '  self.current_gf.name  '\n')
				if result != 'first':
					return result
				else:
					return None
				
				
class Girl():
	def __init__(self):
		self.ranking = None
		self.current_bf = None
		
	def compare_two_boys(self, new_suitor):
		'返回0 if 拒绝新来的,返回1 if 接受新来的'
		if not self.current_bf:
			self.current_bf = new_suitor
			new_suitor.current_gf = self
			return 'first'	# 成功,没有新的singleboy
		else:
			if self.ranking.index(new_suitor) < self.ranking.index(self.current_bf):
				new_single_boy = self.current_bf
				self.current_bf = new_suitor
				new_suitor.current_gf = self
				new_single_boy.current_gf = None
				#print('%s lost his gf %s' % (new_single_boy.name, self.name))
				return new_single_boy	# 产生一个新的singleboy
			else:
				return None		# 不成功


if __name__ == '__main__':
	gs_match = GS_match()
	gs_match.match()
