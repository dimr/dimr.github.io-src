Title: Debian snapshot repository cli tool
Date: 2016-05-18 04:47:56
Tags: debian, linux, debsnapshot,python
Summary: debsnapshot repository command line tool
slug: debsnap-cli
status: published

[Debian snapshot repository](http://snapshot.debian.org/) is
> is a wayback machine that allows access to old packages based on dates and version numbers. It consists of all past and current packages the Debian archive provides.

As a tarting point for creating this package was that some times xserver transitions were not compatible with the current nvidia proprietary driver, so
when you were upgrading the xserver you had to switch to the nouveau driver. The result was black screen and you either, had to edit xorg.conf and choose
the open source driver or downgrade the nvidi-driver. Since i prefer to use the second one i had to downgrade but there where times that it was
removed from the official repository. This is where the debian snapshot repository comes in handy but in a situation like this with no gui environment
you have to go to another computer, search the package, copy the timestamp that your package was first seen in the repository and manually write
the url to your sources.list file, plus write down how you should update your package cache and ignore the Valid-Until header within the Release files.
So, you need to write some like this

> deb http://snapshot.debian.org/archive/debian/20131221T035435Z unstable main contrib non-free

and then update the package cache either with apt-get

> apt-get -o Acquire::Check-Valid-Until=false update

or with aptitude

> aptitude -o Acquire::Check-Valid-Until=false update

The first thing that came in mind was that i should search for a program that does all this work for me. To my suprise **there is no such thing**.
The closest you can find that interacts with the snapshot server is a program called debsnap that you can find it in the [devscripts](https://packages.debian.org/sid/devscripts) package

All these happened while using the debian testing branch for about 3.5 years. At some point, i switched to unstable with the [Siduction](http://news.siduction.org/) distro, which is by the way a great choice, and in general you have to be more careful with your upgrades, be careful with upgrading packages, be **more** careful with dist-upgrading packages, **holding** packages -patience is a virtue in unstable-, reading changelogs and eventually downgrading packages.

[debsnap-cli](https://github.com/dimr/debsnapshot-cli) gives you this extra functionality that extends the available package versions that you can install.
I personally use it a lot :). The last time i used it was when the [gtk 3.20 entered the unstable branch ](https://igurublog.wordpress.com/2016/04/20/heads-up-gtk-3-20-off-to-a-troubled-start/) and messed up some programs (pavucontrol, file-roller, kazam, gedit) including firefox.

I just queried the snapshot server for firefox with

> debsnap-cli -first-seen -arch amd64 45.0.2-1  firefox

it found the relevant timestamp, created the url and appended to a snapshot.list file that it creates inside the /etc/apt/sources.list.d/ path

> http://snapshot.debian.org/archive/debian/20160413T160058Z

see the full documentation on the github page for instructions on how to use it.

<!-- Final note. Building packages in python should be easier, there are way to many resources on line that can give you a clue on how to  -->
<!-- start but in the end you are going to spend a lot of time in a   -->
