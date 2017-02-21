import urllib.request
from bs4 import BeautifulSoup
from lxml import html
from lxml import etree

base_url = "http://www.imdb.com/"


# ##nominees for best motion picture of the year
# #
# #nominees = tree.xpath("//*[@id='main']/div[1]/blockquote/blockquote[1]/div")
# #for i in range(len(nominees)):
# #    nominee = "//*[@id='main']/div[1]/blockquote/blockquote[1]/div["+str(i)+"]/strong/a/text()"
# #    #nominee_link = "//*[@id='main']/div[1]/blockquote/blockquote[1]/div["+str[i]+"]/strong/a"
# #    print(tree.xpath(nominee))
# #    #print(tree.xpath(nominee_link))
# #
# #
# #    #//*[@id="main"]/div[1]/blockquote/blockquote[1]/div[1]/div/a  movie name
# #    #//*[@id="main"]/div[1]/blockquote/blockquote[1]/div[1]/strong/a movie link

# gives the response of the url as tree
def url_opener(url):
    # response = urllib.request.urlopen("http://www.imdb.com/event/ev0000003/2017")
    print("reading the response to the url -" + url)
    response = urllib.request.urlopen(url)
    # print(response.read())
    soup = BeautifulSoup(response, 'html.parser')
    # print(soup.prettify())
    tree = html.fromstring(str(soup))
    return tree

# create a data file
def data_file():
    return

# write the data to csv file
def write_to_csv():
    return

# gives all the information about the film crew
def get_film_crew_data():

    return


# gives all the information about the given movie
def get_movie_data(response,title):

    return

# returns the genre of the movie
def get_genre_for_movie(url):
    response = url_opener(base_url+''.join(url))
    genre = response.xpath("//div[@itemprop='genre']/a/text()")
    return genre


def oscar_nominees(response):
    all_categories = response.xpath("//*[@id='main']/div[1]/blockquote/blockquote")
    print("\nTotal categories nominated for the oscars " + str(len(all_categories)))
    print("\n All the categories")
    print("---------------------")
    categories = (response.xpath("//*[@id='main']/div[1]/blockquote[1]/h2/text()"))
    # for i in categories :
    # print("-->"+i)


    for i in range(1, len(categories)+1):
        print("\n-->" + categories[i - 1])
        print()
        total_nominees = response.xpath("//*[@id='main']/div[1]/blockquote[1]/blockquote[" + str(i) + "]/div")
        for j in range(1, len(total_nominees)+1):
            if j == 1:
                print("******winner******")
                # //*[@id='main']/div[1]/blockquote[1]/blockquote[1]/div[1]/strong/a/text()
                print(response.xpath(
                    "//*[@id='main']/div[1]/blockquote[1]/blockquote[" + str(j) + "]/div[1]/strong/a/text()"))
                print(response.xpath(
                    "//*[@id='main']/div[1]/blockquote[1]/blockquote[" + str(j) + "]/div[1]/strong/a/@href"))
                print(get_genre_for_movie(response.xpath(
                    "//*[@id='main']/div[1]/blockquote[1]/blockquote[" + str(j) + "]/div[1]/strong/a/@href")))
                print()
                print("||||||Nominees||||||")
            else:
                print(response.xpath(
                    "//*[@id='main']/div[1]/blockquote[1]/blockquote[" + str(i) + "]/div["+str(j)+"]/strong/a/text()"))
                print(get_genre_for_movie(response))
                # //*[@id='main']/div[1]/blockquote[1]/blockquote[1]/div[1]/strong/a/text()
    other_categories = len(response.xpath("//div[@class='award']"))

    for i in range(2, other_categories + 1):
        print("category")
        print(response.xpath("//div[@class='award']["+str(i)+"]/h1/text()"))
        print("winners")
        for j in range(1, len(response.xpath("//div[@class='award']["+str(i)+"]//div/div/a")) + 1):
            print(response.xpath("//div[@class='award']["+str(i)+"]/blockquote/blockquote/div["+str(j)+"]/a/text()"))
            print(response.xpath("//div[@class='award']["+str(i)+"]/blockquote/blockquote/div["+str(j)+"]/a/@href"))
    return


# for loop to navigate so url's based on year
def collect_years():
    response = url_opener(base_url + "event/ev0000003/2017")
    a = response.xpath("//h3[text()='Event History']/../a")
    # print(len(a))
    # change (1,3) to len(a)
    for i in range(1, 2):
        year_xpath = "//h3[text()='Event History']/../a[" + str(i) + "]/text()"
        year = response.xpath(year_xpath)
        year = [int(i) for i in year]
        y = str(year[0])
        print("\nnavigating to the url for the oscars given in the year: " + y)
        oscar_nominees(url_opener(base_url + "event/ev0000003/" + y))
    return year


collect_years()
