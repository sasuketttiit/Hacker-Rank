def designerPdfViewer(h, word):
    max_height = height = 0
    for i in word:
        height = h[ord(i)-ord('a')]
        if height > max_height:
            max_height = height
    return max_height*len(word)
