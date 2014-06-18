#!/usr/bin/python

import sys, os, json, urllib, urllib2


def get_albums_data(token):
    response = urllib2.urlopen('https://graph.facebook.com/me/albums?access_token='+token)
    html = response.read()
    d = json.loads(html)
    return d['data']

def get_pic_data(token, album_id):
    response = urllib2.urlopen('https://graph.facebook.com/'+album_id+'/photos?access_token='+token)
    html = response.read()
    d = json.loads(html)
    return d['data']

    

def main():
    auth_token = sys.argv[1]
    save_dir = sys.argv[2]
    album_data = get_albums_data(auth_token)
    for album in album_data:
        folder = os.path.join(save_dir, album['name'])
        if not os.path.exists(folder):
            os.makedirs(folder)
        pic_data = get_pic_data(auth_token, album['id'])
        print "Downloading "+album['name']+" to "+folder
        for pic in pic_data:
            image = urllib.urlretrieve(pic['source'], folder+"/"+pic['id'])
    


if __name__ == "__main__":
    main()


