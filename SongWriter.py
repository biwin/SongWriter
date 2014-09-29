# This script copies lyrics text from the provided web link from
# azlyrics.com. to a text file. Wrote it for educational purpose only!!
# Uses python3's urllib and data structures - level intermediate

# Legal disclaimer: I have no connection with the www.azlyrics.com.
# Lyrics fetched by this script may be copyrighted by the authors, it's up to
# you to determine whether this is the case, and if so, whether you are entitled
# to request/use those lyrics. You will almost certainly not be allowed to use
# the lyrics obtained for any commercial purposes.

__author__ = 'biwin'
import urllib.request

proceed = False

while proceed is False:
	url = str(input("Enter the azLyrics url you want to download !!"))
	url_parts = url.split('.com')
	if url_parts[0] == 'http://www.azlyrics':
		proceed = True
	elif url_parts[0] == 'www.azlyrics':
		url_parts[0] = 'http://www.azlyrics'
		url = '.com'.join(url_parts)
		proceed = True
	elif url_parts[0] == 'azlyrics':
		url_parts[0] = 'http://www.azlyrics'
		url = '.com'.join(url_parts)
		proceed = True
	else:
		print('Enter the URL again!')

print('Opening the URL....')

try:
	# opens the url
	# url = "http://www.azlyrics.com/lyrics/eminem/stan.html"
	page = urllib.request.urlopen(url)
	text = page.read().decode('utf8')
except (ValueError, RuntimeError, TypeError, NameError):
	print("Unable to open the URL")


# clears the html tags
def clear_html_tags(content):
	content = content.replace("<i>", "")
	content = content.replace("</i>", "")
	content = content.replace("<br>", "")
	content = content.replace("<br />", "")
	content = content.replace(">", "")
	return content


# finds the given fields
def find_text(find_this):
	position = text.find(find_this)
	return position


# writes to a file
def write_lyrics(final_artist, final_title, final_lyric):
	filename = final_artist + " - " + final_title + " lyrics.txt"
	dislclaimer = final_artist + ' lyrics are property and copyright of their owners.\n \
	"' + final_title + '" lyrics provided for educational purposes and personal-\nuse only. Phrased from azlyrics.com \n'
	line = " - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n"
	a = open(filename, 'w')
	a.write(dislclaimer + line + "\n\n")
	a.write("Artist: " + final_artist + "\n")
	a.write("Song Title: " + final_title + "\n ")
	a.write(final_lyric)
	a.write("\n\n\n" + line + dislclaimer + line)
	a.close()


print('Fetching the metadata...')


# grabs the song info
artist_start = find_text('ArtistName')
artist_end = find_text('SongName')

artemp = text[artist_start:artist_end]
artist_list = artemp.split('"')[1::2]

song_title_start = text.find('><h1>')
song_title_end = text.find('</h1></div>')
title_temp = text[song_title_start:song_title_end]
title_list = title_temp.split('"')[1::2]

title = title_list[0]

artist = artist_list[0]

print('Fetching the lyrics...')
# grabs the song lyrics

lyric_start = find_text('"margin-left:10px;margin-right:10px;">') + 63
lyric_end = find_text('<!-- end of lyrics -->')
lyric = text[lyric_start:lyric_end]

lyric = clear_html_tags(lyric)

artist = artist.title()
title = title.title()

print('Writing the lyrics file...')
# writes the file
write_lyrics(artist, title, lyric)
print("Downloading finished without any errors")
