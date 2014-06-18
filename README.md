facebook_album_downloader
=========================

Bash script that downloads all Facebook albums uploaded

Requires python 2.7

To Use:

  Go to https://developers.facebook.com/tools/explorer and get an access token. Place access token in a regular file called
  AUTH_TOKEN in the same directory as download.sh and helper.py. 
  Be sure to enable user_photos permissions when requesting an access token
  <pre><code>echo "{access_token}" > "AUTH_TOKEN"</code></pre>
  Run in terminal
  <pre><code>./download.sh "download_directory"</code></pre>
  If download directory is unspecified, script will create a photos directory in the same directory as download.sh
  
  
  
