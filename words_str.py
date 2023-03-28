# from urllib.request import urlopen
# story = urlopen('http://sixty-north.com/c/t.txt')
# story_words = []
# for line in story:
#     line_words = line.split()
#     for word in line_words:
#         story_words.append(word)


# since http is returned in bytes b before each word.


# below is improved
from urllib.request import urlopen

def fetch_words():
    story = urlopen('http://sixty-north.com/c/t.txt')
    story_words = []
    for line in story:
        line_words = line.decode('utf8').split()
        for word in line_words:
            story_words.append(word)
    story.close()

    for word in story_words:
        print(word)

# print(__name__)

def print_items(items):
    for word in items:
        print(word)

def main():
    words = 

if __name__ == '__main__':
    fetch_words()