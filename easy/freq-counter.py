paragraph = """
Lorem Ipsum is simply dummy text of of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum selected selected selected selected selected selected selected you're you're you're you're you're you're you're you're Harshvardhan Harshvardhan Harshvardhan Harshvardhan Harshvardhan Harshvardhan Harshvardhan Harshvardhan Harshvardhan.
"""
print("Enter paragraph...or just hit enter if you're lazy...")
s = input().strip()
if(len(s) == 0):
    s = paragraph
    
print("Text:", s)
d = {}
for word in s.split():
    if word in d:
        curr_freq = d[word]
    else:
        curr_freq = 0
    d[word] = curr_freq + 1
    
d = sorted(d, key=d.get)[-3:]
d.reverse()
print("Top 3 frequent words: ", d)
print("\n")