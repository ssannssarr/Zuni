# hide sidebars on home
sed -i '1i ---\nhide:\n  - navigation\n  - toc\n---\n' docs/index.md

# full-width home
cat >> docs/stylesheets/home.css <<'EOF'

/* ---------- Laptop / full-width fix ---------- */
.md-main__inner:has(.zuni-hero) {
  max-width: none;
  margin: 0;
}

.md-content:has(.zuni-hero) {
  max-width: none;
}

.md-content__inner:has(.zuni-hero)::before {
  display: none;
}

@media screen and (min-width: 769px) {
  .zuni-hero {
    min-height: 82vh;
  }
}
EOF
