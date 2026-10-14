import wordninja
import sys

SPECIAL = {
    "space": " ",
    "enter": "\n",
    "backspace": "<BS>",
    "num_lock": "#",
    "ctrl": "",
    "alt": "",
    "shift": "",
    "shift_l": "",
    "shift_r": "",
    "caps_lock": "",
    "ctrl_l": "",
    "ctrl_r": "",
    "alt_l": "",
    "alt_r": "",
}


# --- Load the raw tokens ---
def load_tokens(path):
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        return [line.replace("'", "") for line in f.read().splitlines()]


# --- Clean up the tokens ---
def normalize_tokens(tokens):
    buffer = []

    for t in tokens:
        t = t.lower()
        
        if t in SPECIAL:
            buffer.append(SPECIAL[t])
        elif len(t) == 1:
            buffer.append(t)
        elif t.startswith("key."):
            name = t[4:]
            buffer.append(SPECIAL.get(name, f"<{name.upper()}>"))
        else:
            buffer.append(f"<{t.upper()}>")

    return buffer


def apply_edit(keys):
    buffer = []
    for k in keys:
        if k == "<BS>" and buffer:
            buffer.pop()
        else:
            buffer.append(k)
    return "".join(buffer)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"usage: python {sys.argv[1]} keys.txt")
        sys.exit(1)

    raw = load_tokens(sys.argv[1])
    raw = normalize_tokens(raw)
    sentences = apply_edit(raw)
    
    print("\n=== Raw ===")
    print(sentences)

    # Normalize the words
    words = wordninja.split(sentences)
    print("\n=== Normalized ===")
    print(words)