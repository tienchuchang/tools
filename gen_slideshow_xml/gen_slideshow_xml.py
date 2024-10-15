#!/usr/bin/python3

import os
import datetime
import random
import argparse
import xml.etree.ElementTree as ET

def getPictureList(picPath, rand=False):
    result = []
    picPath = os.path.abspath(picPath)

    for root, sub, files in os.walk(picPath):
        for f in files:
            if f.endswith(('.jpeg','.jpg')):
                result.append(os.path.join(root, f))

    if rand == True:
        random.shuffle(result)

    return result

def generateXML(picList, staticSecond, transSecond, output):
    root = ET.Element('background')

    now = datetime.datetime.now()
    starttime = ET.Element('starttime')
    ET.SubElement(starttime, 'year').text = f'{now.year}'
    ET.SubElement(starttime, 'month').text = f'{now.month:02}'
    ET.SubElement(starttime, 'day').text = f'{now.day:02}'
    ET.SubElement(starttime, 'hour').text = f'00'
    ET.SubElement(starttime, 'minute').text = f'00'
    ET.SubElement(starttime, 'second').text = f'00'
    root.append(starttime)

    for i in range(len(picList)):
        if i > 0:
            trans = ET.Element('transition')
            ET.SubElement(trans, 'duration').text = str(transSecond)
            ET.SubElement(trans, 'from').text = picList[i - 1]
            ET.SubElement(trans, 'to').text = picList[i]
            root.append(trans)

        static = ET.Element('static')
        ET.SubElement(static, 'duration').text = str(staticSecond)
        ET.SubElement(static, 'file').text = picList[i]
        root.append(static)

        if i == len(picList) - 1:
            trans = ET.Element('transition')
            ET.SubElement(trans, 'duration').text = str(transSecond)
            ET.SubElement(trans, 'from').text = picList[i]
            ET.SubElement(trans, 'to').text = picList[0]
            root.append(trans)

    tree = ET.ElementTree(root)
    ET.indent(tree, space="  ", level=0)

    with open(output, 'wb') as file:
        tree.write(file)

def arg_parse():
    parser = argparse.ArgumentParser(description='XML generate for Ubuntu wallpaper slideshow')
    parser.add_argument('-p', '--path', dest='path', required=True, help='Path of pictures floder')
    parser.add_argument('-o', '--output', dest='output', default='wallpaper-slideshow.xml', help='Output XML file name')
    parser.add_argument('-r', '--random', action='store_true', help='Shuffle the picture list randomly')
    parser.add_argument('--transition', type=float, default=1.0, help='Transition time between two pictures (default 1.0 second)')
    parser.add_argument('--static', type=float, default=599.0, help='Static time that one picture is shown (default 599.0 second)')

    return parser.parse_args()

def main():
    args = arg_parse()

    picList = getPictureList(picPath=args.path, rand=args.random)
    generateXML(picList, args.static, args.transition, args.output)

if __name__ == "__main__":
    main()
