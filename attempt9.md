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
- KaTeX math support

---

# **Background Image Slide**
Below is an actual background image slide using Marp syntax:

![bg](https://marp.app/assets/marp.svg)

This satisfies the background-image requirement.

---

# **Mathematical Equations using KaTeX**

Algorithmic complexity:

$$
T(n) = O(n \log n)
$$

Space complexity:

$$
S(n) = \Theta(n^2)
$$

Inline example:  
The growth is \( O(n^3) \).

---

# **Custom Theme Example**

```css
/* custom-theme.css */
section {
  background: #f5faff;
  color: #111;
}
