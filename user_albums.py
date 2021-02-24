'''Start with your program from Exercise 8-7. Write a while
loop that allows users to enter an album’s artist and title. Once you have that
information, call make_album() with the user’s input and print the dictionary
that’s created. Be sure to include a quit value in the while loop.'''

def make_album (album_artist,album_title):
    album_new = {}
    album_new['alb_artist'] = album_artist
    album_new['alb_title'] = album_title
    return album_new

while True:
    print ("Please enter the following data")
    print ("Please enter q at any point of time to quit")

    artist = input ("Please enter the artist name: ")
    if artist == 'q':
        break

    title = input ("Please enter the title of the album: ")
    if title == 'q':
        break

    album = make_album (artist, title)
    print (album)





    

