# `manager`

## Description

> _Auto-captured from ctrader_spotware reporting DB (Demo environment)._

## Fields

| Column | Type | Nullable | Default | Description |
|--------|------|----------|---------|-------------|
| `manager_id` | bigint | NO |  |  |
| `login` | bigint | NO |  |  |
| `email` | character varying | NO |  |  |
| `name` | character varying | NO |  |  |
| `enabled` | boolean | NO |  |  |
| `deleted` | boolean | NO |  |  |
| `utc_last_update_timestamp` | timestamp without time zone | NO |  |  |
| `region_ids` | ARRAY | NO | '{}'::bigint[] | Allowed regionId for manager |
| `webserv_token` | text | NO | (md5(((random())::text || (clock_timestamp())::text)))::uuid | Token to authorize manager in webserv component |
| `manager_ids` | ARRAY | NO | '{}'::bigint[] |  |
| `specific_group_ids` | ARRAY | NO | '{}'::bigint[] |  |
| `group_mask` | text | YES |  |  |
| `disabled_broker_names` | ARRAY | NO | '{}'::text[] |  |
| `template` | boolean | YES | false |  |
| `create_timestamp` | timestamp without time zone | NO | now() |  |
| `last_login_timestamp` | timestamp without time zone | YES |  |  |

## Sample Data

| `manager_id` | `login` | `email` | `name` | `enabled` | `deleted` | `utc_last_update_timestamp` | `region_ids` | `webserv_token` | `manager_ids` | `specific_group_ids` | `group_mask` | `disabled_broker_names` | `template` | `create_timestamp` | `last_login_timestamp` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1010 | [REDACTED] | [REDACTED] | [REDACTED] | True | False | [REDACTED] | [] | 0a386a4f-02ec-4b43-be61-8721b696def0 | [1015, 1016, 1018, 1020, 1021] | [1024, 1025, 1026, 1027, 1028, 1029, 1030, 1031, 1032, 1033, 1034, 1035, 1036, 1037, 1038, 1039, 1040, 1041, 1042, 1043, 1044, 1045, 1046, 1047, 1048, 1049, 1050, 1051, 1052, 1053, 1054, 1056, 1057, 1058, 1059, 1060, 1061, 1062, 1063, 1066, 1067, 1068, 1069, 1070, 1075, 1076, 1077, 1078, 1079, 1085, 1086, 1087, 1088, 1089, 1090, 1092, 1093, 1095, 1096, 1098, 1099, 1101, 1102, 1103, 1000, 1020, 1021, 1022, 1023] | NULL | [REDACTED] | False | 2023-08-24 07:21:37.205000 | [REDACTED] |
| 1009 | [REDACTED] | [REDACTED] | [REDACTED] | True | True | [REDACTED] | [] | d1f4fd02-ef52-4727-b036-49819c372dd3 | [] | [1000] | NULL | [REDACTED] | False | 2023-08-03 07:34:49.391000 | NULL |
| 1011 | [REDACTED] | [REDACTED] | [REDACTED] | True | False | [REDACTED] | [] | 8c951fb6-53c7-467e-82ec-cc6f8b4bc337 | [] | [1024, 1025, 1026, 1027, 1028, 1029, 1030, 1031, 1032, 1033, 1034, 1035, 1036, 1037, 1038, 1039, 1040, 1041, 1042, 1043, 1044, 1045, 1046, 1047, 1048, 1049, 1050, 1051, 1052, 1053, 1054, 1056, 1057, 1058, 1059, 1060, 1061, 1062, 1063, 1066, 1067, 1068, 1069, 1070, 1075, 1076, 1077, 1078, 1079, 1085, 1086, 1087, 1088, 1089, 1090, 1092, 1093, 1095, 1096, 1098, 1099, 1101, 1102, 1103, 1104, 1000, 1020, 1021, 1022, 1023] | NULL | [REDACTED] | False | 2023-08-24 07:21:37.207000 | NULL |


## Notes

- Source: cTrader Reporting DB (`ctrader_spotware`)
- Access: read-only replica via stunnel → dbapi.ctrader.com:15220
- PII fields redacted with `[REDACTED]`
