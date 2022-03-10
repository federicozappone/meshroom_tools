#!/usr/bin/env bash

wget https://www.fosshub.com/Meshroom.html?dwl=Meshroom-2021.1.0-linux-cuda10.tar.gz
tar -zxvf Meshroom-2021.1.0-linux-cuda10.tar.gz --one-top-level=meshroom --strip-components 1
ln -s meshroom/Meshroom Meshroom
rm Meshroom-2021.1.0-linux-cuda10.tar.gz