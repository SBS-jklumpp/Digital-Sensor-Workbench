## SBS DSW Update Server

This folder provides a simple HTTP update server and publisher for `sbs_dsw.exe`.

### 1) Publish an update payload

From repo root:

```powershell
python .\tools\update_server\publish_update.py --exe .\dist\sbs_dsw.exe --version 1.3.0 --notes "Bug fixes"
```

If your build output path is different, pass that file path to `--exe` (for example `.\dist\.exe`).

This writes:

- `tools/update_server/public/sbs_dsw.exe`
- `tools/update_server/public/manifest.json`

### 2) Start the web server

```powershell
python .\tools\update_server\serve_updates.py --host 0.0.0.0 --port 8080
```

Feed URL for clients:

- `http://<your-server-ip>:8080/manifest.json`

Health endpoint:

- `http://<your-server-ip>:8080/healthz`

### 3) Point the app to your feed

In `sbs_dsw.exe`:

- click `Update Feed URL`
- set `http://<your-server-ip>:8080/manifest.json`
- click `Check Update`
