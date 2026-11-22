# JurnalOS 2026.1

Sistem operasi kustom berbasis **Linux Mint 22 Xfce 64-bit** (basis Ubuntu Noble) yang di-remaster menggunakan **Cubic** untuk kebutuhan produktivitas akademik, penulisan ilmiah, dan manajemen referensi.

## Struktur Repository
- `scripts/` — Skrip kustomisasi desktop, *plank*, *mode fokus*, dan *welcome app*.
- `config/` — Konfigurasi remastering Cubic (`cubic.conf`), panel Xfce (`jurnalos-panel.xml`), dan tata letak ikon desktop (`icons.screen0-1264x735.rc`).
- `autostart/` — Konfigurasi *autostart* saat sesi login (`jurnalos-desktop-rc.desktop`, `jurnalos-welcome.desktop`, `plank.desktop`).
- `desktop/` — *Desktop entry* / shortcut aplikasi (`jurnalos-focus-mode.desktop`, `jurnalos-guidebook.desktop`, `jurnalos-pandoc-latex.desktop`).
- `assets/` — Aset visual dan *branding* (`jurnalos-installer.png`, `jurnalos-menu.png`, `jurnalos-focus-on.png`, `jurnalos-focus-off.png`).
- `docs/` — Dokumentasi panduan penggunaan (`guidebook.html`).

## Distribusi ISO & Verifikasi Checksum
File citra ISO berukuran besar tidak disimpan langsung di GitHub dan didistribusikan melalui Google Drive:
- **Nama File ISO**: `JurnalOS-final.iso`
- **Ukuran File**: `4.5 GB` (`4.5G`)
- **SHA256 Checksum**: `4653c4d6476794209b17022145ffaec315d2976fefdfd28639cc2067e89cef56`
- **Tautan Google Drive (ISO & `.sha256`)**: `https://drive.google.com/drive/folders/1D_mP33o_SD-_wqtRkx_GY8HXJM0FcQeO`
- **Video Demonstrasi**: `https://youtu.be/DrDuMT9Sas8?si=Jb51hSeKBSgl5zie`

### Cara Verifikasi SHA256 di Windows (PowerShell)
```powershell
Get-FileHash .\JurnalOS-final.iso -Algorithm SHA256
