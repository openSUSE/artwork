NAME=upwind
VERSION=12.1
VERSION_NO_DOT=`echo ${VERSION} | sed 's:\.::g'`

all: info openSUSE.tar.gz

info:
	echo "Make sure to have php and GraphicsMagick installed"

openSUSE.tar.gz: openSUSE.d
	tar cvfz openSUSE.tar.gz openSUSE
#	rm -r openSUSE

openSUSE.d: gfxboot.d bootsplash.d kdelibs.d yast.d wallpaper.d ksplashx.d kde-workspace.d kdm.d gnome.d susegreeter.d

gfxboot.d: defaults
	rm -rf openSUSE/gfxboot
	inkscape -w 800 -e tmp.png gfxboot/startup.svg
	mkdir -p openSUSE/gfxboot/data-boot/
	convert -quality 90 tmp.png openSUSE/gfxboot/data-boot/back.jpg
	inkscape -w 800 -e tmp.png gfxboot/install.svg
	mkdir -p openSUSE/gfxboot/data-install
	convert -quality 90 tmp.png openSUSE/gfxboot/data-install/back.jpg
	inkscape -w 800 -e tmp.png gfxboot/welcome.svg
	convert -quality 90 tmp.png openSUSE/gfxboot/data-install/welcome.jpg
	rm tmp.png

bootsplash.d:
	mkdir -p openSUSE
	rm -rf openSUSE/bootsplash
	rm -rf bs
	mkdir bs
	cp -a bootsplash/create_bootsplash.sh bs
	inkscape -w 200 -e bs/auge_1.png --export-id=Auge_1 -C -j bootsplash/geeko-animation.svg 
	inkscape -w 200 -e bs/auge_2.png --export-id=Auge_2 -C -j bootsplash/geeko-animation.svg
	inkscape -w 200 -e bs/body.png --export-id=Geeko_Body -C -j bootsplash/geeko-animation.svg
	gm composite bs/auge_1.png bs/body.png bs/logo-right.png
	gm composite bs/auge_2.png bs/body.png bs/logo-left.png
	inkscape -w 90 -e bs/logov.png bootsplash/logo-verbose.svg
	mkdir -p bs/output/config
	mkdir -p bs/output/images
	gm convert -comment "id logo delay 1000 deltaprevbg" bs/logo-right.png -comment "id eye1 delay 1000 loop logo deltaprevbg" bs/logo-left.png bs/output/images/logo.mng
	gm convert -colorspace gray -comment "id logov deltabg stop" bs/logov.png bs/output/images/logov.mng
	cd bs ;\
	  sh create_bootsplash.sh ${VERSION} 1440 900 91 169 ;\
	  if true; then \
	  sh create_bootsplash.sh ${VERSION} 640 480 95 43 ;\
	  sh create_bootsplash.sh ${VERSION} 800 600 95 43 ;\
	  sh create_bootsplash.sh ${VERSION} 1024 600 94 169 ;\
	  sh create_bootsplash.sh ${VERSION} 1024 768 94 43 ;\
	  sh create_bootsplash.sh ${VERSION} 1152 768 94 43 ;\
	  sh create_bootsplash.sh ${VERSION} 1152 864 93 43 ;\
	  sh create_bootsplash.sh ${VERSION} 1280 768 93 169 ;\
	  sh create_bootsplash.sh ${VERSION} 1366 768 93 169 ;\
	  sh create_bootsplash.sh ${VERSION} 1280 800 93 169 ;\
	  sh create_bootsplash.sh ${VERSION} 1280 854 93 43 ;\
	  sh create_bootsplash.sh ${VERSION} 1280 960 92 43 ;\
	  sh create_bootsplash.sh ${VERSION} 1280 1024 92 43 ;\
	  sh create_bootsplash.sh ${VERSION} 1400 1050 91 43 ;\
	  sh create_bootsplash.sh ${VERSION} 1600 1024 90 169 ;\
	  sh create_bootsplash.sh ${VERSION} 1600 1200 89 43 ;\
	  sh create_bootsplash.sh ${VERSION} 1600 900 90 169 ;\
	  sh create_bootsplash.sh ${VERSION} 1920 1080 90 169 ;\
	  sh create_bootsplash.sh ${VERSION} 1680 1050 89 169 ;\
	  sh create_bootsplash.sh ${VERSION} 1920 1200 80 169 ;\
	  sh create_bootsplash.sh ${VERSION} 3200 1200 70 169 ;\
	  fi

	mv bs/output openSUSE/bootsplash
	rm -rf bs

kdelibs.d: defaults
	rm -rf openSUSE/kdelibs
	mkdir -p openSUSE/kdelibs
	cp kdelibs/body-background.jpg openSUSE/kdelibs

yast.d:
	rm -rf openSUSE/yast_wizard
	mkdir -p openSUSE
	cp -a yast openSUSE/yast_wizard
	rm -f openSUSE/yast_wizard/*.svg

wallpaper.d: defaults
	rm -rf openSUSE/wallpapers
	mkdir -p openSUSE/wallpapers
	cp wallpapers/default-1600x1200.jpg.desktop openSUSE/wallpapers
	cp wallpapers/default-1920x1200.jpg.desktop openSUSE/wallpapers
	sed "s:@VERSION@:${VERSION}:g;s:@VERSION_NO_DOT@:${VERSION_NO_DOT}:g" wallpapers/openSUSE-1600x1200.jpg.desktop.in > openSUSE/wallpapers/openSUSE${VERSION_NO_DOT}-1600x1200.jpg.desktop
	sed "s:@VERSION@:${VERSION}:g;s:@VERSION_NO_DOT@:${VERSION_NO_DOT}:g" wallpapers/openSUSE-1920x1200.jpg.desktop.in > openSUSE/wallpapers/openSUSE${VERSION_NO_DOT}-1920x1200.jpg.desktop
	cp default-1600x1200.jpg openSUSE/wallpapers/openSUSE${VERSION_NO_DOT}-1600x1200.jpg
	cp default-1920x1200.jpg openSUSE/wallpapers/openSUSE${VERSION_NO_DOT}-1920x1200.jpg
	ln -s openSUSE${VERSION_NO_DOT}-1600x1200.jpg openSUSE/wallpapers/default-1600x1200.jpg
	ln -s openSUSE${VERSION_NO_DOT}-1920x1200.jpg openSUSE/wallpapers/default-1920x1200.jpg
	echo ${NAME} > openSUSE/wallpaper-name

# When changing the commands below, also update the commands in gnome_dynamic
defaults:
	inkscape -e default-1600x1200.png -w 1600 background-43.svg
	convert -quality 95 -geometry 1600x1200 default-1600x1200.png default-1600x1200.jpg
	inkscape -e default-1900.png -w 1920 background-169.svg
	convert -quality 95 -geometry 1920x1200 default-1900.png default-1920x1200.jpg
	rm default-1900.png default-1600x1200.png 

ksplashx.d: defaults
	rm -rf openSUSE/ksplashx
	mkdir -p openSUSE/ksplashx
	sed "s:@VERSION@:${VERSION}:g" ksplashx/Theme.rc.in > openSUSE/ksplashx/Theme.rc
	cp -a ksplashx/1600x1200 openSUSE/ksplashx/
	inkscape -w 260 --export-id=Geeko -C -j -e openSUSE/ksplashx/1600x1200/opensuse-logo.png logo.svg
	convert -quality 90 -geometry 300x250 default-1600x1200.jpg openSUSE/ksplashx/Preview.png

kde-workspace.d: defaults
	rm -rf openSUSE/kde-workspace
	mkdir -p openSUSE/kde-workspace
	cp -p kde-workspace/*.desktop openSUSE/kde-workspace/
	convert -quality 90 -geometry 400x250 default-1920x1200.jpg openSUSE/kde-workspace/screenshot.jpg

kdm.d: defaults
	rm -rf openSUSE/kdm
	mkdir -p openSUSE/kdm/themes
	cp -a kdm openSUSE/kdm/themes/SUSE
	cp logo.svg openSUSE/kdm/themes/SUSE
	mv openSUSE/kdm/themes/SUSE/pics openSUSE/kdm/

# Create images used for the dynamic wallpaper; note that we do the same as in the 'defaults' target
gnome_dynamic: defaults
	rm -rf gnome/dynamic
	mkdir -p gnome/dynamic
	for file in morning night; do \
		inkscape -e gnome/$${file}-1600x1200.png -w 1600 gnome/$${file}43.svg ; \
		convert -quality 95 -geometry 1600x1200 gnome/$${file}-1600x1200.png gnome/dynamic/$${file}-1600x1200.jpg ; \
		inkscape -e gnome/$${file}-1920x1200.png -w 1920 gnome/$${file}169.svg ; \
		convert -quality 95 -geometry 1920x1200 gnome/$${file}-1920x1200.png gnome/dynamic/$${file}-1920x1200.jpg ; \
		rm gnome/$${file}-1600x1200.png gnome/$${file}-1920x1200.png ; \
	done
	cp default-1600x1200.jpg gnome/dynamic/day-1600x1200.jpg
	cp default-1920x1200.jpg gnome/dynamic/day-1920x1200.jpg
	sed "s:@PATH_TO_IMAGES@:/usr/share/backgrounds/${NAME}:g" gnome/dynamic-wallpaper.xml.in > gnome/dynamic/${NAME}.xml
	sed "s:@PATH_TO_IMAGES@:`pwd`/gnome/dynamic:g" gnome/dynamic-wallpaper.xml.in > gnome/dynamic-wallpaper-localtest.xml
	sed "s:@PATH_TO_IMAGES@:`pwd`/gnome/dynamic:g;s:7200:6:g;s:14400:12:g;s:18000:15:g;s:25200:21:g" gnome/dynamic-wallpaper.xml.in > gnome/dynamic-wallpaper-localtest-fast.xml

gnome.d: gnome_dynamic
	rm -rf openSUSE/gnome
	mkdir -p openSUSE/gnome
	sed "s:@VERSION@:${VERSION}:g;s:@GNOME_STATIC_DYNAMIC@:static:g" gnome/wallpaper-branding-openSUSE.xml.in > openSUSE/gnome/wallpaper-branding-openSUSE.xml
	sed "s:@VERSION_NO_DOT@:${VERSION_NO_DOT}:g" gnome/openSUSE-default-static.xml.in > openSUSE/gnome/openSUSE-default-static.xml
	sed "s:@VERSION@:${VERSION}:g;s:@GNOME_STATIC_DYNAMIC@:dynamic:g" gnome/wallpaper-branding-openSUSE.xml.in > openSUSE/gnome/dynamic-wallpaper-branding-openSUSE.xml
	cp -a gnome/dynamic/ openSUSE/gnome/${NAME}

susegreeter.d:
	rm -rf openSUSE/SUSEgreeter
	mkdir -p openSUSE/SUSEgreeter
	inkscape -w 800 -e openSUSE/SUSEgreeter/background.png kde-workspace/SUSEgreeter/background.svg

