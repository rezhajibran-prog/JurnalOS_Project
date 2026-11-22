#!/bin/bash
CONF_DIR="$HOME/.config/xfce4/desktop"
SRC_RC="/etc/skel/.config/xfce4/desktop/icons.screen0-1264x735.rc"
mkdir -p "$CONF_DIR"

if [ -f "$SRC_RC" ]; then
  sed "s|/home/mahasiswa|$HOME|g" "$SRC_RC" > "$CONF_DIR/icons.screen0-1264x735.rc"
  ln -sf "$CONF_DIR/icons.screen0-1264x735.rc" "$CONF_DIR/icons.screen.latest.rc"
fi
