#!/bin/bash

clear
figlet Installer
figlet Kuhaku Tools

sleep 2

chmod +x uninstall

if [ "$PREFIX" = "/data/data/com.termux/files/usr" ]; then
    INSTALL_DIR="$PREFIX/usr/share/doc/Kuhaku"
    BIN_DIR="$PREFIX/bin/"
    BASH_PATH="$PREFIX/bin/bash"
    TERMUX=true

    pkg install -y git python2
elif [ "$(uname)" = "Darwin" ]; then
    INSTALL_DIR="/usr/local/Kuhaku"
    BIN_DIR="/usr/local/bin/"
    BASH_PATH="/bin/bash"
    TERMUX=false
else
    INSTALL_DIR="$HOME/.Kuhaku"
    BIN_DIR="/usr/local/bin/"
    BASH_PATH="/bin/bash"
    TERMUX=false

    apt-get install -y git python2.7
fi

echo "[✔] Memeriksa Directory...";
if [ -d "$INSTALL_DIR" ]; then
    echo "[◉] Di Directory Nya Sudah Terinstall Tools Ini Apakah Anda Ingin Install Ulang ? Y/N" ;
    read -r mama
    if [ "$mama" = "y" ]; then
        if [ "$TERMUX" = true ]; then
            rm -rf "$INSTALL_DIR"
            rm  " $ BIN_DIR / Kuhaku *"
        else
            sudo rm -rf "$INSTALL_DIR"
            sudo rm "$BIN_DIR/Kuhaku*"
        fi
    else
        echo "[✘] Hapus Tools Di Directory usr/share/doc/ Untuk Melanjutkan Installasi [✘] ";
        echo "[✘] Installasi Gagal! [✘] ";
        exit
    fi
fi
echo "[✔] Membersihkan File Di Directory Sebelummnya...";
if [ -d "$ETC_DIR/Kuhaku" ]; then
    echo "$DIR_FOUND_TEXT"
    if [ "$TERMUX" = true ]; then
        rm -rf "$ETC_DIR/Kuhaku"
    else
        sudo rm -rf "$ETC_DIR/Kuhaku"
    fi
fi

echo "[✔] Menginstall ...";
echo "";
git clone --depth=1 https://github.com/The-X-Team-Debug/kuhaku_tools "$INSTALL_DIR";
echo "#!$BASH_PATH
python $INSTALL_DIR/kuhaku.py" "${1+"$@"}" > "$INSTALL_DIR/fsociety";
chmod +x "$INSTALL_DIR/Kuhaku";
if [ "$TERMUX" = true ]; then
    cp "$INSTALL_DIR/kuhaku_tools" "$BIN_DIR"
    cp "$INSTALL_DIR/kuhaku.cfg" "$BIN_DIR"
else
    sudo cp "$INSTALL_DIR/Kuhaku" "$BIN_DIR"
    sudo cp "$INSTALL_DIR/kuhaku.cfg" "$BIN_DIR"
fi
rm "$INSTALL_DIR/Kuhaku";


if [ -d "$INSTALL_DIR" ] ;
then
    echo "";
    echo "[✔] Tools Berhasil Di Install [✔]";
    echo "";
    echo "[✔]====================================================================[✔]";
    echo "[✔]      Enjoy, Bro Menggunakan Tools Ini {{ The X Team }} !!       [✔]";
    echo "[✔]====================================================================[✔]";
    echo "";
else
    echo "[✘] Installasi Gagal Periksa Jaringan Internet [✘] ";
    exit
fi
