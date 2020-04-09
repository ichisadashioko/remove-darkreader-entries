# Remove site list entries from [Dark Reader](https://github.com/darkreader/darkreader) extension

After using Dark Reader for a few months, my site list has been growing and this affects my browsing experience a lot.

For example:

- Everytime I run a ASP.NET app, IIS will assign it a random port (e.g. `localhost:55167`) and every `localhost` website will share Dark Reader configuration.
- Recently, when I toggle any `localhost` sites, they will not change from `dark` to `light` or reverse. I must toggle the option `Invert list only`/`Not invert list` to deal with this behavior in the mean time. I suspect that there are many `localhost` sites with different port in the site list but I only toggle the `localhost` site with its current port number. There are still many other `localhost` sites in the site list.

I tried to dig through Dark Reader code for filtering/deleting my site list but the codebase is huge for me. There are many design decisions in there but there is no comment/documentation explain how things work so I gave up on the codebase.

I can remove the site list manually from the Dark Reader popup but my number of sites in there has been growing to 3 digits. I cannot delete all of them manually.

Because of that, I decide to create a Python script to automate the task for me.

# How to use the script

## Install dependencies

```bash
pip install -r ./requirements.txt
```

## Run the script

> Check the content of the script before runnning. I not responsible for any works you may lost while you are using the script.

```
python main.py
```

## Move the cursor to the starting site in Dark Reader popup

- Open Dark Reader by click on the extension icon
- Open `Site List`
- Scroll to the first site in the list
- Place the cursor on the first site

## Star the automation

- Press `F9` to start or pause
- Press `ESC` to end the program

Start the automating process with `F9` and leave the computer there until there is no site entry left then press `ESC` to end the program.