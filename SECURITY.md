# Security Policy for gh-auto-follow

## Supported Versions

Use this section to tell people about which versions of your project are
currently being supported with security updates.

| Version | Supported          |
| ------- | ------------------ |
| 3.1.3(python)   | :white_check_mark: |

## Reporting a Vulnerability

Preferred way to report a security issue:
- Open a private GitHub Security Advisory for this repository: https://github.com/vinit105/gh-auto-follow/security/advisories/new
- If you cannot use GitHub Security Advisories, open a new issue in this repository and mark it "security" (do NOT include proof-of-concept details publicly) or contact the repository owner via their GitHub profile: https://github.com/vinit105

What to include in your report:
- A short, clear summary of the issue.
- Affected version(s) or commit(s).
- Detailed reproduction steps and environment (OS, Python version, etc.).
- Proof-of-concept (PoC) or exploit code, if available — provide this privately.
- Expected vs actual behavior and potential impact (data leakage, account compromise, etc.).
- Any suggested mitigations or fixes.
- Whether you request coordination for CVE assignment and whether you want to be credited.

Please avoid posting sensitive information (tokens, private keys, or secrets) in public issues.

## Triage and Response

- Acknowledgement: We'll acknowledge receipt of valid reports within 72 hours.
- Triage: We'll triage and estimate severity within 7 days of acknowledgement.
- Fixes: We'll aim to provide a fix or mitigation, or an actionable plan, within 30 days for confirmed vulnerabilities affecting supported versions. If an immediate patch is not possible, we will provide workarounds and a clear timeline.
- Updates: We'll provide status updates at least once per week until resolved.
- Disclosure: We'll coordinate public disclosure with the reporter and will credit researchers unless they request anonymity.

## Patch Releases and Advisories

- Security fixes will be published as releases and documented in a GitHub Security Advisory for affected versions.
- When appropriate, we will request a CVE and include CVE information in the advisory and release notes.

## Scope & Severity

- The policy covers vulnerabilities in the project code, workflows, and documentation that could lead to account compromise, credential leakage, or unwanted follower/following actions.
- Third-party dependencies (Python packages / GitHub Actions) are in scope; please include dependency information in reports.

## Secure Defaults and Recommendations

From the repository README and best practices:

- Tokens and Scopes
  - The bot requires only these scopes:
    - read:user
    - user:follow
  - Do NOT grant repo, admin, or unnecessary scopes.
  - Consider using fine-grained tokens where possible. If using classic tokens, keep scopes minimal.
  - Treat tokens as secrets — never commit tokens or other secrets to the repository.

- Storing Secrets
  - Store tokens in GitHub Actions Secrets (Settings → Secrets and variables → Actions).
  - Name secrets clearly (e.g., GH_TOKEN, GH_USERNAME).
  - Rotate tokens regularly and immediately revoke leaked tokens.

- GitHub Actions
  - Limit workflow permissions to the minimum required.
  - Do not run untrusted community workflows that could exfiltrate secrets.
  - Review cron schedules and consider reducing frequency to limit exposure.

- Code & Dependencies
  - Keep Python runtime and dependencies updated (Python 3.10+ recommended).
  - Use automated dependency scanning (Dependabot, GitHub Dependabot Alerts).
  - Validate inputs and API responses where applicable.

## Handling Sensitive Data Leaks

If you believe a secret (token) has been leaked:
1. Revoke the token immediately via your GitHub settings.
2. Rotate to a new token and update the repository secret.
3. Report the incident privately via the Security Advisory or directly to the repository owner.
4. Provide timeline and scope of exposure in the report so we can assess impact.

## Credit and Safe Harbor

- Reporters who follow responsible disclosure practices will be credited in advisories and release notes, unless they request anonymity.
- We appreciate responsible disclosures and will not initiate legal action against good-faith security researchers following this policy.

## Contact

- Preferred: GitHub Security Advisory for this repository:
  https://github.com/vinit105/gh-auto-follow/security/advisories/new
- Alternative: open an issue marked "security" or contact the repository owner via https://github.com/vinit105

---

Thank you for helping keep gh-auto-follow secure. If you're reporting an issue, please follow the guidance above and include reproduction steps and PoC privately.
```
