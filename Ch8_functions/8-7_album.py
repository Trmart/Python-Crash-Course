# 8-7. Album: Write a function called make_album() that builds a dictionary 
# describing a music album. The function should take in an artist name and an 
# album title, and it should return a dictionary containing these two pieces of 
# information. Use the function to make three dictionaries representing different 
# albums. Print each return value to show that the dictionaries are storing the 
# album information correctly.
# Add an optional parameter to make_album() that allows you to store the 
# number of tracks on an album. If the calling line includes a value for the number of tracks, add that value to the album’s dictionary. Make at least one new 
# function call that includes the number of tracks on an album.

def make_album(artist_name,album_title,num_tracks,album_genre,album_year):
    album_info = {'band name' : artist_name , 'album title': album_title , 'number of tracks':num_tracks,'genre' : album_genre, 'year released':album_year}
    return album_info


def main():
    album_info = make_album('trivium', 'court of the dragon' ,'10', 'metal','2021')
    for key,val in album_info.items():
        print(key.title(),':', val.title())

if(__name__ == '__main__'):
    main()