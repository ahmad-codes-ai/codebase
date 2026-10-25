import re


pattern = r'<([^>]+)>;\s*rel="next"'
text = '<https://api.github.com/repos?page=2>; rel="next"'


def extract(pattern,header):

    if not header:
        return None   # safety check
    
    match = re.search(pattern, header)  #github link <([^>]+)>;\s*rel="next"
    return match.group(1) if match else None





