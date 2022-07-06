import string
import Pyro4
from ytmusicapi import YTMusic
ytmusic = YTMusic()

class Video():
    url: str
    title: str
    duration: str
    artirst: str

    def __init__(self, url: str, title: str, duration: str, artirst: str) -> None:
        self.url = url
        self.title = title
        self.duration = duration
        self.artirst = artirst

    def toString(self):
        return f'Título: {self.title}\nArtista: {self.artirst}\nurl: {self.url}\nDuração: {self.duration}'

@Pyro4.expose
@Pyro4.behavior(instance_mode="single")
class Youtube(object):
    def __init__(self) -> None:
        self.queue = []

    def search(self, video: string):
        video_info = ytmusic.search(video)[0]
        new_video = Video(url= f"https://www.youtube.com/watch?v={video_info['videoId']}",
            title=video_info['title'],
            duration=video_info['duration'],
            artirst=(video_info['artists'][0])['name']
            )
        self.queue.append(new_video)
        return new_video.toString()

    def list_queue(self):
        queue_to_string = ''
        for i in range(len(self.queue)):
            queue_to_string += f'[{i}] - {self.queue[i].title}\n'
        return queue_to_string
        
    def get_video_by_index(self, index: int):
        return(self.queue[index].toString())



def main():
    Pyro4.Daemon.serveSimple(
            {
                Youtube: "example.youtube"
            },
            ns = False)

if __name__=="__main__":
    main()

