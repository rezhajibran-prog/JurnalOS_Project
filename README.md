# JurnalOS 2026.1

Sistem operasi kustom berbasis Linux Mint 22 Xfce 64-bit (basis Ubuntu Noble) yang di-remaster menggunakan Cubic untuk kebutuhan produktivitas akademik, penulisan ilmiah, dan manajemen referensi.

## Struktur Repository

- `scripts/` — Skrip kustomisasi desktop, plank, mode fokus, welcome app, dan aplikasi logbook (`jurnalos-logbook`, `jurnalos-focus-toggle`, `jurnalos-apply-desktop-rc.sh`, `jurnalos-plank-start`, `jurnalos-welcome.py`).
- `config/` — Konfigurasi remastering Cubic (`cubic.conf`), panel Xfce (`jurnalos-panel.xml`), tata letak ikon desktop (`icons.screen0-1264x735.rc`), dan stylesheet tema logbook (`white-theme.css`).
- `autostart/` — Konfigurasi autostart saat sesi login (`jurnalos-desktop-rc.desktop`, `jurnalos-welcome.desktop`, `plank.desktop`).
- `desktop/` — Desktop entry / shortcut aplikasi (`jurnalos-logbook.desktop`, `jurnalos-focus-mode.desktop`, `jurnalos-pandoc-latex.desktop`).
- `assets/` — Aset visual dan branding (`jurnalos-installer.png`, `jurnalos-menu.png`, `jurnalos-focus-on.png`, `jurnalos-focus-off.png`).
- `docs/` — Dokumentasi panduan penggunaan (`guidebook.html`).

## Distribusi ISO & Verifikasi Checksum

File citra ISO berukuran besar tidak disimpan langsung di GitHub dan didistribusikan melalui Google Drive:

- **Nama File ISO:** `JurnalOS-final-3.iso`
- **Ukuran File:** 4.45 GB (4,787,159,040 bytes)
- **SHA256 Checksum:** `d630ee78775cec3c403e083447c6a4d75f7c6e29109a4e2fdcc89536878ffc3c`
- **Tautan Google Drive (ISO & .sha256):** https://drive.google.com/file/d/1jkIGMTVgjmWgyRxpBAPp06KNs-jfdEwx/view?usp=sharing
- **Video Demonstrasi:** 

## Cara Verifikasi SHA256 di Windows (PowerShell)

```powershell
Get-FileHash .\JurnalOS-final-3.iso -Algorithm SHA256
