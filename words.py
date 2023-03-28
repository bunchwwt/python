"""
Retrieve and print words from a URL. 
Usage:
python3 words.py <URL>
"""
#!/
# Modularity
import sys
from urllib.request import urlopen

def fetch_words(url):
    """
    Fetch a list of words from a URL.
    Args:
        url: The url of a UTF-8 text document. 
        
    Returns:
        A list of strings containing the words from the document. 
    """
    story = urlopen(url)
    story_words = []
    for line in story:
        line_words = line.decode('utf8').split()
        for word in line_words:
            story_words.append(word)
    story.close()
    return story_words

def print_items(story_items):
    for item in story_items:
        print(item)

#allows you to test in repl aka console
def main():
    words = fetch_words()
    print_items(words)

if __name__ == '__main__':
    main(sys.argv[1]) # The 0th arg is the module filename. 