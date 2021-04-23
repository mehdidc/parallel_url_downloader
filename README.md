# What is it?

This is a simple script that works on the top of Aria2 (<https://aria2.github.io/>),
to make it easy to download a large number of urls.

# How to Install ?

1. Install Aria2 <https://aria2.github.io/>, in Debian/Ubuntu you can use `sudo apt install aria2`
2. Install the script: `pip install git+https://github.com/mehdidc/parallel_url_downloader`

# How to use ?

## Step 1: getting a url file

First, you need a file containing urls, one url per line.
For instance, you can try `wget https://gist.githubusercontent.com/mehdidc/9d62e587fad8713b9ad045b30ea66182/raw/3bba052ce1678b2e4a814758533d87d0451c0562/urls_conceptual_captions_validation.txt --output-document=urls.txt` as an example, these are urls from
the Conceptual Captions dataset <https://ai.google.com/research/ConceptualCaptions/download>,
validation split.

Once this is done, you should have a filename `urls.txt` (can be any name)

## Step 2: making chunks

Here, we make a set of independent chunks of the urls, where we also specify
the output filename associated to each url. 

`parallel_url_downloader make-chunks urls.txt --nb-chunks=16`

This will make 16 chunks, by default named `chunk_0.txt`, `chunk_1.txt`, etc.
By default, the url in line `i` (starting from line 0) from `urls.txt` will be saved into `downloads/{i}.jpg`. 
This can be changed, check the documentation for more information `parallel_url_downloader --help`.
Note that in this step, nothing is downloaded, this step specifies which urls belong to which chunk and
the filename in local disk associated to each url.

## Step 3: download a chunk

To download a chunk, you can use:

`parallel_url_downloader download chunk_0.txt`

This will download the urls in `chunk_0.txt`
You can also easily download all the chunks in parallel using `xargs`:

`find -name 'chunk*.txt'| xargs -n1 -P8 python cli.py download`

here, `P8` specifies the total number of processes allowed in parallel (here 8), where each process
launches Aria to download a single chunk file.
