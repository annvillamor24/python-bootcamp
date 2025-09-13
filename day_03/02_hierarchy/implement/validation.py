


class ImageFileValidator:
    def __init__(self, path):
        self.path = path

    def valid(self):
        if self.path.endswith(".jpg"):
            return True
        if self.path.endswith(".png"):
            return True
        if self.path.endswith(".jpeg"):
            return True
        else:
            return False


class DocumentValidator:
    def __init__(self, path, pages):
        self.path = path
        self.pages = pages

    def valid(self):
        if self.path.endswith(".pdf") and self.pages > 0:
            return True
        else:
            return False

class AudioFileValidator:
    def __init__(self, path, length):
        self.path = path
        self.length = length

    def valid(self):
        if self.path.endswith(".mp3") and self.length > 0:
            return True
        else:
            return False

class VideoFileValidator:
    def __init__(self, path, length, res):
        self.path = path
        self.length = length
        self.res = res

    def valid(self):
        if self.path.endswith(".mp4") and self.length > 0 and self.res == "720" or self.res == "1080":
            return True
        else:
            return False

validators = [
    ImageFileValidator("image.JPG"),
    DocumentValidator("document.PDF",10),
    AudioFileValidator("audio.MP3",1000),
    VideoFileValidator("video.MP4", 10_000, 1080),
]
for validator in validators:
    print(validator.valid())