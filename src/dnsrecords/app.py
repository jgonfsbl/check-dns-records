#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# pylint: disable=W0102,E0712,C0103

""" DNS Records """

__updated__ = "2024-04-28 01:36:53"

import dns.resolver
import config


fich_with_domains = config.FICH_WITH_DOMAINS


def get_nameservers(domain: str) -> list:
    """Get IP addresses of nameservers for a specific domain."""
    ns_ips = []
    try:
        # First resolve the NS records to get the nameserver domains.
        nsquery = dns.resolver.resolve(domain, "NS")
        for ns in nsquery:
            # Resolve each nameserver domain to get its IP address.
            ns_ip_query = dns.resolver.resolve(ns.target, "A")
            ns_ips.extend([ip.address for ip in ns_ip_query])
    except Exception as e:
        print(f"Error resolving nameservers for {domain}: {e}")
    return ns_ips


def main() -> None:
    """Main function to resolve A and TXT records for a list of domains."""

    with open(fich_with_domains, "r") as f:
        list_of_domains = f.read().splitlines()

    for domain in list_of_domains:

        # Identify IP addresses of nameservers for the domain
        domain_ns = get_nameservers(domain)
        print(f"Processing domain {domain} with nameservers: {domain_ns}\n")

        query = dns.resolver.Resolver()
        query.timeout = 1
        query.nameservers = domain_ns

        # Resolve A record
        try:
            a_response = query.resolve(domain, "A")
            for rdata in a_response:
                print(f"A record for {domain}: {rdata}")
        except Exception as e:
            print(f"Failed to resolve A record for {domain}: {e}")

        # Resolve TXT record
        try:
            txt_response = query.resolve(domain, "TXT")
            for rdata in txt_response:
                print(f"TXT record for {domain}: {rdata}")
        except Exception as e:
            print(f"Failed to resolve TXT record for {domain}: {e}")

        print("\n")


if __name__ == "__main__":
    main()
