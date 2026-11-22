#!/usr/bin/env python3
import subprocess
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Pango


class JurnalOSWelcome(Gtk.Window):

  def __init__(self):
    super().__init__(title="Selamat Datang di JurnalOS")
    self.set_default_size(500, 360)
    self.set_position(Gtk.WindowPosition.CENTER)
    self.set_resizable(False)
    self.set_border_width(24)

    # Kontainer Utama
    vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=16)
    self.add(vbox)

    # Judul Utama
    title_label = Gtk.Label()
    title_label.set_markup(
        "<span size='xx-large' weight='bold'>Welcome to JurnalOS</span>"
    )
    vbox.pack_start(title_label, False, False, 0)

    # Subjudul / Deskripsi
    desc_label = Gtk.Label(
        label=(
            "JurnalOS 22.1 (Academic Edition)\nLingkungan kerja siap pakai"
            " untuk perkuliahan, riset, dan penulisan karya ilmiah."
        )
    )
    desc_label.set_justify(Gtk.Justification.CENTER)
    desc_label.set_line_wrap(True)
    vbox.pack_start(desc_label, False, False, 0)

    # Garis Pemisah
    vbox.pack_start(Gtk.Separator(), False, False, 4)

    # Label Akses Cepat
    quick_label = Gtk.Label()
    quick_label.set_markup("<b>Akses Cepat Perangkat Akademik:</b>")
    vbox.pack_start(quick_label, False, False, 0)

    # Tombol Peluncur Aplikasi
    btn_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    btn_box.set_homogeneous(True)
    vbox.pack_start(btn_box, False, False, 4)

    apps = [
        ("Buka Zotero", "zotero"),
        ("Buka Obsidian", "obsidian"),
        ("LibreOffice Writer", "libreoffice --writer"),
    ]

    for label, cmd in apps:
      btn = Gtk.Button(label=label)
      btn.connect("clicked", self.launch_app, cmd)
      btn_box.pack_start(btn, True, True, 0)

    # Tombol Tutup / Mulai
    close_btn = Gtk.Button(label="Mulai Menggunakan Desktop")
    close_btn.get_style_context().add_class("suggested-action")
    close_btn.connect("clicked", Gtk.main_quit)
    vbox.pack_end(close_btn, False, False, 0)

  def launch_app(self, widget, command):
    subprocess.Popen(command.split())


if __name__ == "__main__":
  win = JurnalOSWelcome()
  win.connect("destroy", Gtk.main_quit)
  win.show_all()
  Gtk.main()
