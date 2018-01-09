# -*- coding: utf-8 -*-
import re
from konlpy.tag import Twitter
import sys
import operator
import math
import base64
import json
from langdetect import detect
from natto import MeCab
# Mecab binder : https://pypi.python.org/pypi/natto-py
import nltk

# konlpy 사용시 ascii encoding관련된 문제 해결법 
# 아래와 같이 할 경우 jupyter notebook에서 출력시 console에만 출력되기 때문에
# 이 경우 주석처리된 소스를 사용
# import sys
# stdout = sys.stdout
# reload(sys)
# sys.setdefaultencoding('UTF8')
# sys.stdout = stdout

reload(sys)
sys.setdefaultencoding('UTF8')

'''
Langdetect Library Example : Unicode로 넣지 않으면 에러 발생
detect_lang function : all possibility

text1 = unicode("太郎はこの本を二郎を見た女性に渡した")
text2 = u"안녕하세요."
text3 = "apple is"
text4 = u"apple is"
print detect_langs(" ".join(text1))
print detect_langs(" ".join(text2))
print detect_langs(" ".join(text3))
print detect_langs(" ".join(text4))
'''

'''
Input은 Base64 encoded text, 정규표현식으로 html tag제거
'''
program_name = sys.argv[0]
arguments = sys.argv[1:]
data = base64.b64decode(arguments[0])
cleanr = re.compile('<.*?>')
cleantext = re.sub(cleanr, ' ', data)
lang = detect(unicode(cleantext))
#print lang

word_arr = []

if lang == 'ko':
	twitter = Twitter()
	array = twitter.nouns(cleantext)
	print json.dumps(array)

elif lang == 'ja':
	mn = MeCab('-d /var/lib/mecab/dic/ipadic-utf8')
	t = mn.parse(cleantext)
	t_ar = t.split('\n')
	for ar in t_ar:
		if len(ar.split('\t')) > 1:
			word = ar.split('\t')[0]
			pr = ar.split('\t')[1]
			morp = pr.split(',')[0]
			is_num = pr.split(',')[1]
			kata = pr.split(',')[6]
			if morp == u'名詞' and is_num != u'数' and kata != '*':	
				word_arr.append(word)

	print json.dumps(word_arr)

else:
	tokens = nltk.word_tokenize(cleantext)

	if len(tokens) == 0:
		print json.dumps(word_arr)
	else:
		tagged = nltk.pos_tag(tokens)
		for tok in tagged:
			if tok[1] == 'NN' or tok[1] == 'NNS':
				word_arr.append(tok[0])

		print json.dumps(word_arr)
