# Repository Guidelines

## Project Structure & Module Organization
- Main application code lives in `argentum/HAJIME` (Vue 3 + Vite).
- App entry and routing: `argentum/HAJIME/src/main.js`, `argentum/HAJIME/src/router/`.
- UI units: `argentum/HAJIME/src/components/`; page-level views: `argentum/HAJIME/src/views/`.
- Static assets: `argentum/HAJIME/public/` and `argentum/HAJIME/src/assets/`.
- Python practice scripts are centralized in `exercises/` (for example `exercises/training.py`, `exercises/nowai.py`).
- Codeforces/algorithm problem solutions are centralized in `cf_solutions/` (for example `cf_solutions/team.py`, `cf_solutions/watermelon.py`).
- Backend API and tests live in `server/`; keep `server/` and `argentum/` structures unchanged when reorganizing other files.

## Build, Test, and Development Commands
Run commands from `argentum/HAJIME`:
- `pnpm install`: install dependencies.
- `pnpm dev`: start local dev server with hot reload.
- `pnpm build`: create production bundle in `dist/`.
- `pnpm preview`: serve the production build locally.

## Coding Style & Naming Conventions
- Use 2-space indentation in Vue/JS/CSS to match current files.
- Vue SFCs use PascalCase component names (for example `HelloWorld.vue`, `WelcomeItem.vue`).
- Keep route view files in `src/views` and reusable UI in `src/components`.
- Use camelCase for JS variables/functions and descriptive file names.
- No formatter/linter is currently configured; keep edits minimal, consistent, and readable.

## Testing Guidelines
- No automated test framework is configured yet (`package.json` has no `test` script).
- For now, validate changes by running `pnpm dev`, exercising affected routes/components, and confirming `pnpm build` succeeds.
- If adding tests, prefer Vitest + Vue Test Utils and place specs as `*.spec.js` near source files or under `src/__tests__/`.

## Commit & Pull Request Guidelines
- Git history has no commits yet, so no project-specific commit convention is established.
- Recommended commit format: Conventional Commits (for example `feat: add about page hero`).
- Keep commits focused and atomic; include scope when useful (for example `fix(router): handle missing route`).
- PRs should include: summary, changed paths, local verification steps, and screenshots for UI changes.

## Security & Configuration Tips
- Use the Node version in `package.json` engines: `^20.19.0 || >=22.12.0`.
- Do not commit secrets or local environment files; keep credentials out of source and `public/` assets.

## User Identity & Interaction Rules
- 全程使用中文交流与输出。
- 用户是统计系学生，回答时注重代码思路引导与步骤说明。
- 面对代码题目不做联想或扩展，仅严格回答用户提出的问题。
