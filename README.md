```markdown
# rule-forwarding

Custom detection rules for IBM QRadar SIEM v7.5.0, focused on Active Directory and Windows Security event monitoring. Rules are mapped to the MITRE ATT&CK framework and tested in a live AWS-hosted QRadar environment.

---

## Purpose

Most out-of-the-box SIEM rules are too broad or too noisy. This repo documents rules that were manually built, tested, and tuned against real Windows/AD event logs — with exact QIDs, offense configurations, and test commands included.

---

## Environment

- IBM QRadar SIEM v7.5.0 (AWS)
- IBM WinCollect 7.3.1
- Windows Server / Active Directory
- Log Source: Microsoft Windows Security Event Log

---

## Rules

| ID | Description | Event ID | Severity | MITRE |
|----|-------------|----------|----------|-------|
| SEC-001 | New user account created in AD | 4720 | 5 | T1136.002 |
| SEC-002 | Member added to administrators group | 4728 | 8 | T1098 |
| SEC-003 | User account permanently deleted | 4726 | 7 | T1531 |
| SEC-004 | Member removed from AD group | 4729/4733 | 6 | T1531 |
| SEC-005 | User account disabled | 4725 | 6 | T1531 |
| SEC-006 | User account enabled | 4722 | 6 | T1098 |
| SEC-007 | User account locked out | 4740 | 7 | T1110 |
| SEC-008 | Password changed or reset | 4723/4724 | 5 | T1098 |
| SEC-009 | Password never expires flag set | 4738 | 7 | T1098 |
| SEC-010 | Successful logon after multiple failures | 4624+4625 | 9 | T1110 |

---

## Structure

```
rule-forwarding/
├── rules/
│   ├── SEC-001|AD New User Account Created
│   ├── SEC-002|User Added to Administrators Group
│   ├── SEC-003 | AD User Account Deleted.json
│   ├── SEC-004 | AD Group Member Removed.json
│   ├── SEC-005 | AD User Account Disabled.json
│   ├── SEC-006 | AD User Account Enabled.json
│   ├── SEC-007 | AD User Account Locked Out.json
│   ├── SEC-008 | AD Password Changed.json
│   ├── SEC-009 | AD Password Never Expires Set.json
│   └── SEC-010|Successful Logon After Multiple Failures.json
├── scripts/
│   └── deploy_rules.py
└── README.md
```

---

## Scripts

| Script | Description |
|--------|-------------|
| `deploy_rules.py` | Deploys rule JSON files to QRadar via API |

---

## Notes

- QID values are environment-specific. Verify via Log Activity → Map Event before deploying.
- All rules tested on QRadar v7.5.0. Behavior may differ on other versions.
- Response Limiter is configured on all rules to reduce noise.

---

## Status

Actively building — more rules being added as they are tested.
```

---

