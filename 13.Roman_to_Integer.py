class Solution(object):
	def romanToInt(self,s):
		dict = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
		track = 0
		total = 0
		if len(s) == 0:
			return 0
		elif len(s) == 1:
			if s in dict:
				return dict[s]
		for i in range(len(s)):
			if i == 0:
				track = dict[s[i]]
			else:
				if dict[s[i]] == track:
					track += dict[s[i]]
				elif dict[s[i]] < track:
					total += track
					track = dict[s[i]]
				elif dict[s[i]] > track:
					if track == 0:
						track = dict[s[i]]
					else:
						track = abs(track - dict[s[i]])
						total += track
						track = 0
		total += track
		return total