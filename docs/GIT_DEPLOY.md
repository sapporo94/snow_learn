# Git and GitHub deployment

## First push

```bash
git init
git add .
git commit -m "Initial NowSkill ServiceNow Bible portal"
git branch -M main
git remote add origin https://github.com/YOUR-USER/YOUR-REPO.git
git push -u origin main
```

## GitHub Pages

For a static site, enable GitHub Pages from the repository settings and publish from the `main` branch root.

This repository also includes a GitHub Actions workflow at `.github/workflows/pages.yml` so every push to `main` can deploy the site automatically.

If you are turning on Pages for the first time, make sure the repository is set to deploy from GitHub Actions.

## Future edits

```bash
git checkout -b content/admin-acls
git add modules/administration.html content/volume0-scope.json
git commit -m "content: expand administration ACL chapter"
git push -u origin content/admin-acls
```

Then open a pull request, review the changed page, and merge.
