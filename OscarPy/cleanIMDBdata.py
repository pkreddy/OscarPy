# converts list to string
def list_to_string(s_list):
    return str(s_list[0])

def cleanBestMovieData:
 file = open("data.csv","r")
 fileWrite = open("cleanData.csv","w")
 a = file.readline(1)
 i = 2
 while a is not None:
  line = (file.readline(i)).split(",")
  year = list_to_string(line[0])
  movie = list_to_string(line[1])
  genre = (list_to_string(line[2])).split(":")
  genre_count = len(genre)
  oscar_result = list_to_string(line[4])

def get_data:
