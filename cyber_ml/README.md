# Cyber ML — Log Analysis, Threat Scoring, and Threat Intelligence Integration

**Domain:** SOC Automation, Threat Intelligence  
**Practitioner Level:** IT Security Leader (15+ yrs, Banking)  

## Problem Statement

Security teams need automated log analysis with threat intelligence enrichment. Integration with AbuseIPDB provides real-time IP reputation scoring to prioritize incident response.

## Methodology

1. **Log Analysis**: Keyword-based threat scoring engine for security logs
2. **Threat Intelligence**: AbuseIPDB API v2 integration with configurable cache age
3. **Scoring Rules**: Weighted rule matching (`ABUSEIPDB_HIGH_SCORE=90`, `PORT_SCAN=70`)
4. **Output Formats**: Human-readable summary and raw JSON modes

## Key Concepts

- Threat intelligence enrichment via external APIs
- Rule-based scoring for SOC triage
- API client design with error handling

## References

- AbuseIPDB API v2. https://www.abuseipdb.com/
- MITRE ATT&CK. https://attack.mitre.org/
- Chuvakin & Schmidt (2013). *Logging and Log Management*. Syngress.

## Usage

```bash
python -m cyber_ml.abuseipdb_client 8.8.8.8 --api-key YOUR_KEY
python -m cyber_ml.log_analysis_example --file security.log
```
