---
marp: true
theme: custom-theme
paginate: true
header: "Product Documentation – Technical Writer"
footer: "© 2025 | Contact: 22f2000771@ds.study.iitm.ac.in"
---

<!--
This is the Custom Theme
Save this file as slides.md (or similar) in your GitHub repo.
-->

<style>
/* Custom Theme Styling */
section {
  font-family: "Segoe UI", sans-serif;
  padding: 40px;
}
h1 {
  color: #004aad;
  font-weight: 700;
}
h2 {
  color: #0085ff;
}
footer {
  font-size: 12px;
  color: #666;
}
/* Page number styling */
section::after {
  content: attr(data-marpit-pagination) "/" attr(data-marpit-pagination-total);
  position: absolute;
  bottom: 20px;
  right: 30px;
  font-size: 14px;
  color: #444;
}
</style>

---

# **Product Documentation Presentation**
### Technical Writer: *Ashwadhi*  
📧 22f2000771@ds.study.iitm.ac.in  

This presentation demonstrates how to create maintainable, version-controlled documentation using **Marp**.

---

# **Why Marp?**
- Markdown-based → easy for developers to maintain  
- Version-control friendly  
- Exportable:  
  - PDF  
  - PPTX  
  - HTML  
- Supports themes, diagrams, and math equations  

---

<!-- _backgroundImage is a Marp directive for background images -->
<!-- Replace with any public image URL if needed -->
![bg opacity=0.25](https://marp.app/assets/marp.svg)

# **Slide with Background Image**
Marp supports **full-width background images**, great for branding and visual storytelling.

Use directive:

```markdown
![bg](image_url)
