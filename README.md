# Seabird-Scientific Digital Sensor Workbench - End User Help

This guide explains how to operate the app as a bench/tooling user.

## What This Tool Does

Seabird-Scientific Digital Sensor Workbench combines:
- COM port connection management
- Automated unit test runs
- Live plotting during acquisition
- Per-port serial debug consoles
- Session result review and export

Use it when you need to connect one or more instruments, run repeatable sample-based tests, and inspect results quickly.

## Basic Workflow (Quick Start)

1. Connect sensors/devices and open the app.
2. In Connection, choose port/baud and connect ports.
3. In Test Setup, confirm Operator and setup fields.
4. In Actions, run `Run Unit Test (all connected)`.
5. Watch Live Plot and Run Log while the run executes.
6. Review results in Test Results and export if needed.

## Connection Panel Buttons

- `Refresh Ports`: Rescan available COM ports.
- `Connect Selected`: Connect only the currently selected COM port.
- `Reconnect @ Baud`: Disconnect and reconnect selected port using current baud.
- `Disconnect Selected`: Disconnect the selected COM port.
- `Connect All`: Connect all detected ports (up to app limit).
- `Disconnect All`: Disconnect every connected port.
- `Hide/Show Port Station View`: Collapse/expand the card view of connected ports.
- `About`: Opens this help file in your browser.

## Test Setup Fields

- `Operator`: Required before test run can start.
- `Bath ID`: Optional identifier for current setup.
- `Notes`: Optional run/session note.
- `Bath Temp (C)`: Optional setup metadata.
- `Salinity (PSU)`: Read-only in this workflow.
- `Samples`: Number of samples per run.
- `Results Root` + `Browse`: Folder root where session/unit outputs are written.

## Actions Panel Buttons

- `Run Unit Test (all connected)`: Starts parallel run on all currently connected ports.
- `Save Session JSON`: Writes current session rows to a JSON file.
- `Reset Session`: Clears current table/session and starts a new session.
- `Show Plot`: Switches to Live Plot tab.
- `Show Console`: Switches to Serial Consoles tab.
- `Detach Console`: Pops console tab into separate window.
- `Plot Session`: Plots current session summary data.
- `Load Session Plot`: Load a prior session and plot it.
- `Reload Current Session JSON`: Reload current session JSON for plotting.
- `Toggle CSV Column`: Show/hide sample CSV path column in results grid.
- `Dark Mode`: Toggle dark/light theme.

## Test Results Tab

- Table columns include timestamp, port, serial, noise, voltage statistics, flags, and raw sample CSV path.
- Click a column header to sort ascending/descending.
- Use `Toggle CSV Column` to include/exclude raw sample path visibility.

## Live Plot Tab

### Generic Sample Format Area
- Used to define parser behavior for incoming sample lines.
- You can map fields, descriptions, units, scaling, derived expressions, and plotting inclusion.

### Current Run Live View Controls
- `Plot field`: Select which measureand to graph live.
- `Refresh Plot`: Redraw using latest data/control settings.
- `Auto Y`: Automatic y-axis scaling.
- `Ymin`, `Ymax`: Manual axis limits when Auto Y is off.
- `Points`: Toggle points overlay.
- `Visible Ports`: Choose which connected ports appear on plot.
- `X Start`, `X End`: Restrict sample index range shown.
- `Std Dev`, `Samples`: Quick indicators for current plotted stream.

## Serial Consoles Tab

Each port has its own console tab for manual TX/RX interaction.

- `Send`: Sends typed command to selected port.
- `Read`: Performs short read window and prints responses.
- `Stream`: Continuously read/display incoming lines.
- `Clear Selected Debug Tab`: Clears active debug output.
- `Export Console CSV`: Saves captured TX/RX console rows.
- `CR` / `LF`: Include carriage return / line feed on transmitted command.
- Display mode: `ASCII`, `HEX`, `DEC`, `BIN`.

## Port Station View (Card Grid)

Each connected port card shows:
- Slot number
- Port name
- Current serial number
- Current status badge (`CONNECTED`, `RUNNING`, `PASS`, etc.)

## Output Files

Under your Results Root, the app writes session and per-unit artifacts (CSV/JSON/log files).  
Use these for traceability, quick comparisons, and offline review.

## Plotting Examples

### Example 1: Check stability on Red Phase
1. Open Live Plot.
2. Set `Plot field` to `Red Phase`.
3. Enable `Auto Y`.
4. Start a run.
5. Watch `Std Dev` value settle; unstable units usually show larger spread and noisier trend.

### Example 2: Compare only two ports
1. In Live Plot, click `Visible Ports`.
2. Keep only two ports checked.
3. Set `Plot field` to `Blue Voltage` (or relevant field).
4. Use `X Start`/`X End` to zoom on transient sections.

### Example 3: Manual Y limits for subtle drift
1. Disable `Auto Y`.
2. Enter narrow `Ymin`/`Ymax` bounds around expected nominal.
3. Click `Refresh Plot`.
4. Small drift becomes visible that auto scaling might hide.

## Common Issues

- Run button disabled:
  - Ensure at least one port is connected.
  - Ensure `Operator` is filled.
  - Ensure no run is currently active.

- No live updates:
  - Confirm selected field exists in parser mapping.
  - Confirm port is connected and actively streaming samples.

- Console command shows no response:
  - Verify CR/LF settings expected by device.
  - Try `Read` after `Send`.
  - Check baud rate and connection health.

## Notes

- This tool helps accelerate diagnosis and bench workflows.
- It is not a replacement for formal production QA/calibration systems.

