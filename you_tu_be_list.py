""" Simple youtube downloader list the best resolution video by URL """
from you_tu_be_best_res import get_video
from pytube import Playlist
from os import mkdir


def get_video_list(url):
    symbols_to_remove = '~@#$%^-_(){}+=[]:;«,./?\*<>|'

    pl = Playlist(url)
    folder = pl.title
    for s in symbols_to_remove:
        folder = folder.replace(s, '')
    try:
        mkdir('video/' + folder)
    except FileExistsError:
        print(f'Folder "{folder}" already exist.')

    count = 1
    max_count = len(pl)
    print(f'Total {max_count} videos.')

    for url in pl.video_urls:
        i = 0
        while i < 3:
            try:
                count += 1
                get_video(url=url, path='video/' + folder)
                print(f'[{count}|{max_count}]')
                break
            except Exception as e:
                print(e, end='')
                print('. Try again')


def main():
    url = input('Enter the YouTube URL: ')
    get_video_list(url)


if __name__ == '__main__':
    main()
