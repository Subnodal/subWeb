import urllib.request

def get(url, follow = -1, highlight = -1):
    requests = urllib.request.urlopen(url)

    if url.endswith(".sw"):
        compilation = ""
        currentLink = ""
        currentHighlight = 0
        URLBounce = None

        for line in requests.readlines():
            line = line.decode("utf-8")

            if line.startswith("#"):
                pass
            elif line.startswith("\\"):
                compilation += "\n" + line[1:]
            elif line.startswith("[link] "):
                currentLink = line[7:]
            elif line.startswith("[linktext] "):
                if currentHighlight == highlight:
                    compilation += "[" + line[11:-1] + "]"
                else:
                    compilation += " " + line[11:-1] + " "
                
                currentHighlight += 1
            else:
                compilation += "\n" + line

            if currentHighlight == follow:
                URLBounce = currentLink

        return {
            "content": compilation,
            "URLBounce": URLBounce
        }
    else:
        return requests.readlines().decode("utf-8")