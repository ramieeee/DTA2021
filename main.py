import bs4

# article from 33000 - 33129
for i in range(33000, 33130):
    webpage=urlopen('http://www.dentalarirang.com/news/articleView.html?idxno=33129')
    source = BeautifulSoup(webpage, 'html.parser', from_encoding='utf-8')
    source.findAll('p')
