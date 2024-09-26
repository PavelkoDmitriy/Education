def all_variants(text):
    for length in range(1, len(text) + 1):
        for start in range(len(text) - length + 1):
            yield text[start:start + length]


text = "abc"
generator = all_variants(text)
for variant in generator:
    print(variant)
