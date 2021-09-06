from pytube import YouTube


def print_streams_info(iter, streams, i_tag):
    for stream in streams:
        str_to_print = str(iter) + ':'
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

        iter += 1
        i_tag.append(stream["itag"])
        print(str_to_print)

    return [iter, i_tag]


def get_video(url):
    print('\n============== Video info ==============')
    yt = YouTube(url)
    print(f'Title: {yt.title}')
    print(f'Author: {yt.author}')
    # print(f'Description = {yt.description}')

    streams = yt.streaming_data
    i = 1
    i_tag = [0]

    print('Progressive Formats:')
    i, i_tag = print_streams_info(i, streams['formats'], i_tag)

    print('Adaptive Formats:')
    i, i_tag = print_streams_info(i, streams['adaptiveFormats'], i_tag)

    print()
    video_number = int(input(f'Enter video number to download (1 to {i - 1}): '))

    print('\n============ Start download ============')
    print('It may take several minutes to complete ...')
    yt.streams.get_by_itag(i_tag[video_number]).download('video/')
    print('================ Done! =================')


def main():
    url = input('Enter the YouTube URL: ')
    get_video(url)


if __name__ == '__main__':
    main()
