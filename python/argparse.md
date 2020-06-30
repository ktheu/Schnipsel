### Argparse

[doc](https://docs.python.org/3/library/argparse.html)

Datei argtest.py

```
import argparse
parser = argparse.ArgumentParser(description='Videos to images')
parser.add_argument('indir', type=str, help='Input dir for videos')
parser.add_argument('outdir', type=str, help='Output dir for image')
args = parser.parse_args()
print(args.indir)
```

Aufruf mit 

```
python argtest.py  /videos  /images
python argtest.py -h     # gibt Hilfetext
python argtest.py --help
```

Ein positionales Argument:

```
parser.add_argument('indir', type=str, help='Input dir for videos')
```

Optionale Argumente mit `--` oder 
```
parser = argparse.ArgumentParser(description='My example explanation')
parser.add_argument(
    '--my_optional',
    default=2,
    help='provide an integer (default: 2)'
)
my_namespace = parser.parse_args()
print(my_namespace.my_optional)
```