import os
import re

ROOT_FOOTER = """  <footer class="footer">
    <div class="container">
      <div class="footer__grid">
        <div class="footer__brand">
          <a href="index.html" class="footer__logo" aria-label="Booklee Technologies home">
            <img src="assets/images/booklee-logo.png" alt="Booklee Technologies" class="footer__logo-img" width="560" height="560" decoding="async" loading="lazy">
          </a>
          <p>We engineer digital products that scale - combining product thinking, technical excellence, and growth strategy for ambitious teams.</p>
        </div>
        <div>
          <h3 class="footer__heading">Company</h3>
          <a href="about.html" class="footer__link">About</a>
          <a href="services.html" class="footer__link">Services</a>
          <a href="book-call.html" class="footer__link">Book a Call</a>
        </div>
        <div>
          <h3 class="footer__heading">Services</h3>
          <a href="services/product-engineering.html" class="footer__link">Product Engineering</a>
          <a href="services/system-architecture.html" class="footer__link">System Architecture</a>
          <a href="services/web-engineering.html" class="footer__link">Web Engineering</a>
          <a href="services/ui-ux-systems.html" class="footer__link">UI/UX Systems</a>
          <a href="services/digital-growth-strategy.html" class="footer__link">Digital Growth Strategy</a>
          <a href="services/product-strategy-consulting.html" class="footer__link">Product Strategy &amp; Consulting</a>
        </div>
        <div>
          <h3 class="footer__heading">Contact</h3>
          <a href="mailto:bookleetechnologies@gmail.com" class="footer__link" data-site-email="text">bookleetechnologies@gmail.com</a>
          <a href="contact.html" class="footer__link">Contact Form</a>
        </div>
      </div>
      <div class="footer__final" id="footer-signature">
        <div class="footer__final-left">
          <p class="footer__copyright">&copy; <span id="year"></span> Booklee Technologies. All rights reserved.</p>
          <div class="footer__social-pills">
            <a href="https://www.linkedin.com/company/booklee-technologies/" class="footer__pill" data-site-linkedin target="_blank" rel="noopener noreferrer">LinkedIn</a>
            <a href="https://www.instagram.com/booklee.in/" class="footer__pill" data-site-instagram target="_blank" rel="noopener noreferrer">Instagram</a>
          </div>
        </div>
        <div class="footer__final-right">
          <div class="footer__signature-glow" id="footer-booklee-glow" aria-hidden="true"></div>
          <span class="footer__booklee reveal-stagger" role="img" aria-label="Booklee">
            <span class="footer__booklee-char" tabindex="0">B</span>
            <span class="footer__booklee-char" tabindex="0">o</span>
            <span class="footer__booklee-char" tabindex="0">o</span>
            <span class="footer__booklee-char" tabindex="0">k</span>
            <span class="footer__booklee-char" tabindex="0">l</span>
            <span class="footer__booklee-char" tabindex="0">e</span>
            <span class="footer__booklee-char" tabindex="0">e</span>
          </span>
        </div>
      </div>
    </div>
  </footer>"""

NESTED_FOOTER = """  <footer class="footer">
    <div class="container">
      <div class="footer__grid">
        <div class="footer__brand">
          <a href="../index.html" class="footer__logo" aria-label="Booklee Technologies home">
            <img src="../assets/images/booklee-logo.png" alt="Booklee Technologies" class="footer__logo-img" width="560" height="560" decoding="async" loading="lazy">
          </a>
          <p>We engineer digital products that scale - combining product thinking, technical excellence, and growth strategy for ambitious teams.</p>
        </div>
        <div>
          <h3 class="footer__heading">Company</h3>
          <a href="../about.html" class="footer__link">About</a>
          <a href="../services.html" class="footer__link">Services</a>
          <a href="../book-call.html" class="footer__link">Book a Call</a>
        </div>
        <div>
          <h3 class="footer__heading">Services</h3>
          <a href="product-engineering.html" class="footer__link">Product Engineering</a>
          <a href="system-architecture.html" class="footer__link">System Architecture</a>
          <a href="web-engineering.html" class="footer__link">Web Engineering</a>
          <a href="ui-ux-systems.html" class="footer__link">UI/UX Systems</a>
          <a href="digital-growth-strategy.html" class="footer__link">Digital Growth Strategy</a>
          <a href="product-strategy-consulting.html" class="footer__link">Product Strategy &amp; Consulting</a>
        </div>
        <div>
          <h3 class="footer__heading">Contact</h3>
          <a href="mailto:bookleetechnologies@gmail.com" class="footer__link" data-site-email="text">bookleetechnologies@gmail.com</a>
          <a href="../contact.html" class="footer__link">Contact Form</a>
        </div>
      </div>
      <div class="footer__final" id="footer-signature">
        <div class="footer__final-left">
          <p class="footer__copyright">&copy; <span id="year"></span> Booklee Technologies. All rights reserved.</p>
          <div class="footer__social-pills">
            <a href="https://www.linkedin.com/company/booklee-technologies/" class="footer__pill" data-site-linkedin target="_blank" rel="noopener noreferrer">LinkedIn</a>
            <a href="https://www.instagram.com/booklee.in/" class="footer__pill" data-site-instagram target="_blank" rel="noopener noreferrer">Instagram</a>
          </div>
        </div>
        <div class="footer__final-right">
          <div class="footer__signature-glow" id="footer-booklee-glow" aria-hidden="true"></div>
          <span class="footer__booklee reveal-stagger" role="img" aria-label="Booklee">
            <span class="footer__booklee-char" tabindex="0">B</span>
            <span class="footer__booklee-char" tabindex="0">o</span>
            <span class="footer__booklee-char" tabindex="0">o</span>
            <span class="footer__booklee-char" tabindex="0">k</span>
            <span class="footer__booklee-char" tabindex="0">l</span>
            <span class="footer__booklee-char" tabindex="0">e</span>
            <span class="footer__booklee-char" tabindex="0">e</span>
          </span>
        </div>
      </div>
    </div>
  </footer>"""

def update_file(filepath, is_nested):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the footer tag using regex
    # Match from <footer class="footer"> to </footer>
    pattern = re.compile(r'  <footer class="footer">.*?</footer>', re.DOTALL)
    
    footer_text = NESTED_FOOTER if is_nested else ROOT_FOOTER
    new_content, count = pattern.subn(footer_text, content)
    
    if count == 0:
        # try without the spaces
        pattern2 = re.compile(r'<footer class="footer">.*?</footer>', re.DOTALL)
        new_content, count = pattern2.subn(footer_text, content)
    
    if count > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filepath}")
    else:
        print(f"Footer not found in {filepath}")

# Root files
root_files = ['index.html', 'about.html', 'services.html', 'contact.html', 'book-call.html']
for f in root_files:
    update_file(f, False)

# Nested files
services_dir = 'services'
if os.path.exists(services_dir):
    for f in os.listdir(services_dir):
        if f.endswith('.html'):
            update_file(os.path.join(services_dir, f), True)
