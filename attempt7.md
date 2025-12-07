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

# **Product Documentation Presentation**
### Technical Writer: *Ashwadhi*  
📧 22f2000771@ds.study.iitm.ac.in  

---

# **Why Marp?**
- Markdown-based  
- Version-controlled  
- Converts to PDF, HTML, PPTX  
- Custom themes  
- **Built-in KaTeX math support**  

---

![bg opacity=0.25](https://marp.app/assets/marp.svg)

# **Background Image Slide**
This slide demonstrates a full background image.

---

# **Mathematical Equations Using KaTeX**

Algorithmic complexity:

$$
T(n) = O(n \log n)
$$

Another:

$$
\text{Space}(n) = \Theta(n^2)
$$

And an inline example:  
The growth is \( O(n^3) \).

---

# **Custom Theme Definition**
Saved as `custom-theme.css`:

```css
/* custom-theme.css */
section {
  background: #f5faff;
  color: #111;
}
