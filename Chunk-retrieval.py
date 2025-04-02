for elem in ibanChunk:
    if isinstance(elem, nltk.Tree):
        ibanString = ""
        for (text, tag) in elem:
            ibanString += text
        chunkList.append(ibanString)
