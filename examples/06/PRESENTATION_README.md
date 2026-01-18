# Presentation Export Instructions

This presentation uses **Marp** (Markdown Presentation Ecosystem) for creating slides from markdown.

## Quick Export to PDF

### Option 1: HTML to PDF (Easiest)

The `PRESENTATION.html` file is already generated. To convert to PDF:

**Using Chrome/Edge:**
1. Open `PRESENTATION.html` in Chrome or Edge browser
2. Press `Ctrl+P` (Windows/Linux) or `Cmd+P` (Mac)
3. Select "Save as PDF" as destination
4. Adjust settings:
   - Layout: Landscape
   - Margins: None
   - Background graphics: On
5. Click "Save"

**Using Firefox:**
1. Open `PRESENTATION.html` in Firefox
2. Press `Ctrl+P` or `Cmd+P`
3. Select "Save to PDF"
4. Use Landscape orientation
5. Click "Save"

### Option 2: Marp CLI (Command Line)

```bash
# Install Marp CLI
npm install -g @marp-team/marp-cli

# Export to PDF
marp PRESENTATION.md --pdf --allow-local-files

# Export to PDF with custom theme
marp PRESENTATION.md --pdf --theme default --allow-local-files

# Export to PowerPoint
marp PRESENTATION.md --pptx --allow-local-files
```

### Option 2: VS Code Extension

1. Install the [Marp for VS Code](https://marketplace.visualstudio.com/items?itemName=marp-team.marp-vscode) extension
2. Open `PRESENTATION.md` in VS Code
3. Click the Marp icon in the top-right corner
4. Select "Export Slide Deck..."
5. Choose PDF format
6. Save the file

### Option 3: Marp Web

1. Go to https://web.marp.app/
2. Copy and paste the contents of `PRESENTATION.md`
3. Click "Export" → "PDF"

## Customization

### Themes

The presentation uses the default theme. You can customize by:

1. **Use built-in themes:** Change `theme: default` to `gaia` or `uncover`
2. **Custom CSS:** Modify the `style:` section in the frontmatter
3. **Images:** Add images using standard markdown syntax

### Adding Images

To add images from the analysis folders:

```markdown
![Analysis Chart](./analysis_02/tax_revenue_trends.png)
```

**Note:** For PDF export with local images, use `--allow-local-files` flag.

### LinkedIn Optimization

For best LinkedIn appearance:
- Keep slides concise (current 10 slides + 1 appendix is ideal)
- Use high contrast colors
- Ensure text is readable on mobile
- Export as PDF (most compatible format)

## File Outputs

After export, you'll have:
- `PRESENTATION.pdf` - For LinkedIn attachment
- `PRESENTATION.html` - For web viewing (optional)
- `PRESENTATION.pptx` - For PowerPoint (optional)

## LinkedIn Post Suggestion

```
📊 New Analysis: Estonia's Economic Reality Beyond Government Optimism

Based on Jüri Käo's recent ERR interview, I conducted a comprehensive
empirical study using Statistics Estonia data.

Key findings:
• Consumer confidence paradox explained
• Tax policy impact: +31% revenue, -19% retail sales
• Food inflation crisis: 29.75% peak (2x EU average)
• Vehicle market: 51% collapse post-tax
• 4-year retail decline confirmed

Full analysis validates concerns about disconnect between official
messaging and lived economic experience.

All data sources, methodology, and code available on GitHub.

#Economics #Estonia #DataAnalysis #EmpiricalResearch #PublicPolicy
```

## Troubleshooting

**Issue:** Images not showing in PDF
**Solution:** Use `--allow-local-files` flag with Marp CLI

**Issue:** Fonts look different
**Solution:** Marp uses system fonts. Install matching fonts or specify custom fonts in CSS

**Issue:** PDF too large for LinkedIn (max 100MB)
**Solution:** Use `--pdf-optimize` flag or compress using Adobe Acrobat

## Additional Resources

- [Marp Official Documentation](https://marpit.marp.app/)
- [Marp CLI Documentation](https://github.com/marp-team/marp-cli)
- [Marp Themes](https://github.com/marp-team/marp-core/tree/main/themes)
