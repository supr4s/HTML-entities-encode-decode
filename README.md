# HTML-entities-encode-decode
Script for fast decoding/encoding of HTML entities

## Example

Encoded : 

```
$ python3 html-entities.py --encode='alert(document.domain)'             
Encoded: &#97&#108&#101&#114&#116&#40&#100&#111&#99&#117&#109&#101&#110&#116&#46&#100&#111&#109&#97&#105&#110&#41
```

Encoded + URL encoding

```
$ python3 html-entities.py --encode='alert(document.domain)' --url-encode
Encoded: %26%2397%26%23108%26%23101%26%23114%26%23116%26%2340%26%23100%26%23111%26%2399%26%23117%26%23109%26%23101%26%23110%26%23116%26%2346%26%23100%26%23111%26%23109%26%2397%26%23105%26%23110%26%2341
```

Decoded : 

```
$ python3 html-entities.py --decode='&#72&#105&#89&#111&#117'
Decoded: HiYou
```
