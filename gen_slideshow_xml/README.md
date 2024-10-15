# Ubuntu Wallpaper Slideshow XML generator

## Usage
```
usage: gen_slideshow_xml.py [-h] -p PATH [-o OUTPUT] [-r] [--transition TRANSITION] [--static STATIC]

XML generator for Ubuntu wallpaper slideshow

options:
  -h, --help            show this help message and exit
  -p PATH, --path PATH  Path of pictures floder
  -o OUTPUT, --output OUTPUT
                        Output XML file name (default wallpaper-slideshow.xml)
  -r, --random          Shuffle the picture list randomly
  --transition TRANSITION
                        Transition time between two pictures (default 1.0 second)
  --static STATIC       Static time that one picture is shown (default 599.0 second)
```

### Apply Slideshow XML to System
Tested on Ubuntu 24.04
```
gsettings set org.gnome.desktop.background picture-uri "file:///path/to/xmlfile"
gsettings set org.gnome.desktop.background picture-uri-dark "file:///path/to/xmlfile"
```

### Verify Slideshow XML on System
Tested on Ubuntu 24.04
```
gsettings get org.gnome.desktop.background picture-uri
gsettings get org.gnome.desktop.background picture-uri-dark
```
