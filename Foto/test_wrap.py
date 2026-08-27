# Let's test the enhanced concept map generator and visual card rendering

def test_text_wrapping():
    def wrap_text(text, max_len=16):
        words = text.split()
        lines = []
        current = []
        cur_len = 0
        for w in words:
            if cur_len + len(w) + (1 if current else 0) <= max_len:
                current.append(w)
                cur_len += len(w) + (1 if len(current) > 1 else 0)
            else:
                if current:
                    lines.append(" ".join(current))
                current = [w]
                cur_len = len(w)
        if current:
            lines.append(" ".join(current))
        return lines[:3]

    print("Wrapped 'Le 5 Giornate di Milano e la diplomazia di Cavour':", wrap_text('Le 5 Giornate di Milano e la diplomazia di Cavour', 16))
    print("Wrapped 'Business Planning & Market Research':", wrap_text('Business Planning & Market Research', 16))

test_text_wrapping()
