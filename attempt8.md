---
marp: true
theme: custom-theme
paginate: true
math: katex
header: "Product Documentation – Technical Writer"
footer: "© 2025 | Contact: 22f2000771@ds.study.iitm.ac.in"
---

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

<!-- _class: lead -->
# **Product Documentation Presentation**
### Technical Writer: *Ashwadhi*  
📧 **22f2000771@ds.study.iitm.ac.in**

---

# **Why Marp?**
- Markdown-based  
- Version-controlled  
- Converts to PDF, HTML, PPTX  
- Custom themes  
- **KaTeX math support**

---

<!-- _backgroundImage: "https://marp.app/assets/marp.svg" -->
<!-- _backgroundOpacity: 0.25 -->
# **Background Image Slide**
This slide uses a Marp background-image directive.

---

# **Mathematical Equations using KaTeX**

Time complexity:

$$
T(n) = O(n \log n)
$$

Space complexity:

$$
S(n) = \Theta(n^2)
$$

Inline example:  
Growth is \( O(n^3) \).

---

# **Example of a Custom Theme**
```css
/* custom-theme.css */
section {
  background: #f5faff;
  color: #111;
}
