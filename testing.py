from lyrics_extractor import SongLyrics
extract_lyrics = SongLyrics("AIzaSyCBZHXigBymV1utxKV6oI3sNLceK693CdE", "30796381ecf94465b")
data = extract_lyrics.get_lyrics("Shape of you")
print(data)