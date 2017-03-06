class ImportAmazonReviews:
    """
        Class that imports amazon reviews based on search criteria and returns sentiments
    """

    #Import section
    import nltk
    import urllib.request
    import pprint
    import re
    from bs4 import BeautifulSoup
    from nltk.sentiment import vader

    #code to improve the review analysis by pulling the information from other countries
    #for future improvements
    #countries=['com','co.uk','ca','de']
    #books=[
    #        '''http://www.amazon.%s/Glass-House-Climate-Millennium-ebook/dp/B005U3U69C''',
    #        '''http://www.amazon.%s/The-Japanese-Observer-ebook/dp/B0078FMYD6''',
    #        '''http://www.amazon.%s/Falling-Through-Water-ebook/dp/B009VJ1622''',
    #      ]
    # for country in countries:
    #    asin=book.split('/')[-1]; title=book.split('/')[3]
    #   url='''http://www.amazon.%s/product-reviews/%s'''%(country,asin)

    #   req = urllib.request.Request(url)
    #   response = urllib.request.urlopen(req)
    ##f = urllib2.urlopen(url)
    #  print (response.read())
    ##page=response.read().lower(); print ('%s=%s'%(country, page.count('member-review')))
    #def __init__(self, searchQuery):
    #    pass

    def SearchAmazon(self,searchQuery):
        import urllib.request
        from bs4 import BeautifulSoup
        import nltk
        from nltk.sentiment import vader

        searchQueryString = "+".join(searchQuery.split())
        urlsearch = "https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=" + searchQueryString + "&rh=i%3Aaps%2Ck%3A" + searchQueryString
        print(urlsearch)
        req = urllib.request.Request(urlsearch)
        req.add_header('User-Agent', 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11')
        response = urllib.request.urlopen(req)

        soup = BeautifulSoup(response)

        for a in soup.find_all('a', {"class": "a-size-small a-link-normal a-text-normal"}, href=True):
            # print ("Found the URL:", a['href'])
            urlProduct = a['href']
            if "/dp" in urlProduct and "http" in urlProduct:
                urlReviews = a['href'].replace("/dp/", "/product-review/").split("/ref", 1)[0]
                # urlReviews=a['href'].split("/dp/")[0]
                urlReviews += "/ref=cm_cr_arp_d_paging_btm_2?pageNumber="
                for x in range(1, 1000):
                    req = urllib.request.Request(urlReviews + str(x))
                    req.add_header('User-Agent', 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11')
                    response = urllib.request.urlopen(req)
                    soup = BeautifulSoup(response)
                    noReviewsDiv = soup.find_all("div", {"id": "cm_cr-review_list"})
                    # columns = soup.findAll('div', {"id": "cm_cr-review_list"}, text=re.compile('Sorry, no reviews match your current selections'))
                    # columns = soup.findAll('div', {"id": "cm_cr-review_list"}, text='Sorry, no reviews match your current selections')
                    if len(noReviewsDiv) == 1 and noReviewsDiv[
                        0].text == "Sorry, no reviews match your current selections.Try clearing or changing some filters.Show all reviews":
                        break;
                    else:
                        print(urlReviews + str(x))

                        # url = 'https://www.amazon.com/AmazonBasics-13-3-Inch-Laptop-Sleeve-Black/product-reviews/B00CD8AF48/ref=cm_cr_dp_d_acr_sr?ie=UTF8&reviewerType=avp_only_reviews'

                        req = urllib.request.Request(urlReviews + str(x))
                        req.add_header('User-Agent', 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11')
                        response = urllib.request.urlopen(req)

                        # print (response.read())
                        soup = BeautifulSoup(response)

                        mydivs = soup.find_all("span", {"class": "a-size-base review-text"})
                        sia = vader.SentimentIntensityAnalyzer()
                        # posts=[]
                        for div in mydivs:
                            # posts+= map(lambda p: p.text.encode("ascii", errors="replace").replace(b"?",b" ").decode("utf-8"), div.findAll("li"))
                            print(div.text)
                            ps = sia.polarity_scores(div.text)
                            print(ps)
                            print('-' * 40)




x=ImportAmazonReviews()
x.SearchAmazon("Samsung Galaxy S7")


