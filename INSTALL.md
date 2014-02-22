# RTL-SDR

## Debian (and Ubuntu)

* Be sure you have installed: 
    * `pkg-config`
    * `build-essentials`
    * `autoconf`
    * `libusb-1.0-0-dev`
    * `autotools-dev`
    * `libtool`
    * `linux-headers-$(uname -r)`
    * `libproc-processtable-perl`
* Those are optional packages:
    * `dvb-apps`
    * `dvb-tools`
    * `patchutils`
    * `w-scan`
* Clone `git://linuxtv.org/media_build.git`
```bash
    cd media<tab>
    ./build
```
Modify `Makefile` according to your system.
```
...
# kernel 3.0.0 / 3.1.0
#INCLUDE_EXTRA_DVB := include-300

# kernel 3.2.0
INCLUDE_EXTRA_DVB := include-320
...
```
Do some magic.
```bash
    make
    sudo make install
    # Sorry guys, it's a kernet module, you can not install without root privileges.
```

* Clone `git://git.osmocom.org/rtl-sdr.git`
```bash
    cd rtl-sdr
    git checkout tags/v0.5.2 # Versions >0.5.2 don't work!!!!!!!
    libtoolize
    autoreconf -fiv
    ./configure --prefix=<Somepath you want> # If you use /opt I will find you and I will kill you.
    make
    make install # You might need root privileges if you install it into some dangerous directory.
```
* Give non-root permisions to the pincho. There's a lot of ways to do that, but I don't trust
3rd party rules. The easiest way is `make install-udev-rules`, the best way is:
```bash
    lsbub
```
Get the `idVendor` and `idProduct` numbers. The pincho is called `Realtek Semiconductor 
Corp. RTL2838 DVB-T` with `idVendor = 0bda` and `idProduct = 2838` but remember this
could be different for each pincho.
```bash
    # Superuser
    echo 'SUBSYSTEMS=="usb", ATTRS{idVendor}=="0bda", ATTRS{idProduct}=="2838", MODE:="0666"' > /etc/udev/rules.d/pincho.rules
    service udev restart
    ls -l /dev/
```
* Disable default drivers for the pincho. I don't want to remove permanently the drivers since I want
to use it for watching DVB-T and listening FM radio.
```bash
    sudo modprobe -r dvb_usb_rtl28xxu
    sudo modprobe -r rtl2830
    sudo modprobe -r rtl2832
```
But you're free to do it.
```bash
    (
    cat <<'EOF'
      blacklist dvb_usb_rtl28xxu
      blacklist rtl2830
      blacklist rtl2832
    EOF
    ) > /etc/modprobe.d/blacklist-dvb
```

* Test the pincho:
```bash
    <prefix>/bin/rtl_test
```

* Download or clone `https://github.com/antirez/dump1090.git`
```bash
    PKG_CONFIG_PATH="$PKG_CONFIG_PATH:<prefix>/lib/pkconfig" make
```
* Add the librtlsdr path to `LD_LIBRARY_PATH`:
```bash
    export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:<prefix>/RTLSDR/lib"
```
* Time to enjoy:
```bash
    ./dump1090 --interactive --net
```
* And that's your [reward](http://www.youtube.com/watch?v=-YCN-a0NsNk).

