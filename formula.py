import ads
from unidecode import unidecode

##### bibcodes.txt has the bibcodes of the publications, one per line (maximum of 10)
with open('bibcodes.txt') as f:
	bibcodes = f.read().splitlines()

# PI last name. Does not need to be the full name to help with the woes
# of accented characters, but be careful that it does not match other co-authors
# in your papers
PI_name='Jord'
#############

def P(c):
    return min(5,3 + 2*c/12.)

if (len(bibcodes) > 10):
	raise ValueError("La lista de publicaciones no debe tener mas de 10 articulos")

PI_name_length=len(PI_name)
liderazgo = 0
N = 0
pi_sum = 0

for b in bibcodes:
	res = ads.SearchQuery(bibcode=b,fl=['year', 'author', 'citation_count', 'title'])
	for paper in res:
		print "Processing paper: "+ b
		print 'Title: "'+unidecode(paper.title[0])+'"'
		yr = int(paper.year)
		years = 2016 - yr
		if (yr < 2011):
			raise ValueError("No papers prior to 2011 can be used")
		if years == 0: 
			years = 1
		p_i = P(paper.citation_count/years)
		if (yr == 2016) and (p_i < 4):
			p_i = 4.0
		pi_sum += p_i
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
		liderazgo += l_i
		print "\tP_i={0:4.2f} l_i={1:2.1f}".format(p_i,l_i)
	N += 1

deltaP = 0
if (N < 10):
	deltaP = (1/3.)*(N-10)

deltaL = 0
if (liderazgo < 5):
	deltaL = 1.75*((1-0.2*liderazgo)**(1.25))

puntaje_final = pi_sum/N - deltaP - deltaL

print "\nPuntaje de lista de publicaciones:", puntaje_final