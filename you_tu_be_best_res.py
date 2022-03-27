""" Simple youtube downloader best resolution video by URL """
from pytube import YouTube


def print_progress_bar(file_size: int, bytes_remaining: int) -> None:
    """ Visualizes the download progress """
    # rows, columns = os.popen('stty size', 'r').read().split()
    fill_empty = ' '
    fill_full = '#'
    fill_width = 48

    current_percent = (file_size - bytes_remaining) / file_size

    filled_length = int(fill_width * current_percent)
    empty_length = fill_width - filled_length
    # bar = f'| {fill_full*filled_length + fill_empty*empty_length} | {bytes_remaining} bytes of {file_size} bytes.'
    bar = f'| {fill_full * filled_length + fill_empty * empty_length} | '

    print(f'Downloaded:{bar} {current_percent:.0%}', end='\n' if current_percent >= 1.0 else '\r')


def get_video(url: str, path: str = 'video/') -> None:
    """
    Download the best resolution video by URL

    :param url: video url address
    :param path: video save folder (default = 'video/')
    """

    def on_progress(stream, chunk, bytes_remaining: int):
        print_progress_bar(file_size, bytes_remaining)

    def on_complete(stream, path: str):
        print("File saved as:\n" + path)

    # print('\n============== Video info ==============')
    print('\nVideo and audio info:')
    yt = YouTube(url, on_progress_callback=on_progress, on_complete_callback=on_complete)
    print(f'Title: {yt.title}')
    print(f'Author: {yt.author}')

    # print('\n============ Start download ============')
    file_size = int(yt.streams.filter(progressive=True, file_extension='mp4')
                    .order_by('resolution').desc().first().filesize)
    print(f"File size {file_size: _} bytes")
    # yt.streams.get_by_itag(i_tag[video_number]).download('video/')
    yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(path)
    # print('================ Done! =================')


def main():
    url = input('Enter the YouTube URL: ')
    get_video(url)


if __name__ == '__main__':
    main()
