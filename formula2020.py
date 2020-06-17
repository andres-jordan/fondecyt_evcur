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

def P(s):
	print 1 + 1.7*(s**0.25)
	return min(5,1 + 1.7*(s**0.25))

if (len(bibcodes) > 10):
	raise ValueError("La lista de publicaciones no debe tener mas de 10 articulos")

PI_name_length=len(PI_name)
S = 0
N = 0
ci_sum = 0

for b in bibcodes:
	res = ads.SearchQuery(bibcode=b,fl=['year', 'author', 'citation_count', 'title'])
	for paper in res:
		print "Processing paper: "+ b
		print 'Title: "'+unidecode(paper.title[0])+'"'
		yr = int(paper.year)
		years = 2020 - yr
		if (yr < 2015):
			raise ValueError("No papers prior to 2015 can be used")
		if years == 0:
			years = 1
		c_i = paper.citation_count/years
		ci_sum += c_i
		author_list_length = len(paper.author)
		bis = min(author_list_length,6)
		I_i=0.2
		for i in range(bis):
			last_name = paper.author[i].split(',')[0]
			if (last_name[:PI_name_length] == PI_name):
				if (i <= 1):
					I_i = 1
				if (i==2):
					I_i = 0.9
				if (i==3):
					I_i = 0.7
				if (i==4):
					I_i = 0.5
				if (i==5):
					I_i = 0.3
		tmp = (I_i * (1+c_i**0.5))
		S += (I_i * (1+c_i**0.5))
		print "\tc_i={0:4.2f} I_i={1:2.1f} S={2:4.2f}".format(c_i,I_i,tmp)
	N += 1


puntaje_final = P(S)

print "\nPuntaje de lista de publicaciones:", puntaje_final
