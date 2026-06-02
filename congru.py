def modexp(a, b, m):
    r = 1
    a %= m
    while b > 0:
        if b & 1:
            r = (r * a) % m
        a = (a * a) % m
        b //= 2
    return r

def extract_mod(s):
    s = s.lower()
    for k in ("modulo", "%"):
        if k in s:
            i = s.rfind(k)
            n = ""
            for c in s[i+len(k):]:
                if c.isdigit() or (c == '-' and not n):
                    n += c
                elif n:
                    break
            return s[:i], int(n)
    return s, None

def congru():
    try:
        txt, B = extract_mod(input("A: "))
        if B is None:
            B = int(input("B: "))
        txt = txt.replace(" ", "")
        if txt[0] == "-":
            txt = "0" + txt
        txt = txt.replace("-", "+-")
        total = 0
        for t in txt.split("+"):
            if not t: continue
            s = -1 if t[0] == "-" else 1
            t = t[1:] if t[0] == "-" else t
            if not t: continue
            if "^" in t or "**" in t:
                p = t.split("**",1) if "**" in t else t.split("^",1)
                val = modexp(int(p[0]), int(p[1]), B)
            else:
                val = int(t) % B
            total = (total + s * val) % B
        print("R:", total)
    except:
        print("ERREUR")

congru()
