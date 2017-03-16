import urllib.request
from bs4 import BeautifulSoup
from lxml import html

base_url = "http://www.imdb.com/"
file = open("data.csv", "w")
file.write("year,movie,movie_genre,category,oscar_result\n")
file.close()


# gives the response of the url as tree
def url_opener(url):
    # response = urllib.request.urlopen("http://www.imdb.com/event/ev0000003/2017")
    print("\nreading the response to the url -" + url)
    response = urllib.request.urlopen(url)
    # print(response.read())
    soup = BeautifulSoup(response, 'html.parser')
    # print(soup.prettify())
    tree = html.fromstring(str(soup))
    return tree


# create a data file
def data_file():
    return


# converts list to string
def list_to_string(s_list):
    return str(s_list[0])


# write the data to csv file
def write_to_csv(data):
    file = open("data.csv","a")
    file.write(data)
    file.write("\n")
    file.close()
    return


# gives all the information about the given movie
def get_movie_data():
    return


# returns the genre of the movie
def get_genre(href):
    response = url_opener(base_url + href[1:])
    temp = response.xpath("//div[@itemprop='genre']/a/text()")
    genre = ":".join(temp)
    return genre


# gives all the information about the film crew
def get_film_crew_data():
    return


def oscar_nominees(response, year):
    all_categories = response.xpath("//*[@id='main']/div[1]/blockquote/blockquote")
    print("\nTotal categories nominated for the oscars " + str(len(all_categories)))
    print("\n All the categories")
    print("---------------------")
    categories = (response.xpath("//*[@id='main']/div[1]/blockquote[1]/h2/text()"))
    # for i in categories :
    # print("-->"+i)
    # for i in range(1, len(categories)+1):
    for i in range(1, 2):
        print("\n-->" + categories[i - 1] + year)

        print()
        total_nominees = response.xpath("//*[@id='main']/div[1]/blockquote[1]/blockquote[" + str(i) + "]/div")

        for j in range(1, len(total_nominees) + 1):
            # for j in range(1, 2):
            if j == 1:
                print("******winner******")
                # //*[@id='main']/div[1]/blockquote[1]/blockquote[1]/div[1]/strong/a/text()
                movie = list_to_string(response.xpath(
                    "//*[@id='main']/div[1]/blockquote[1]/blockquote[" + str(j) + "]/div[1]/strong/a/text()"))
                movie_href = list_to_string(response.xpath(
                    "//*[@id='main']/div[1]/blockquote[1]/blockquote[" + str(j) + "]/div[1]/strong/a/@href"))
                movie_genre = get_genre(movie_href)
                movie_genre = movie_genre.replace(",","")
                movie = movie.replace(",","")
                movie_href = movie_href.replace(",","")
                print(movie + movie_href + movie_genre)
                write_to_csv(year+","+movie+","+movie_genre+","+categories[i - 1]+","+"1")
                print()
                if categories[i - 1] == 1:
                    get_genre(response.xpath(
                        "//*[@id='main']/div[1]/blockquote[1]/blockquote[" + str(j) + "]/div[1]/strong/a/@href"))
                print('||||||Nominees||||||')
            else:
                movie = list_to_string(response.xpath(
                    "//*[@id='main']/div[1]/blockquote[1]/blockquote[" + str(i) + "]/div[" + str(
                        j) + "]/strong/a/text()"))
                movie_href = list_to_string(response.xpath(
                    "//*[@id='main']/div[1]/blockquote[1]/blockquote[" + str(i) + "]/div[" + str(
                        j) + "]/strong/a/@href"))
                movie_genre = get_genre(movie_href)
                movie_genre = movie_genre.replace(",","")
                movie = movie.replace(",","")
                movie_href = movie_href.replace(",","")
                print(movie + movie_href + movie_genre)
                write_to_csv(year + "," + movie + "," + movie_genre + "," +categories[i - 1]+","+ "0")
                # //*[@id='main']/div[1]/blockquote[1]/blockquote[1]/div[1]/strong/a/text()
    other_categories = len(response.xpath("//div[@class='award']"))

    # for i in range(2, other_categories + 1):
    #     print("category")
    #     print(response.xpath("//div[@class='award'][" + str(i) + "]/h1/text()"))
    #     print("winners")
    #     for j in range(1, len(response.xpath("//div[@class='award'][" + str(i) + "]//div/div/a")) + 1):
    #         print(response.xpath(
    #             "//div[@class='award'][" + str(i) + "]/blockquote/blockquote/div[" + str(j) + "]/a/text()"))
    #         print(response.xpath(
    #             "//div[@class='award'][" + str(i) + "]/blockquote/blockquote/div[" + str(j) + "]/a/@href"))
    return


# for loop to navigate so url's based on year
def collect_years():
    # ****** change the start_year in the url when you need to include latest oscar data *****
    start_year = "2017"
    response = url_opener(base_url + "event/ev0000003/" + start_year)
    oscar_nominees(url_opener(base_url + "event/ev0000003/" + start_year), start_year)
    a = response.xpath("//h3[text()='Event History']/../a")
    # change (1,3) to len(a)
    for i in range(1, len(a)):
        year_xpath = "//h3[text()='Event History']/../a[" + str(i) + "]/text()"
        year = response.xpath(year_xpath)
        year = [int(i) for i in year]
        y = str(year[0])
        year_href = list_to_string(response.xpath("//h3[text()='Event History']/../a[" + str(i) + "]/@href"))
        oscar_nominees(url_opener(base_url + year_href[1:]), y)
    return year


collect_years()
