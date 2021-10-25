# 8-8. User Albums: Start with your program from Exercise 8-7. Write a while
# loop that allows users to enter an album’s artist and title. Once you have that 
# information, call make_album() with the user’s input and print the dictionary 
# that’s created. Be sure to include a quit value in the while loop.

def make_album(artist_name,album_title,num_tracks,album_genre,album_year):
    album_info = {'band name' : artist_name , 'album title': album_title , 'number of tracks':num_tracks,'genre' : album_genre, 'year released':album_year}
    return album_info


def main():
    user_input = True
    while(user_input):
        print("please enter some information about an album you would like to store:".title())
        artist_name = input("please enter the name of the artist:".title())
        album_title = input("please enter the album name:".title())
        num_tracks = input("please enter the number of tracks:".title())
        album_genre = input("please enter the album's genre:".title())
        album_year = input("please enter the release year:".title())
        album_info = make_album(artist_name,album_title,num_tracks,album_genre,album_year)
        user_input = False


    for key,val in album_info.items():
        print(key.title(),':', val.title())

if(__name__ == '__main__'):
    main()