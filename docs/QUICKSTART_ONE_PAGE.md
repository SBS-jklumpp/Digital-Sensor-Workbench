<![CDATA[# ⚡ SBS DSW Quickstart Guide

> **One-page reference for fast bench runs**

---

## 🎯 Fast Path (60 Seconds)

```
1. Launch           →  sbs_dsw.exe
2. Refresh          →  Click "Refresh" button
3. Connect          →  Select port + baud → "▶ Connect"
4. Setup            →  Enter Operator name, set Samples ≥ 20
5. Run              →  Click "▶ Run Test"
6. Monitor          →  Watch Live Plot (auto-opens)
7. Review           →  Check Results tab (auto-switches when done)
8. Save             →  Click "Save"
```

---

## 📋 Step-by-Step Checklist

### Step 1: Connect

| Action | Control |
|--------|---------|
| Scan ports | Click **Refresh** |
| Select COM port | Use dropdown |
| Set baud rate | Use dropdown (typically 9600 or 115200) |
| Connect | Click **▶ Connect** |

✅ **Success:** Port shows in connected list, status badge shows "CONNECTED"

### Step 2: Configure

| Field | Value |
|-------|-------|
| **Operator** | Your name (required) |
| **Samples** | 20 or more (required) |
| **Results Root** | Output folder (auto-set) |

Optional: Bath ID, Notes, Bath Temp, Salinity

### Step 3: Run Test

| Action | Result |
|--------|--------|
| Click **▶ Run Test** | Panels auto-collapse, Live Plot opens |
| Watch progress | Real-time plotting during run |
| Wait for complete | Auto-switches to Results tab |

### Step 4: Review Results

Check these columns in the Results table:

| Column | What to Look For |
|--------|------------------|
| **red_ns** | Noise ≤ 10 ns = PASS |
| **blue_ns** | Noise ≤ 10 ns = PASS |
| **flags** | Should be empty for good runs |
| **severity** | PASS / WARN / FAIL |

### Step 5: Save

| Action | Control |
|--------|---------|
| Save session | Click **Save** |
| Export console | Use Console tab → Export |

---

## 🚦 Pass/Warn/Fail Rules

| Result | Criteria |
|--------|----------|
| **PASS** | Red AND Blue noise ≤ 10 ns |
| **WARN** | Either noise > 10 ns AND ≤ 20 ns |
| **FAIL** | Either noise > 20 ns |

---

## 🆕 v1.4.0 Quick Tips

| Feature | How to Use |
|---------|-----------|
| **Max View** | Click "□ Max View" to collapse all panels |
| **Auto Layout** | Panels auto-hide when test starts |
| **Sniffer** | Use Sniffer tab to view raw serial data |
| **Bridge Mode** | Intercept external app traffic via com0com |

---

## 🔧 If Blocked

| Problem | Solution |
|---------|----------|
| "Run Test" disabled | Connect a port AND fill Operator field |
| No samples collected | Check baud rate and Sample Cmd |
| Plot looks wrong | Verify parser delimiter and field config |
| Console no response | Toggle CR/LF, click Read after Send |

---

## ⌨️ Quick Commands

**Run packaged app:**
```powershell
.\sbs_dsw.exe
```

**Run from source:**
```powershell
cd src
python -m engineers_field_kit_multitool.app
```

---

## 🔗 More Help

- **Full Documentation:** See [README.md](../README.md)
- **In-App Help:** Click "Help" in header bar
- **Serial Sniffer:** See [Sniffer Guide](../README.md#-serial-port-sniffer)
- **Parser Setup:** See [Parser Config](../README.md#-sample-parser-configuration)

---

<div align="center">

*SBS DSW v1.4.0 — Quick Reference*

</div>
]]>
