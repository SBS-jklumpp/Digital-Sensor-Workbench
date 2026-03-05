import tkinter as tk
from tkinter import ttk

# ═══════════════════════════════════════════════════════════════════════════════
# MODERN PROFESSIONAL DARK PALETTE — Glass-morphic Deep Ocean
# ═══════════════════════════════════════════════════════════════════════════════
# Ultra-deep backgrounds with subtle blue undertones
# Vivid teal-cyan accent for CTAs · Refined typography contrast
DARK_BG        = "#040810"   # near-black with blue undertone
DARK_PANEL     = "#0a1220"   # primary panel — deep navy
DARK_PANEL_2   = "#121e2e"   # elevated surface — card/hover bg
DARK_PANEL_3   = "#1a2a42"   # tertiary surface — treeview rows
DARK_BORDER    = "#2a3e5c"   # subtle borders — low contrast
DARK_BORDER_HI = "#4d9fff"   # focused / active borders — electric blue
DARK_TEXT      = "#f0f4f8"   # primary text — near white warm
DARK_TEXT_SUB  = "#b8c4d0"   # secondary text
DARK_MUTED     = "#5e7087"   # muted / disabled — steel blue
DARK_ACCENT    = "#00d4aa"   # vivid teal accent — modern CTA
DARK_ACCENT_DIM= "#00a888"   # pressed accent
DARK_ACCENT_HI = "#33ffe4"   # hover accent — glow effect
DARK_OK        = "#00e676"   # neon green pass/ok
DARK_WARN      = "#ffab00"   # amber warning
DARK_FAIL      = "#ff5252"   # coral red fail/error
DARK_SEL_BG    = "#0d2a40"   # treeview selection row — deep blue tint

# Supplementary accent colors for richer UI
DARK_INFO      = "#40c4ff"   # info blue
DARK_PURPLE    = "#b388ff"   # purple accent for special states
DARK_CANVAS    = "#060e18"   # ultra-deep canvas background

# ═══════════════════════════════════════════════════════════════════════════════
# MODERN PROFESSIONAL LIGHT PALETTE
# ═══════════════════════════════════════════════════════════════════════════════
LIGHT_BG       = "#f8fafc"   # soft cool white
LIGHT_PANEL    = "#ffffff"
LIGHT_PANEL_2  = "#e8f0f8"   # elevated panel
LIGHT_BORDER   = "#c4d4e4"   # subtle border
LIGHT_BORDER_HI= "#0066ff"   # focused border
LIGHT_TEXT     = "#0f172a"   # near black
LIGHT_TEXT_SUB = "#475569"   # secondary text
LIGHT_MUTED    = "#94a3b8"   # muted/disabled
LIGHT_ACCENT   = "#0066ff"   # primary blue
LIGHT_ACCENT_HI= "#338aff"   # hover accent
LIGHT_ACCENT_DIM="#0052cc"   # pressed accent
LIGHT_OK       = "#00c853"   # success green
LIGHT_WARN     = "#ff9100"   # warning orange
LIGHT_FAIL     = "#ff1744"   # error red
LIGHT_SEL_BG   = "#e0f2ff"   # selection row

# Font configuration — use system UI fonts for crisp rendering
DEFAULT_FONT   = ("Segoe UI Variable", 9)
HEADER_FONT    = ("Segoe UI Variable Display", 9)
MONO_FONT      = ("Cascadia Code", 10)


def apply_theme(root: tk.Tk, field_mode: bool = False, dark_mode: bool = True):
    """Apply a modern professional theme to all ttk widgets with enhanced visual polish."""
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
        btn_active = "#162030"
        btn_pressed= "#0e1824"
        btn_hover  = "#1a2c42"
        treesel_fg = "#ffffff"
        input_bg   = "#0c1624"
        canvas_bg  = DARK_CANVAS if 'DARK_CANVAS' in dir() else "#060e18"
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
        btn_active = "#e8f4ff"
        btn_pressed= "#d0e8ff"
        btn_hover  = "#f0f6fc"
        treesel_fg = "#0f172a"
        input_bg   = "#ffffff"
        canvas_bg  = "#f8fafc"

    # Refined font sizes for modern look
    fsz            = 12 if field_mode else 10
    fsz_sm         = 11 if field_mode else 9
    fsz_xs         = 10 if field_mode else 8
    strong_text    = "#ffffff" if (field_mode and dark_mode) else text
    btn_pad        = (10, 5) if field_mode else (8, 4)
    primary_pad    = (12, 6) if field_mode else (10, 5)
    tab_pad        = [22, 10] if field_mode else [18, 8]
    row_h          = 32 if field_mode else 28
    entry_pad      = 7 if field_mode else 5

    root.configure(bg=bg)

    # ══ Base defaults ════════════════════════════════════════════════════════
    style.configure(".",
        background=bg,
        foreground=strong_text,
        fieldbackground=panel,
        bordercolor=border,
        borderwidth=1,
        relief="flat",
        font=("Segoe UI Variable", fsz),
        focuscolor=accent,
    )

    # ══ Frames ═══════════════════════════════════════════════════════════════
    style.configure("TFrame", background=bg)
    style.configure("Card.TFrame", background=panel_2, relief="flat")
    style.configure("Elevated.TFrame", background=panel_2, relief="flat")


    # ══ LabelFrame — modern section card with accent header ═════════════════
    style.configure("TLabelframe",
        background=bg,
        foreground=text,
        bordercolor=border,
        borderwidth=1,
        relief="flat",
        padding=(10, 8),
    )
    style.configure("TLabelframe.Label",
        background=bg,
        foreground=accent,
        font=("Segoe UI Variable", fsz_sm, "bold"),
        padding=(2, 0, 0, 3),
    )

    # ══ Labels — refined typography hierarchy ════════════════════════════════
    style.configure("TLabel",
        background=bg,
        foreground=strong_text,
        font=("Segoe UI Variable", fsz),
    )
    style.configure("Muted.TLabel",
        background=bg,
        foreground=muted,
        font=("Segoe UI Variable", fsz_sm),
    )
    style.configure("Small.TLabel",
        background=bg,
        foreground=text_sub,
        font=("Segoe UI Variable", fsz_xs),
    )
    style.configure("OK.TLabel",    background=bg, foreground=ok,   font=("Segoe UI Variable", fsz, "bold"))
    style.configure("Warn.TLabel",  background=bg, foreground=warn, font=("Segoe UI Variable", fsz, "bold"))
    style.configure("Fail.TLabel",  background=bg, foreground=fail, font=("Segoe UI Variable", fsz, "bold"))
    style.configure("Accent.TLabel",background=bg, foreground=accent, font=("Segoe UI Variable", fsz, "bold"))
    style.configure("Header.TLabel",background=bg, foreground=text, font=("Segoe UI Variable Display", fsz + 4, "bold"))
    style.configure("Subheader.TLabel",background=bg, foreground=text_sub, font=("Segoe UI Variable", fsz_sm))

    # ══ Standard button — refined with better hover states ══════════════════
    style.configure("TButton",
        background=panel_2,
        foreground=strong_text,
        bordercolor=border,
        focuscolor=accent,
        padding=btn_pad,
        relief="flat",
        font=("Segoe UI Variable", fsz_sm),
    )
    style.map("TButton",
        background=[("active", btn_hover), ("pressed", btn_pressed), ("disabled", panel)],
        foreground=[("disabled", muted)],
        bordercolor=[("focus", accent), ("active", border_hi)],
    )

    # ══ Primary (accent-filled) button — vibrant CTA ═════════════════════════
    style.configure("Primary.TButton",
        background=accent,
        foreground="#000000" if dark_mode else "#ffffff",
        bordercolor=accent,
        focuscolor=accent_hi,
        padding=primary_pad,
        relief="flat",
        font=("Segoe UI Variable", fsz_sm, "bold"),
    )
    style.map("Primary.TButton",
        background=[("active", accent_hi), ("pressed", accent_dim), ("disabled", panel_2)],
        foreground=[("disabled", muted)],
        bordercolor=[("active", accent_hi), ("pressed", accent_dim)],
    )

    # ══ Secondary button — subtle outline style ══════════════════════════════
    style.configure("Secondary.TButton",
        background=bg,
        foreground=accent,
        bordercolor=accent,
        focuscolor=accent_hi,
        padding=btn_pad,
        relief="flat",
        font=("Segoe UI Variable", fsz_sm),
    )
    style.map("Secondary.TButton",
        background=[("active", panel_2), ("pressed", panel)],
        foreground=[("active", accent_hi), ("disabled", muted)],
        bordercolor=[("active", accent_hi), ("disabled", border)],
    )

    # ══ Danger button — clear warning appearance ════════════════════════════
    style.configure("Danger.TButton",
        background=panel_2,
        foreground=fail,
        bordercolor=fail,
        padding=btn_pad,
        relief="flat",
        font=("Segoe UI Variable", fsz_sm),
    )
    style.map("Danger.TButton",
        background=[("active", "#1a0f0f" if dark_mode else "#fef2f2"),
                    ("pressed", "#2a1515" if dark_mode else "#fee2e2")],
        foreground=[("disabled", muted)],
        bordercolor=[("active", fail), ("disabled", border)],
    )

    # ══ Success button ══════════════════════════════════════════════════════
    style.configure("Success.TButton",
        background=ok,
        foreground="#000000" if dark_mode else "#ffffff",
        bordercolor=ok,
        padding=btn_pad,
        relief="flat",
        font=("Segoe UI Variable", fsz_sm, "bold"),
    )
    style.map("Success.TButton",
        background=[("active", ok), ("pressed", ok), ("disabled", panel_2)],
        foreground=[("disabled", muted)],
    )

    # ══ Toolbar button — compact, icon-like ════════════════════════════════
    style.configure("Toolbar.TButton",
        background=bg,
        foreground=text_sub,
        bordercolor=bg,
        padding=(6, 3),
        relief="flat",
        font=("Segoe UI Variable", fsz_xs),
    )
    style.map("Toolbar.TButton",
        background=[("active", panel_2), ("pressed", panel)],
        foreground=[("active", text), ("disabled", muted)],
        bordercolor=[("active", border)],
    )

    # ══ Entry — modern input field ══════════════════════════════════════════
    style.configure("TEntry",
        fieldbackground=input_bg if 'input_bg' in dir() else panel,
        foreground=strong_text,
        bordercolor=border,
        insertcolor=accent,
        selectbackground=sel_bg,
        selectforeground=strong_text,
        padding=entry_pad,
        relief="flat",
    )
    style.map("TEntry",
        bordercolor=[("focus", accent), ("hover", border_hi)],
        fieldbackground=[("disabled", panel_2), ("readonly", panel_2)],
        foreground=[("disabled", muted), ("readonly", text_sub)],
    )

    # ══ Combobox — dropdown selector ════════════════════════════════════════
    style.configure("TCombobox",
        fieldbackground=input_bg if 'input_bg' in dir() else panel,
        background=panel_2,
        foreground=strong_text,
        bordercolor=border,
        arrowcolor=text_sub,
        padding=entry_pad,
        relief="flat",
    )
    style.map("TCombobox",
        fieldbackground=[("readonly", input_bg if 'input_bg' in dir() else panel), ("active", panel)],
        foreground=[("readonly", strong_text), ("disabled", muted)],
        arrowcolor=[("active", accent), ("hover", accent), ("focus", accent)],
        bordercolor=[("focus", accent)],
    )

    # ══ Spinbox — numeric input with arrows ═════════════════════════════════
    style.configure("TSpinbox",
        fieldbackground=input_bg if 'input_bg' in dir() else panel,
        foreground=strong_text,
        bordercolor=border,
        arrowcolor=text_sub,
        insertcolor=accent,
        padding=entry_pad,
        relief="flat",
    )
    style.map("TSpinbox",
        arrowcolor=[("active", accent), ("focus", accent)],
        bordercolor=[("focus", accent), ("hover", border_hi)],
        fieldbackground=[("disabled", panel_2)],
    )

    # ══ Checkbutton — modern toggle indicator ═══════════════════════════════
    style.configure("TCheckbutton",
        background=bg,
        foreground=strong_text,
        focuscolor=accent,
        padding=(3, 3),
        indicatorcolor=panel_3 if dark_mode else LIGHT_PANEL,
        indicatormargin=(0, 0, 8, 0),
        font=("Segoe UI Variable", fsz_sm),
    )
    style.map("TCheckbutton",
        background=[("active", bg)],
        foreground=[("active", strong_text), ("disabled", muted)],
        indicatorcolor=[("selected", accent), ("selected active", accent_hi)],
    )

    # ══ Radiobutton — clean radio selector ══════════════════════════════════
    style.configure("TRadiobutton",
        background=bg,
        foreground=strong_text,
        focuscolor=accent,
        padding=(3, 3),
        font=("Segoe UI Variable", fsz_sm),
    )
    style.map("TRadiobutton",
        background=[("active", bg)],
        foreground=[("active", strong_text), ("disabled", muted)],
        indicatorcolor=[("selected", accent), ("selected active", accent_hi)],
    )

    # ══ Notebook tabs — sleek tabbed interface ══════════════════════════════
    style.configure("TNotebook",
        background=bg,
        bordercolor=border,
        tabmargins=[4, 6, 4, 0],
        padding=0,
    )
    style.configure("TNotebook.Tab",
        background=panel_2,
        foreground=muted,
        padding=tab_pad,
        bordercolor=border,
        relief="flat",
        font=("Segoe UI Variable", fsz_sm),
    )
    style.map("TNotebook.Tab",
        background=[("selected", panel), ("active", btn_hover if 'btn_hover' in dir() else panel_2)],
        foreground=[("selected", accent), ("active", strong_text)],
        bordercolor=[("selected", accent)],
        font=[("selected", ("Segoe UI Variable", fsz_sm, "bold"))],
    )

    # ══ Treeview — clean data grid ══════════════════════════════════════════
    style.configure("Treeview",
        background=panel,
        fieldbackground=panel,
        foreground=strong_text,
        bordercolor=border,
        rowheight=row_h,
        relief="flat",
        font=("Segoe UI Variable", fsz_sm),
    )
    style.map("Treeview",
        background=[("selected", sel_bg)],
        foreground=[("selected", treesel_fg)],
    )
    style.configure("Treeview.Heading",
        background=panel_2,
        foreground=text_sub,
        bordercolor=border,
        padding=(10, 7),
        font=("Segoe UI Variable", fsz_sm, "bold"),
        relief="flat",
    )
    style.map("Treeview.Heading",
        background=[("active", panel_3), ("pressed", panel)],
        foreground=[("active", accent)],
    )

    # ══ Scrollbars — minimal, modern appearance ═════════════════════════════
    _sb_trough = panel if dark_mode else LIGHT_BG
    _sb_thumb = panel_3 if dark_mode else "#cbd5e1"
    _sb_thumb_hover = border if dark_mode else "#94a3b8"
    style.configure("Vertical.TScrollbar",
        background=_sb_thumb,
        troughcolor=_sb_trough,
        bordercolor=_sb_trough,
        arrowcolor=_sb_trough,
        gripcount=0,
        relief="flat",
        width=10,
    )
    style.map("Vertical.TScrollbar",
        background=[("active", _sb_thumb_hover), ("pressed", accent)],
        arrowcolor=[("active", _sb_trough)],
    )
    style.configure("Horizontal.TScrollbar",
        background=_sb_thumb,
        troughcolor=_sb_trough,
        bordercolor=_sb_trough,
        arrowcolor=_sb_trough,
        gripcount=0,
        relief="flat",
        width=10,
    )
    style.map("Horizontal.TScrollbar",
        background=[("active", _sb_thumb_hover), ("pressed", accent)],
        arrowcolor=[("active", _sb_trough)],
    )

    # ══ Separator — subtle divider ══════════════════════════════════════════
    style.configure("TSeparator", background=border)
    style.configure("Accent.TSeparator", background=accent)

    # ══ Progressbar — animated progress indicator ═══════════════════════════
    style.configure("TProgressbar",
        background=accent,
        troughcolor=panel_2,
        bordercolor=panel_2,
        lightcolor=accent_hi,
        darkcolor=accent_dim,
        thickness=6,
    )

    # ══ Scale — slider control ══════════════════════════════════════════════
    style.configure("TScale",
        background=bg,
        troughcolor=panel_2,
        bordercolor=panel_2,
        slidercolor=accent,
    )
    style.map("TScale", slidercolor=[("active", accent_hi)])
