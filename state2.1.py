text = "X-DSPAM-Confidence:    0.8475"

txtLn = len(text) #length of the text
srt = text.find(':') #finding a position of the ":"
num= text[srt+1:txtLn]
final = num.lstrip() #removing whitespave from the left
print(float(final))

