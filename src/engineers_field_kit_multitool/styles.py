import tkinter as tk
from tkinter import ttk

# ─── DARK PALETTE ────────────────────────────────────────────────────────────
# Deep navy-charcoal surfaces · Electric cyan accent · Crisp amber warn/ok
DARK_BG        = "#080c12"   # deep void background
DARK_PANEL     = "#131b27"   # primary panel surface
DARK_PANEL_2   = "#1d2a3c"   # elevated surface / hover
DARK_PANEL_3   = "#26374f"   # card / treeview row
DARK_BORDER    = "#3d5572"   # subtle borders
DARK_BORDER_HI = "#7ea6d6"   # focused / active borders
DARK_TEXT      = "#e6edf3"   # primary text
DARK_TEXT_SUB  = "#c9d1d9"   # secondary text
DARK_MUTED     = "#7d8d9e"   # muted / disabled
DARK_ACCENT    = "#ff7a1a"   # vivid orange accent (primary CTA)
DARK_ACCENT_DIM= "#d95d04"   # pressed accent
DARK_ACCENT_HI = "#ff9a4d"   # hover accent
DARK_OK        = "#3fb950"   # green pass/ok
DARK_WARN      = "#d29922"   # amber warning
DARK_FAIL      = "#f85149"   # red fail/error
DARK_SEL_BG    = "#3b2b1e"   # treeview selection row

# ─── LIGHT PALETTE ───────────────────────────────────────────────────────────
LIGHT_BG       = "#f6f8fa"
LIGHT_PANEL    = "#ffffff"
LIGHT_PANEL_2  = "#e2ebf5"
LIGHT_BORDER   = "#a9bad0"
LIGHT_BORDER_HI= "#0f62fe"
LIGHT_TEXT     = "#1f2328"
LIGHT_TEXT_SUB = "#444c56"
LIGHT_MUTED    = "#7a8491"
LIGHT_ACCENT   = "#0f62fe"
LIGHT_ACCENT_HI= "#2a76ff"
LIGHT_ACCENT_DIM="#0043ce"
LIGHT_OK       = "#1a7f37"
LIGHT_WARN     = "#9a6700"
LIGHT_FAIL     = "#cf222e"
LIGHT_SEL_BG   = "#dbeafe"

DEFAULT_FONT   = ("Segoe UI", 9)


def apply_theme(root: tk.Tk, field_mode: bool = False, dark_mode: bool = True):
    style = ttk.Style(root)
    try:
        style.theme_use("clam")
    except Exception:
        pass

    if dark_mode:
        bg         = DARK_BG
        panel      = DARK_PANEL
        panel_2    = DARK_PANEL_2
        panel_3    = DARK_PANEL_3
        border     = DARK_BORDER
        border_hi  = DARK_BORDER_HI
        text       = DARK_TEXT
        text_sub   = DARK_TEXT_SUB
        muted      = DARK_MUTED
        accent     = DARK_ACCENT
        accent_hi  = DARK_ACCENT_HI
        accent_dim = DARK_ACCENT_DIM
        ok         = DARK_OK
        warn       = DARK_WARN
        fail       = DARK_FAIL
        sel_bg     = DARK_SEL_BG
        btn_active = "#232e3d"
        btn_pressed= "#1a2535"
        treesel_fg = "#e6edf3"
    else:
        bg         = LIGHT_BG
        panel      = LIGHT_PANEL
        panel_2    = LIGHT_PANEL_2
        panel_3    = LIGHT_PANEL_2
        border     = LIGHT_BORDER
        border_hi  = LIGHT_BORDER_HI
        text       = LIGHT_TEXT
        text_sub   = LIGHT_TEXT_SUB
        muted      = LIGHT_MUTED
        accent     = LIGHT_ACCENT
        accent_hi  = LIGHT_ACCENT_HI
        accent_dim = LIGHT_ACCENT_DIM
        ok         = LIGHT_OK
        warn       = LIGHT_WARN
        fail       = LIGHT_FAIL
        sel_bg     = LIGHT_SEL_BG
        btn_active = "#dae2eb"
        btn_pressed= "#c8d3dd"
        treesel_fg = "#1f2328"

    fsz            = 13 if field_mode else 11
    fsz_sm         = 11 if field_mode else 10
    strong_text    = "#f0f6fc" if (field_mode and dark_mode) else text
    btn_pad        = (7, 3) if field_mode else (5, 2)
    primary_pad    = (8, 3) if field_mode else (6, 2)
    tab_pad        = [20, 10] if field_mode else [16, 8]
    row_h          = 34 if field_mode else 30
    entry_pad      = 6 if field_mode else 4

    root.configure(bg=bg)

    # ── Base defaults ──────────────────────────────────────────────────────
    style.configure(".",
        background=bg,
        foreground=strong_text,
        fieldbackground=panel,
        bordercolor=border,
        borderwidth=1,
        relief="flat",
        font=("Segoe UI", fsz),
        focuscolor=accent,
    )

    # ── Frames ────────────────────────────────────────────────────────────
    style.configure("TFrame", background=bg)
    style.configure("Card.TFrame", background=panel, relief="flat")

    # ── LabelFrame — rendered as crisp section card ────────────────────────
    style.configure("TLabelframe",
        background=bg,
        foreground=text,
        bordercolor=border,
        borderwidth=1,
        relief="flat",
        padding=(8, 6),
    )
    style.configure("TLabelframe.Label",
        background=bg,
        foreground=accent,
        font=("Segoe UI Semibold", fsz_sm),
        padding=(0, 0, 0, 2),
    )

    # ── Labels ────────────────────────────────────────────────────────────
    style.configure("TLabel",
        background=bg,
        foreground=strong_text,
        font=("Segoe UI", fsz),
    )
    style.configure("Muted.TLabel",
        background=bg,
        foreground=muted,
        font=("Segoe UI", fsz_sm),
    )
    style.configure("OK.TLabel",    background=bg, foreground=ok,   font=("Segoe UI Semibold", fsz))
    style.configure("Warn.TLabel",  background=bg, foreground=warn, font=("Segoe UI Semibold", fsz))
    style.configure("Fail.TLabel",  background=bg, foreground=fail, font=("Segoe UI Semibold", fsz))
    style.configure("Accent.TLabel",background=bg, foreground=accent, font=("Segoe UI Semibold", fsz))

    # ── Standard button ───────────────────────────────────────────────────
    style.configure("TButton",
        background=panel_2,
        foreground=strong_text,
        bordercolor=border,
        focuscolor=accent,
        padding=btn_pad,
        relief="flat",
        font=("Segoe UI", fsz_sm),
    )
    style.map("TButton",
        background=[("active", btn_active), ("pressed", btn_pressed), ("disabled", panel)],
        foreground=[("disabled", muted)],
        bordercolor=[("focus", border_hi), ("active", border_hi)],
    )

    # ── Primary (accent-filled) button ────────────────────────────────────
    style.configure("Primary.TButton",
        background=accent,
        foreground="#0d1117" if dark_mode else "#ffffff",
        bordercolor=accent,
        focuscolor=accent_hi,
        padding=primary_pad,
        relief="flat",
        font=("Segoe UI Semibold", fsz_sm),
    )
    style.map("Primary.TButton",
        background=[("active", accent_hi), ("pressed", accent_dim), ("disabled", panel_2)],
        foreground=[("disabled", muted)],
    )

    # ── Danger button ─────────────────────────────────────────────────────
    style.configure("Danger.TButton",
        background=panel_2,
        foreground=fail,
        bordercolor=fail,
        padding=btn_pad,
        relief="flat",
        font=("Segoe UI", fsz),
    )
    style.map("Danger.TButton",
        background=[("active", "#2d1117" if dark_mode else "#fef2f2"),
                    ("pressed", "#3a1520" if dark_mode else "#fee2e2")],
        foreground=[("disabled", muted)],
    )

    # ── Entry ─────────────────────────────────────────────────────────────
    style.configure("TEntry",
        fieldbackground=panel,
        foreground=strong_text,
        bordercolor=border,
        insertcolor=accent,
        selectbackground=sel_bg,
        selectforeground=strong_text,
        padding=entry_pad,
        relief="flat",
    )
    style.map("TEntry",
        bordercolor=[("focus", border_hi), ("hover", border)],
        fieldbackground=[("disabled", panel_2)],
        foreground=[("disabled", muted)],
    )

    # ── Combobox ──────────────────────────────────────────────────────────
    style.configure("TCombobox",
        fieldbackground=panel,
        background=panel_2,
        foreground=strong_text,
        bordercolor=border,
        arrowcolor=muted,
        padding=entry_pad - 1,
        relief="flat",
    )
    style.map("TCombobox",
        fieldbackground=[("readonly", panel), ("active", panel)],
        foreground=[("readonly", strong_text), ("disabled", muted)],
        arrowcolor=[("active", accent), ("hover", accent)],
        bordercolor=[("focus", border_hi)],
    )

    # ── Spinbox ───────────────────────────────────────────────────────────
    style.configure("TSpinbox",
        fieldbackground=panel,
        foreground=strong_text,
        bordercolor=border,
        arrowcolor=muted,
        insertcolor=accent,
        padding=entry_pad - 1,
        relief="flat",
    )
    style.map("TSpinbox",
        arrowcolor=[("active", accent)],
        bordercolor=[("focus", border_hi)],
    )

    # ── Checkbutton ───────────────────────────────────────────────────────
    style.configure("TCheckbutton",
        background=bg,
        foreground=strong_text,
        focuscolor=accent,
        padding=(2, 2),
        indicatorcolor=panel_3 if dark_mode else LIGHT_PANEL,
        indicatormargin=(0, 0, 6, 0),
    )
    style.map("TCheckbutton",
        background=[("active", bg)],
        foreground=[("active", strong_text), ("disabled", muted)],
        indicatorcolor=[("selected", accent), ("active", accent_hi if dark_mode else accent_hi)],
    )

    # ── Radiobutton ───────────────────────────────────────────────────────
    style.configure("TRadiobutton",
        background=bg,
        foreground=strong_text,
        focuscolor=accent,
        padding=(2, 2),
    )
    style.map("TRadiobutton",
        background=[("active", bg)],
        foreground=[("active", strong_text), ("disabled", muted)],
        indicatorcolor=[("selected", accent)],
    )

    # ── Notebook tabs ─────────────────────────────────────────────────────
    style.configure("TNotebook",
        background=bg,
        bordercolor=border,
        tabmargins=[6, 8, 6, 0],
    )
    style.configure("TNotebook.Tab",
        background=panel_2,
        foreground=muted,
        padding=tab_pad,
        bordercolor=border,
        relief="flat",
        font=("Segoe UI", fsz),
    )
    style.map("TNotebook.Tab",
        background=[("selected", panel), ("active", btn_active)],
        foreground=[("selected", accent), ("active", strong_text)],
        bordercolor=[("selected", border_hi)],
        font=[("selected", ("Segoe UI Semibold", fsz))],
    )

    # ── Treeview ──────────────────────────────────────────────────────────
    style.configure("Treeview",
        background=panel,
        fieldbackground=panel,
        foreground=strong_text,
        bordercolor=border,
        rowheight=row_h,
        relief="flat",
        font=("Segoe UI", fsz),
    )
    style.map("Treeview",
        background=[("selected", sel_bg)],
        foreground=[("selected", treesel_fg)],
    )
    style.configure("Treeview.Heading",
        background=panel_2,
        foreground=text_sub,
        bordercolor=border,
        padding=(8, 6),
        font=("Segoe UI Semibold", fsz_sm),
        relief="flat",
    )
    style.map("Treeview.Heading",
        background=[("active", btn_active), ("pressed", btn_pressed)],
        foreground=[("active", accent)],
    )

    # ── Scrollbars ────────────────────────────────────────────────────────
    _sb_trough = bg if dark_mode else LIGHT_BG
    style.configure("Vertical.TScrollbar",
        background=panel_3,
        troughcolor=_sb_trough,
        bordercolor=border,
        arrowcolor=muted,
        gripcount=0,
        relief="flat",
    )
    style.map("Vertical.TScrollbar",
        background=[("active", border), ("pressed", accent)],
        arrowcolor=[("active", accent)],
    )
    style.configure("Horizontal.TScrollbar",
        background=panel_3,
        troughcolor=_sb_trough,
        bordercolor=border,
        arrowcolor=muted,
        gripcount=0,
        relief="flat",
    )
    style.map("Horizontal.TScrollbar",
        background=[("active", border), ("pressed", accent)],
        arrowcolor=[("active", accent)],
    )

    # ── Separator ─────────────────────────────────────────────────────────
    style.configure("TSeparator", background=border)

    # ── Progressbar ───────────────────────────────────────────────────────
    style.configure("TProgressbar",
        background=accent,
        troughcolor=panel_2,
        bordercolor=border,
        lightcolor=accent,
        darkcolor=accent,
    )

    # ── Scale ─────────────────────────────────────────────────────────────
    style.configure("TScale",
        background=bg,
        troughcolor=panel_3,
        bordercolor=border,
        slidercolor=accent,
    )
    style.map("TScale", slidercolor=[("active", accent_hi)])
