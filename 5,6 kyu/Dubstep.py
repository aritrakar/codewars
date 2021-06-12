# https://www.codewars.com/kata/551dc350bf4e526099000ae5/train

def song_decoder(song):
    return " ".join(filter(lambda x: len(x) > 0, song.split("WUB")))
