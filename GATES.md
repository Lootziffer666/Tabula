# 🚪 GATES — TABULA SUITE

---

## 🔜 Nächste Gates

### Gate TAB-011: Network Share Scanner
- **Branch:** `gate/tab-011-network-scan`
- **To-Dos:**
  - [ ] SMB/CIFS Share Discovery
  - [ ] Freigabe-Inventar mit Größe
  - [ ] Orphaned Shares erkennen
  - [ ] Report exportierbar
- **Akzeptanz:** Netzwerk-Shares inventarisiert
- **Kill:** Shares ohne Größenangabe

### Gate TAB-012: Startup Optimizer
- **Branch:** `gate/tab-012-startup`
- **To-Dos:**
  - [ ] Autostart-Programme inventarisieren
  - [ ] Impact-Klassifikation (High/Med/Low)
  - [ ] Sichere Disable-Vorschläge
  - [ ] Vorher/Nachher-Boot-Time
- **Akzeptanz:** Autostart übersichtlich, Disable sicher
- **Kill:** Automatisches Disable ohne Bestätigung

### Gate TAB-013: Disk Space Treemap
- **Branch:** `gate/tab-013-treemap`
- **To-Dos:**
  - [ ] Treemap-Visualisierung der Ordnergrößen
  - [ ] Drill-Down per Klick
  - [ ] Farbkodierung nach Alter/Typ
  - [ ] Export als PNG/HTML
- **Akzeptanz:** Visuell korrekte Treemap
- **Kill:** Treemap > 10s Ladezeit für 1TB

### Gate TAB-014: AI-Assisted Classification
- **Branch:** `gate/tab-014-ai-classify`
- **To-Dos:**
  - [ ] Ollama-Integration für Datei-Klassifikation
  - [ ] "Was ist das?"-Analyse pro Ordner
  - [ ] Confidence-Score anzeigen
  - [ ] Offline-Fallback-Heuristik
- **Akzeptanz:** AI-Vorschläge korrekt ≥80%
- **Kill:** AI-Klassifikation ohne Offline-Fallback
