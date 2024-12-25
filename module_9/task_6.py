def all_variants(text):
    text = text.product
    yield all_variants(text)


a = all_variants("abc")
for i in a:
    print(i)
