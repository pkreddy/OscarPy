# converts list to string
import traceback
def list_to_string(s_list):
    return str(s_list[0])


def cleanBestMovieData():
   file = open("data.txt", "r")
   fileWrite = open("cleanedData.csv", "w")
   line = file.readline()
   fileWrite.write(
        "Year,Movie,War, SciFi, Horror, Western, FilmNoir, Drama, Musical, Sport, Fantasy, Family, Romance, Action,"
        " Animation, Crime, Thriller, Adventure, Music, Comedy, Mystery, Biography, History,Oscar\n")
   i = 1
   oscar_result = "1"
   genre = []
   while line is not None:
       try:
            line = ((file.readline()).replace("\n", "")).split(",")
            War, SciFi, Horror, Western, FilmNoir, Drama, Musical, Sport, Fantasy, Family, Romance, Action, Animation, Crime, Thriller, Adventure, Music, Comedy, Mystery, Biography, History = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
            if len(line) == 1:
                break
            year = str(line[0])
            movie = str(line[1])
            oscar_result = str(line[4])
            for b in ((line[2]).split(":")):
                genre.append(b.strip())
            genre_count = float(len(genre))
            if "Horror" in genre:
                Horror = float(1 / genre_count)
            if "Action" in genre:
                Action = float(1 / genre_count)
            if "Comedy" in genre:
                Comedy = float(1 / genre_count)
            if "Adventure" in genre:
                Adventure = float(1 / genre_count)
            if "Thriller" in genre:
                Thriller = float(1 / genre_count)
            if "Fantasy" in genre:
                Fantasy = float(1 / genre_count)
            if "Crime" in genre:
                Crime = float(1 / genre_count)
            if "Biography" in genre:
                Biography = float(1 / genre_count)
            if "Drama" in genre:
                Drama = float(1 / genre_count)
            if "Sport" in genre:
                Sport = float(1 / genre_count)
            if "Sci-Fi" in genre:
                SciFi = float(1 / genre_count)
            if "Animation" in genre:
                Animation = float(1 / genre_count)
            if "Romance" in genre:
                Romance = float(1 / genre_count)
            if "Film-Noir" in genre:
                FilmNoir = float(1 / genre_count)
            if "War" in genre:
                War = float(1 / genre_count)
            if "Family" in genre:
                Family = float(1 / genre_count)
            if "History" in genre:
                History = float(1 / genre_count)
            if "Music" in genre:
                Music = float(1 / genre_count)
            if "Mystery" in genre:
                Mystery = float(1 / genre_count)
            if "Western" in genre:
                Western = float(1 / genre_count)
            if "Musical" in genre:
                Musical = float(1 / genre_count)
            print(line)
            if i==537:
                print ()
            print(War, SciFi, Horror, Western, FilmNoir, Drama, Musical, Sport, Fantasy, Family, Romance, Action,
                  Animation, Crime, Thriller, Adventure, Music, Comedy, Mystery, Biography, History)
            genre.clear()
            fileWrite.write(str(year) + " , " + str(movie) +"," + str(War) +"," + str(SciFi) +"," + str(Horror) +"," + str(Western) +"," + str(FilmNoir) +"," + str(Drama) +"," + str(Musical) +"," + str(Sport) +"," + str(Fantasy) +"," + str(Family) +"," + str(Romance) +"," + str(Action) +"," +
                            str(Animation) +"," + str(Crime) +"," + str(Thriller) +"," + str(Adventure) +"," + str(Music) +"," + str(Comedy) +"," + str(Mystery) +"," + str(Biography) +"," + str(History) +"," + oscar_result + '\n')
            i = i + 1
       except Exception as e:
        print ("Couldn't do it: %s" % e)
        traceback.print_exc()
        print("exception")
        file.close()
        fileWrite.close()
        exit()
   file.close()
   fileWrite.close()


def get_data():
    file = open("data.txt")
    genre = []
    for line in file:
        for b in (line.split(",")[2]).split(":"):
            genre.append(b.strip())
    file.close()
    # print(genre)
    a = (set(genre))
    print(a)


cleanBestMovieData()
