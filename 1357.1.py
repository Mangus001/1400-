text = "ваш текст"
digit_counts = {str(d): 0 for d in range(10)}
for ch in text:
    if ch.isdigit():
        digit_counts[ch] += 1
