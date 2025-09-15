# KQL Query & Threat Hunting Repository

![GitHub last commit](https://img.shields.io/github/last-commit/timo-reymann/kql-query-repo)
![GitHub repo size](https://img.shields.io/github/repo-size/timo-reymann/kql-query-repo)
![GitHub license](https://img.shields.io/github/license/timo-reymann/kql-query-repo)

A curated repository of KQL queries and IoCs for threat hunting and detection in Microsoft Sentinel and Microsoft Defender XDR. This project is aimed at Security Engineers, SOC Analysts, and Threat Hunters.

## Table of Contents

- [KQL Query & Threat Hunting Repository](#kql-query--threat-hunting-repository)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Repository Structure](#repository-structure)
  - [Getting Started](#getting-started)
  - [Web Frontend](#web-frontend)
  - [Queries](#queries)
    - [Microsoft Sentinel](#microsoft-sentinel)
    - [Microsoft Defender XDR](#microsoft-defender-xdr)
  - [Contributing](#contributing)
  - [License](#license)

## Introduction

This repository is a collection of Kusto Query Language (KQL) queries and Indicators of Compromise (IoCs) designed to help security professionals detect and hunt for threats within Microsoft's security ecosystem. The queries are organized by product and use case to make them easy to find and use.

## Repository Structure

The repository is organized as follows:

```
.
├── Sentinel/         # Queries for Microsoft Sentinel
├── XDR/              # Queries for Microsoft Defender XDR
│   ├── Defender Advanced Hunting/
│   ├── Email/
│   ├── Endpoints/
│   ├── Identities/
│   └── MDVM/
├── IOC/              # Indicators of Compromise
│   ├── APT/
│   ├── CVE/
│   └── Malware/
├── Frontend/         # Frontend for displaying queries
└── ...
```

## Getting Started

To use these queries, you can either clone this repository or browse the files directly.

```bash
git clone https://github.com/timo-reymann/kql-query-repo.git
```

The queries are in `.kql` files and can be copied and pasted directly into the advanced hunting interface of the respective Microsoft security product.

## Web Frontend

A web frontend is available to search and view all queries in this repository. It can be accessed here:

[https://timosarkar.github.io/kql/](https://timosarkar.github.io/kql/)

## Queries

### Microsoft Sentinel

The `Sentinel/` directory contains queries for use in Microsoft Sentinel. These queries cover a range of detection and hunting scenarios.

[Browse Sentinel Queries](./Sentinel/)

### Microsoft Defender XDR

The `XDR/` directory contains queries for use in Microsoft Defender XDR's advanced hunting. The queries are categorized by the different data sources within Defender XDR.

- [**Defender Advanced Hunting**](./XDR/Defender%20Advanced%20Hunting/): Queries for general advanced hunting.
- [**Email**](./XDR/Email/): Queries for hunting in email data.
- [**Endpoints**](./XDR/Endpoints/): Queries for endpoint data.
- [**Identities**](./XDR/Identities/): Queries for identity data.
- [**MDVM**](./XDR/MDVM/): Queries for Microsoft Defender Vulnerability Management.

## Contributing

Contributions are welcome! If you have a query or IoC that you would like to add, please open a pull request. Please follow the existing directory structure and naming conventions.

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.