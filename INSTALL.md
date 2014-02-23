# RTL-SDR

## Tools to install
* LinuxTV Media drivers (optional but recommended)
* RTL-SDR Osmocom library
* Dump1090

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
```bash
    INCLUDE_EXTRA_DVB := include-300 # kernel 3.0.0 / 3.1.0
```
Or:
```bash
    INCLUDE_EXTRA_DVB := include-320 # kernel 3.2.0
```
Do some magic. It's a kernel module, you can't install it without root privileges.
```bash
    make
    sudo make install
```

* Clone `git://git.osmocom.org/rtl-sdr.git`
```bash
    export RTLSRD_HOME="Define the path here"
    cd rtl-sdr
    git checkout tags/v0.5.2 # Versions >0.5.2 don't work!!!!!!!
    libtoolize
    autoreconf -fiv
    ./configure --prefix=$RTLSDR_HOME # If you use /opt I will find you and I will kill you.
    make
    make install # You might need root privileges if you install it into some dangerous directory.
```
* Give non-root permisions to the pincho. There's a lot of ways to do that, but I don't trust
3rd party rules. The easiest way is `make install-udev-rules`, the best way is:
```bash
    lsusb
```
Get the `idVendor` and `idProduct` numbers. The pincho is called `Realtek Semiconductor 
Corp. RTL2838 DVB-T` with `idVendor = 0bda` and `idProduct = 2838` but remember this
could be different for each pincho. And as superuser:
```bash
    echo 'SUBSYSTEMS=="usb", ATTRS{idVendor}=="0bda", ATTRS{idProduct}=="2838", MODE:="0666"' > /etc/udev/rules.d/pincho.rules
    service udev restart
    ls -l /dev/
```
* Disable default drivers for the pincho. I don't want to remove permanently the drivers since I want
to use it for watching DVB-T and listening FM radio. As superuser:
```bash
    modprobe -r dvb_usb_rtl28xxu
    modprobe -r rtl2830
    modprobe -r rtl2832
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
    $RTLSDR_HOME/bin/rtl_test
```

* Download or clone `https://github.com/antirez/dump1090.git`
```bash
    PKG_CONFIG_PATH="$PKG_CONFIG_PATH:$RTLSDR_HOME/lib/pkconfig" make
```
* Add the librtlsdr path to `LD_LIBRARY_PATH`:
```bash
    export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:$RTLSDR_HOME/lib"
```
* Time to enjoy:
```bash
    ./dump1090 --interactive --net
```
* And that's your [reward](http://www.youtube.com/watch?v=-YCN-a0NsNk).

