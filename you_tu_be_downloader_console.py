""" Simple youtube downloader by URL """
from pytube import YouTube


def print_streams_info(m_iter, streams, yt, i_tag):
    """ Shows available videos and audios for download """
    for stream in streams:
        str_to_print = str(m_iter) + ':'
        try:
            str_to_print += f'\t{stream["qualityLabel"]}'
        except KeyError:
            pass
        try:
            str_to_print += f'\tWidth: {stream["width"]}'
        except KeyError:
            pass
        try:
            str_to_print += f'\tHeight: {stream["height"]}'
        except KeyError:
            pass
        try:
            str_to_print += f'\tBitrate: {stream["bitrate"]}'
        except KeyError:
            pass
        try:
            str_to_print += f'\tFPS: {stream["fps"]}'
        except KeyError:
            pass
        try:
            str_to_print += f'\tAudio channels: {stream["audioChannels"]}'
        except KeyError:
            pass
        try:
            str_to_print += f'\tAudio rate: {stream["audioSampleRate"]}'
        except KeyError:
            pass
        try:
            # file_size = round(int(yt.streams.get_by_itag(stream["itag"]).filesize) / 1024 / 1024, 3)
            file_size = int(yt.streams.get_by_itag(stream["itag"]).filesize)
            str_to_print += '\t File size: ' + str(file_size) + ' bytes'
        except KeyError:
            pass

        m_iter += 1
        i_tag.append(stream["itag"])
        print(str_to_print)

    return [m_iter, i_tag]


def get_video(url):

    def on_progress(stream, chunk, bytes_remaining):
        percent = (file_size - bytes_remaining) / file_size
        print(f'Downloaded: {percent:.0%}', end='\r')

    def on_complete(stream, path):
        print("\nFile saved as:\n" + path)

    # print('\n============== Video info ==============')
    print('\nVideo and audio info:')
    yt = YouTube(url, on_progress_callback=on_progress, on_complete_callback=on_complete)
    # yt = YouTube(url)
    print(f'Title: {yt.title}')
    print(f'Author: {yt.author}')
    # print(f'Description = {yt.description}')

    streams = yt.streaming_data
    i = 1
    i_tag = [0]

    print('Progressive Formats:')
    i, i_tag = print_streams_info(i, streams['formats'], yt, i_tag)

    print('Adaptive Formats:')
    i, i_tag = print_streams_info(i, streams['adaptiveFormats'], yt, i_tag)

    print()
    video_number = int(input(f'Enter video or audio number to download (1 to {i - 1}): '))

    # print('\n============ Start download ============')
    # print('It may take several minutes to complete ...')
    file_size = int(yt.streams.get_by_itag(i_tag[video_number]).filesize)
    yt.streams.get_by_itag(i_tag[video_number]).download('video/')
    # print('================ Done! =================')


def main():
    url = input('Enter the YouTube URL: ')
    get_video(url)


if __name__ == '__main__':
    main()
