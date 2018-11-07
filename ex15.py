import string
freq = {}
song = "Do you remember the 21st night of September? Love was changin' the minds of pretenders While chasin' the clouds away Our hearts were ringin' in the key that our souls were singin' As we danced in the night, remember How the stars stole the night away, oh, yeah yeah yeah Hey, hey, hey! Ba-dee ya, say, do you remember? Ba-dee ya, dancin' in September Ba-dee ya, never was a cloudy day Ba duda, ba duda, ba duda, badu Ba duda, badu, ba duda, badu Ba duda, badu, ba duda My thoughts are with you, holdin hands with your heart to see you Only blue talk and love, remember How we knew love was here to stay Now in December, found the love that we shared in September Only blue talk and love, remember, the true love we share today Hey, hey, hey! Ba-dee ya, say, do you remember? Ba-dee ya, dancin' in September Ba-dee ya, never was a cloudy day There was a... Ba-dee ya, (dee ya dee ya) say, do you remember? Ba-dee ya, (dee ya dee ya) dancin' in September Ba-dee ya, (dee ya dee ya) golden dreams were shiny days The bell was ringin', oh oh Our souls were singin' Do you remember never a cloudy day? Yow There was a... Ba-dee ya, (dee ya dee ya) say, do you remember? Ba-dee ya, (dee ya dee ya) dancin' in September Ba-dee ya, (dee ya dee ya) never was a cloudy day And we'll say... Ba-dee ya, (dee ya dee ya) say, do you remember? Ba-dee ya, (dee ya dee ya) dancin' in September Ba-dee ya, (dee ya dee ya) golden dreams were shiny days Ba-dee ya, dee ya dee ya Ba-dee ya, dee ya dee ya Ba-dee ya, dee ya dee ya, dee ya! Ba-dee ya, dee ya dee ya Ba-dee ya, dee ya dee ya Ba-dee ya, dee ya dee ya, dee ya!"

#Format Lyrics
songList = []
songFormatted = []
numbers = [0,1,2,3,4,5,6,7,8,9]
song = song.lower()
for i in song:
    if i in string.ascii_lowercase or i is " " or i in numbers:
        songFormatted.extend(i)
songFormatted = "".join(songFormatted)
songList = songFormatted.split(" ")

#Create Dictionary
for i in songList:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

#Find Word with (valueReq) apperences
def Find_Key(valueReq):
    resultsKey = []
    for key, value in freq.items():
        if value == valueReq:
            resultsKey.append(key)

    if len(resultsKey) == 0:
        print("There are no words that occure that many times.")
    else:
        print(f"{resultsKey} appears times {valueReq} times.")

def Find_Max():
    maxValue = max(freq.values())
    maxKey = [key for (key,value) in freq.items()if value == maxValue]
    return maxKey

Find_Key(int(input("Enter the frequency of the word you want to find: ")))
print(f"The word that appears the most is {Find_Max()} which appears {max(freq.values())} times.")
