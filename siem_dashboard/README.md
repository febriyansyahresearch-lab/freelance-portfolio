# SIEM Dashboard — Log Parsing and Threat Reporting

**Domain:** SOC Operations, SIEM Engineering  
**Practitioner Level:** IT Security Leader (15+ yrs, Banking)  

## Problem Statement

Security Operations Centers (SOCs) process millions of log events daily. Automated log parsing with regex-based pattern matching and rule-based threat scoring enables triage at machine speed.

## Methodology

1. **Log Parsing**: Regex pattern capture (timestamp, SRC_IP, DST_IP, ACTION, REASON)
2. **Threat Scoring**: Rule-based engine with weighted threat categories:
   - AbuseIPDB high-confidence indicators (score: 90)
   - Port scan detection (score: 70)
   - Blocked action scoring (score: 50)
3. **Reporting**: HTML/JSON threat report generation
4. **CLI Tools**: `--file`, `--verbose`, `--output` flags for flexible operation

## Key Concepts

- Regex-based log normalization
- Indicator-based threat scoring
- SOC triage workflow automation

## References

- Chuvakin & Schmidt (2013). *Logging and Log Management*. Syngress.
- NIST SP 800-92. Guide to Computer Security Log Management.

## Usage

```bash
python -m siem_dashboard.src.app --file sample.log --verbose
```
