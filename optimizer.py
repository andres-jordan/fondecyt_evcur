from __future__ import print_function
import ads
from unidecode import unidecode
from itertools import combinations
import numpy as np
import copy

max_n = 25

##### bibcodes.txt has the bibcodes of the publications, one per line
with open('bibcodes_opt.txt') as f:
	bibcodes = f.read().splitlines()

# PI last name. Does not need to be the full name to help with the woes
# of accented characters, but be careful that it does not match other co-authors
# in your papers
PI_name='Jord'
#############

def P(c):
    return min(5,3 + 2*c/12.)

num_pubs = len(bibcodes)
if (num_pubs < 11):
	raise ValueError("La lista de publicaciones debe tener al menos 10 articulos")

PI_name_length=len(PI_name)

l_array=[]
p_array=[]
N=10

for b in bibcodes:
	res = ads.SearchQuery(bibcode=b,fl=['year', 'author', 'citation_count', 'title'])
	for paper in res:
		print("Processing paper: "+ b)
		print('Title: "'+unidecode(paper.title[0])+'"')
		yr = int(paper.year)
		years = 2016 - yr
		if (yr < 2011):
			raise ValueError("No papers prior to 2011 can be used")
		if years == 0: 
			years = 1
		p_i = P(paper.citation_count/years)
		if (yr == 2016) and (p_i < 4):
			p_i = 4.0
		p_array.append(p_i)
		author_list_length = len(paper.author)
		bis = min(author_list_length,5)
		l_i=0
		for i in range(bis):
			last_name = paper.author[i].split(',')[0]
			if (last_name[:PI_name_length] == PI_name):
				if (i <= 2):
					l_i = 1
				if (i > 2) and (i < 5):
					l_i = 0.5
		l_array.append(l_i)
		print("\tP_i={0:4.2f} l_i={1:2.1f}".format(p_i,l_i))


l_array = np.array(l_array)
p_array = np.array(p_array)


# Now we select a subset of maximum 20 papers to make the calculation 
# in a reasonable time
n_actual_papers = len(l_array)
if (n_actual_papers > max_n):
	# include all papers with leadership > 0
	print("Restricting your list to {0:d} papers".format(max_n))
	i_l = np.where(l_i > 0)
	tmp_array = copy.copy(p_array)
	tmp_array[i_l] = 5.1
	idx = np.argsort(tmp_array)
	l_array = l_array[idx][-max_n:]
	p_array = p_array[idx][-max_n:]
	#bibcodes = bibcodes[idx][max_n:]
	tmp=[]
	for k in range(max_n):
		tmp.append(bibcodes[idx[-max_n+k + n_actual_papers]])
	bibcodes=tmp
	num_pubs = max_n

def score(l_array,p_array,I):
	liderazgo = l_array[I].sum()
	av_score  = p_array[I].mean()
	deltaL = 0
	if (liderazgo < 5):
		deltaL = 1.75*((1-0.2*liderazgo)**(1.25))
	return av_score - deltaL

best_score=-1e10
C = combinations(range(num_pubs),10)
Ci = np.array(list(C))
I_best = None
ni = len(Ci)

for ind in range(ni):
	II = Ci[ind]
	try_score = score(l_array,p_array,II)
	if (try_score > best_score):
		best_score = try_score
		I_best = II

print("\nBest set of papers:")
for i in I_best:
	print(bibcodes[i])

print("\nBest score:", best_score)

