# -*- coding: utf-8 -*-
"""Build the Primrose Peach Light / Dark color themes from one palette table.

    py -3 scripts/build-theme.py
"""

import json
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
THEMES = BASE / "themes"
NAME = "primrose-peach-theme"
SLUG = "primrose-peach"
DISPLAY = "Primrose Peach Theme"
VERSION = "1.0.0"
REPO = "https://github.com/vaxicy/primrose-peach-theme"

UI = {
    "foreground": ("#46302C", "#F0E6DC"),
    "editor.foreground": ("#46302C", "#F0E6DC"),
    "terminal.foreground": ("#46302C", "#F0E6DC"),
    "input.foreground": ("#3B2724", "#F7EFE6"),
    "dropdown.foreground": ("#3B2724", "#F7EFE6"),
    "quickInput.foreground": ("#3B2724", "#F7EFE6"),
    "editorWidget.foreground": ("#3B2724", "#F7EFE6"),
    "editorHoverWidget.foreground": ("#3B2724", "#F7EFE6"),
    "editorSuggestWidget.foreground": ("#3B2724", "#F7EFE6"),
    "notifications.foreground": ("#3B2724", "#F7EFE6"),
    "descriptionForeground": ("#A08C86", "#A3B5AA"),
    "input.placeholderForeground": ("#A08C86", "#A3B5AA"),
    "focusBorder": ("#C9556E", "#FFACBD"),
    "inputOption.activeBorder": ("#B04E63", "#F5B9C6"),
    "input.border": ("#F0E2D8", "#33443B"),
    "dropdown.border": ("#F0E2D8", "#33443B"),
    "editor.background": ("#FFFFFF", "#22302A"),
    "tab.activeBackground": ("#FFFFFF", "#22302A"),
    "titleBar.activeBackground": ("#FCD6B4", "#1B2621"),
    "titleBar.activeForeground": ("#5A4034", "#D9CFC2"),
    "titleBar.inactiveBackground": ("#FDE7D4", "#1F2A25"),
    "titleBar.inactiveForeground": ("#9C8478", "#8A9A90"),
    "activityBar.background": ("#FDEBDD", "#19231F"),
    "activityBar.foreground": ("#C0705E", "#E8A9B5"),
    "activityBar.activeBorder": ("#C9556E", "#FFACBD"),
    "activityBar.inactiveForeground": ("#C4A99B", "#6E8077"),
    "sideBar.background": ("#FFFAF7", "#1F2A25"),
    "sideBar.foreground": ("#4A3733", "#D6CEC2"),
    "sideBarSectionHeader.background": ("#FDF0E6", "#27332C"),
    "sideBarSectionHeader.foreground": ("#5A4034", "#E2D8CB"),
    "panel.background": ("#FFFCF8", "#1E2823"),
    "terminal.background": ("#FFFCF8", "#1E2823"),
    "panel.border": ("#F0E2D8", "#33443B"),
    "editorGroup.border": ("#F0E2D8", "#33443B"),
    "tab.border": ("#F0E2D8", "#33443B"),
    "sideBar.border": ("#F0E2D8", "#33443B"),
    "titleBar.border": ("#F0E2D8", "#33443B"),
    "statusBar.background": ("#4FA8A5", "#3E6B62"),
    "statusBar.noFolderBackground": ("#4FA8A5", "#3E6B62"),
    "statusBar.foreground": ("#FFFFFF", "#F2E9E0"),
    "statusBar.noFolderForeground": ("#FFFFFF", "#F2E9E0"),
    "statusBarItem.hoverBackground": ("#42938F", "#4C7A71"),
    "statusBar.debuggingBackground": ("#B0742E", "#8A6532"),
    "statusBar.debuggingForeground": ("#FFF9F2", "#F7EEDF"),
    "editorGroupHeader.tabsBackground": ("#F7F0EA", "#1E2823"),
    "tab.inactiveBackground": ("#F7F0EA", "#1E2823"),
    "tab.activeForeground": ("#3B2724", "#F7EFE6"),
    "tab.activeBorderTop": ("#C9556E", "#FFACBD"),
    "tab.inactiveForeground": ("#9C8478", "#96A79C"),
    "tab.hoverBackground": ("#FBEBDF", "#27332C"),
    "tab.activeModifiedBorder": ("#B0742E", "#F0C88A"),
    "tab.inactiveModifiedBorder": ("#B0742E", "#F0C88A"),
    "list.hoverBackground": ("#FFF5EC", "#27332C"),
    "list.activeSelectionBackground": ("#CFEDEA", "#3A4A42"),
    "editorSuggestWidget.selectedBackground": ("#CFEDEA", "#3A4A42"),
    "list.activeSelectionForeground": ("#2A3A36", "#F7EFE6"),
    "list.inactiveSelectionForeground": ("#2A3A36", "#F7EFE6"),
    "editorSuggestWidget.selectedForeground": ("#2A3A36", "#F7EFE6"),
    "list.inactiveSelectionBackground": ("#E2F4F2", "#33443B"),
    "list.highlightForeground": ("#C9556E", "#FFACBD"),
    "list.focusHighlightForeground": ("#C9556E", "#FFACBD"),
    "tree.indentGuidesStroke": ("#EEDFD4", "#33443B"),
    "editorLineNumber.foreground": ("#BBA69E", "#6E8077"),
    "editorLineNumber.activeForeground": ("#C9556E", "#FFACBD"),
    "editor.lineHighlightBackground": ("#FFF8F2", "#27332C"),
    "editor.lineHighlightBorder": ("#FBEBDD", "#2F3C34"),
    "editorCursor.foreground": ("#4FA8A5", "#FFACBD"),
    "selection.background": ("#CFEDEA", "#3A4A42"),
    "editor.selectionBackground": ("#CFEDEA", "#3A4A42"),
    "terminal.selectionBackground": ("#CFEDEA", "#3A4A42"),
    "editor.inactiveSelectionBackground": ("#E2F4F2", "#33443B"),
    "editor.wordHighlightBackground": ("#CFEDEA80", "#4C5F5580"),
    "editor.wordHighlightStrongBackground": ("#CFEDEA80", "#4C5F5580"),
    "editor.selectionHighlightBackground": ("#CFEDEA66", "#4C5F5566"),
    "editor.findMatchHighlightBackground": ("#FBF3C0", "#4A5A4C"),
    "editor.findMatchBackground": ("#F5E79C", "#5A6D5C"),
    "editor.findMatchBorder": ("#B0742E", "#FBF3C0"),
    "editorBracketMatch.background": ("#FDF0DD", "#2F3C34"),
    "editorBracketMatch.border": ("#B1D29B", "#B1D29B"),
    "editorIndentGuide.background1": ("#F1E4DA", "#2F3C34"),
    "editorIndentGuide.activeBackground1": ("#D3BCAF", "#6E8077"),
    "editorWhitespace.foreground": ("#EEDFD4", "#33443B"),
    "editorRuler.foreground": ("#F7EEE6", "#27332C"),
    "textLink.foreground": ("#C9556E", "#FFACBD"),
    "textLink.activeForeground": ("#B04E63", "#F5B9C6"),
    "editorLink.activeForeground": ("#B04E63", "#F5B9C6"),
    "quickInput.background": ("#FFFDFA", "#27332C"),
    "editorHoverWidget.background": ("#FFFDFA", "#27332C"),
    "notifications.background": ("#FFFDFA", "#27332C"),
    "input.background": ("#FFFFFF", "#1F2A25"),
    "dropdown.background": ("#FFFFFF", "#1F2A25"),
    "editorWidget.background": ("#FFFDFA", "#27332C"),
    "editorSuggestWidget.background": ("#FFFDFA", "#27332C"),
    "editorWidget.border": ("#F0E2D8", "#3B4D43"),
    "editorHoverWidget.border": ("#F0E2D8", "#3B4D43"),
    "editorSuggestWidget.border": ("#F0E2D8", "#3B4D43"),
    "notifications.border": ("#F0E2D8", "#3B4D43"),
    "button.background": ("#C9556E", "#FFACBD"),
    "button.foreground": ("#FFFFFF", "#22302A"),
    "button.hoverBackground": ("#B04E63", "#F5B9C6"),
    "button.secondaryBackground": ("#FDEBDD", "#33443B"),
    "button.secondaryForeground": ("#4A3733", "#E2D8CB"),
    "button.secondaryHoverBackground": ("#F7DFCB", "#3A4A42"),
    "badge.background": ("#C9556E", "#FFACBD"),
    "activityBarBadge.background": ("#C9556E", "#FFACBD"),
    "badge.foreground": ("#FFFFFF", "#22302A"),
    "activityBarBadge.foreground": ("#FFFFFF", "#22302A"),
    "scrollbarSlider.background": ("#C4A99B66", "#8A9A9088"),
    "scrollbarSlider.hoverBackground": ("#B3988A88", "#96A79C99"),
    "scrollbarSlider.activeBackground": ("#A2887A99", "#B1D29B99"),
    "errorForeground": ("#B4475C", "#F09A9A"),
    "editorError.foreground": ("#B4475C", "#F09A9A"),
    "problemsErrorIcon.foreground": ("#B4475C", "#F09A9A"),
    "gitDecoration.deletedResourceForeground": ("#B4475C", "#F09A9A"),
    "editorGutter.deletedBackground": ("#B4475C", "#F09A9A"),
    "editorWarning.foreground": ("#A0781F", "#F0C88A"),
    "problemsWarningIcon.foreground": ("#A0781F", "#F0C88A"),
    "editorInfo.foreground": ("#2F8F8B", "#8FD9C4"),
    "problemsInfoIcon.foreground": ("#2F8F8B", "#8FD9C4"),
    "gitDecoration.addedResourceForeground": ("#5F9142", "#B1D29B"),
    "gitDecoration.untrackedResourceForeground": ("#5F9142", "#B1D29B"),
    "editorGutter.addedBackground": ("#5F9142", "#B1D29B"),
    "gitDecoration.modifiedResourceForeground": ("#B0742E", "#F0C88A"),
    "editorGutter.modifiedBackground": ("#B0742E", "#F0C88A"),
    "diffEditor.insertedTextBackground": ("#DFEDCEAA", "#3A4A4266"),
    "diffEditor.removedTextBackground": ("#F7D9DEAA", "#5A3A4066"),
    "diffEditor.insertedLineBackground": ("#DFEDCE66", "#3A4A4244"),
    "diffEditor.removedLineBackground": ("#F7D9DE66", "#5A3A4044"),
    "terminal.ansiBlack": ("#46302C", "#2A3A34"),
    "terminal.ansiRed": ("#B4475C", "#F09A9A"),
    "terminal.ansiGreen": ("#5F9142", "#B1D29B"),
    "terminal.ansiYellow": ("#A0781F", "#F0C88A"),
    "terminal.ansiBlue": ("#3A7A8A", "#A8C6D8"),
    "terminal.ansiMagenta": ("#A05A78", "#E8A9B5"),
    "terminal.ansiCyan": ("#2F8F8B", "#8FD9C4"),
    "terminal.ansiWhite": ("#A08C86", "#D6CEC2"),
    "terminal.ansiBrightBlack": ("#7A6660", "#8A9A90"),
    "terminal.ansiBrightRed": ("#C75E70", "#F7B4B4"),
    "terminal.ansiBrightGreen": ("#74A855", "#CBE4B8"),
    "terminal.ansiBrightYellow": ("#B88E30", "#F7DCAE"),
    "terminal.ansiBrightBlue": ("#4A8A9A", "#BCD6E6"),
    "terminal.ansiBrightMagenta": ("#B46B88", "#F5B9C6"),
    "terminal.ansiBrightCyan": ("#3FA09C", "#BCE4DC"),
    "terminal.ansiBrightWhite": ("#3B2724", "#F7EFE6"),
}

TOKENS = [
    ("comment", ("#A08C86", "#8A9A90"), "italic"),
    (("keyword", "storage"), ("#C25A72", "#FFACBD"), None),
    ("string", ("#7E9B4F", "#D8E4A2"), None),
    (("entity.name.function", "support.function"), ("#2F8F8B", "#8FD9C4"), None),
    (("entity.name.type", "support.type", "support.class"), ("#4A7A86", "#A8C6D8"), None),
    (("constant.numeric", "constant.language", "variable.other.constant"), ("#B0742E", "#F0C88A"), None),
    ("variable", ("#46302C", "#F0E6DC"), None),
    ("variable.parameter", ("#6B5248", "#C9BFB2"), None),
    (("variable.other.property", "support.variable.property"), ("#2F8F8B", "#8FD9C4"), None),
    ("keyword.operator", ("#7A6660", "#B9B3A6"), None),
    ("punctuation", ("#A08C86", "#8A9A90"), None),
    ("entity.name.tag", ("#C25A72", "#FFACBD"), None),
    ("entity.other.attribute-name", ("#B0742E", "#F0C88A"), None),
    ("string.regexp", ("#B0742E", "#DCC48A"), None),
    ("constant.character.escape", ("#A0781F", "#FBF3C0"), None),
    ("markup.heading", ("#3B2724", "#F7EFE6"), "bold"),
    ("markup.bold", ("#3B2724", "#F7EFE6"), "bold"),
    ("markup.italic", ("#3B2724", "#F7EFE6"), "italic"),
    ("invalid", ("#B4475C", "#F09A9A"), None),
]

SEMANTIC = {
    "variable": "#46302C|#F0E6DC",
    "parameter": "#6B5248|#C9BFB2",
    "property": "#2F8F8B|#8FD9C4",
    "function": "#2F8F8B|#8FD9C4",
    "method": "#2F8F8B|#8FD9C4",
    "type": "#4A7A86|#A8C6D8",
    "class": "#4A7A86|#A8C6D8",
    "interface": "#4A7A86|#A8C6D8",
    "variable.readonly": "#B0742E|#F0C88A",
}

PACKAGE = {
    "name": NAME,
    "displayName": DISPLAY,
    "description": "A soft peach palette: white paper with primrose pink and mint in the light variant, a deep moss night in the dark one.",
    "version": VERSION,
    "publisher": "lilinhuang",
    "engines": {"vscode": "^1.80.0"},
    "categories": ["Themes"],
    "keywords": ["theme", "light", "dark", "peach", "floral"],
    "icon": "assets/icon.png",
    "license": "SEE LICENSE IN LICENSE",
    "galleryBanner": {"color": "#22302A", "theme": "dark"},
    "repository": {"type": "git", "url": REPO},
    "contributes": {
        "themes": [
            {"label": f"{DISPLAY} Light", "uiTheme": "vs",
             "path": f"./themes/{SLUG}-light-color-theme.json"},
            {"label": f"{DISPLAY} Dark", "uiTheme": "vs-dark",
             "path": f"./themes/{SLUG}-dark-color-theme.json"},
        ]
    },
}


def build(variant, index):
    colors = {key: pair[index] for key, pair in UI.items()}
    tokens = []
    for scope, pair, style in TOKENS:
        settings = {"foreground": pair[index]}
        if style:
            settings["fontStyle"] = style
        tokens.append({"scope": [scope] if isinstance(scope, str) else list(scope),
                       "settings": settings})
    theme = {
        "name": f"{DISPLAY} {variant.title()}",
        "type": variant,
        "colors": colors,
        "semanticHighlighting": True,
        "semanticTokenColors": {k: v.split("|")[index] for k, v in SEMANTIC.items()},
        "tokenColors": tokens,
    }
    out = THEMES / f"{SLUG}-{variant}-color-theme.json"
    out.write_text(json.dumps(theme, indent=2) + "\n", encoding="utf-8")
    print("wrote", out.relative_to(BASE), len(colors), "UI colors")


def main():
    THEMES.mkdir(exist_ok=True)
    for index, variant in enumerate(("light", "dark")):
        build(variant, index)
    (BASE / "package.json").write_text(json.dumps(PACKAGE, indent=2) + "\n", encoding="utf-8")
    print("wrote package.json")


if __name__ == "__main__":
    main()
