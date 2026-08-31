# shhh-graph

A Codex skill for evidence-based scientific figure upgrades through a mandatory live OriginPro connection.

Search keywords: `shhh-graph`, `OriginPro`, `OriginLab`, `Codex skill`, `scientific visualization`, `research figures`, `SCI plotting`.

## What makes it strict

Every plotting task begins with `scripts/origin_gate.py`. The skill continues only after OriginPro responds through COM and completes a LabTalk handshake. Python-only fallback is deliberately disallowed.

## Requirements

- Windows
- A locally installed and registered OriginPro
- Python 3.10+
- `originpro>=1.1.15`

Install the repository as a Codex skill or copy it to `%USERPROFILE%\.codex\skills\shhh-graph`.

```powershell
git clone https://github.com/565721014-art/shhh-graph.git "$env:USERPROFILE\.codex\skills\shhh-graph"
```

The skill includes a 28-case upgrade matrix, evidence-based chart-selection rules, and the user's SCI technology-future palette.

## License

MIT. See [LICENSE](LICENSE).
