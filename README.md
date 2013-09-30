sc-findusers
============

A command line tool used to find the SnapChat usernames for known or unknown phone numbers

## Usage
============

>$ python sc-findusers.py username password number1,number2
>
>success: found 2 results:
>	number: number1
>	username: number1s_username
>
>	number: number2
>	username: number2s_username


## Prerequisites
============

The following python libraries are required:

* requests
* hashlib
* simplejson

## Credits
============

Thanks a lot to the following people and their resources, a majority of the work was already done by them

* [Thomas Lackner](https://github.com/tlack/snaphax)
* [Adam Caudill](http://adamcaudill.com/2012/06/16/snapchat-api-and-security/)
* [kivikakk](https://kivikakk.ee/2013/05/10/snapchat.html)

## Tools Used
============

I used a few different tools to figure out what needed to be sent to the snapchat server, would have been much more difficult without them.

* [APK  dissasembler](http://code.google.com/p/easy-apk-dissassembler/)
* [android-apktool](https://code.google.com/p/android-apktool/)
* ettercap



