def getprotospecs() -> list:
    speclist = [
        {
            "id": 1,
            "hex": "0x00",
            "protoNumber": "0",
            "protoName": "HOPOPT",
            "rfc": "IPv6 Hop-by-Hop Option"
        },
        {
            "id": 2,
            "hex": "0x01",
            "protoNumber": "1",
            "protoName": "ICMP",
            "rfc": "Internet Control Message Protocol"
        },
        {
            "id": 3,
            "hex": "0x02",
            "protoNumber": "2",
            "protoName": "IGMP",
            "rfc": "Internet Group Management Protocol"
        },
        {
            "id": 4,
            "hex": "0x03",
            "protoNumber": "3",
            "protoName": "GGP",
            "rfc": "Gateway-to-Gateway Protocol"
        },
        {
            "id": 5,
            "hex": "0x04",
            "protoNumber": "4",
            "protoName": "IP-in-IP",
            "rfc": "IP in IP (encapsulation)"
        },
        {
            "id": 6,
            "hex": "0x05",
            "protoNumber": "5",
            "protoName": "ST",
            "rfc": "Internet Stream Protocol"
        },
        {
            "id": 7,
            "hex": "0x06",
            "protoNumber": "6",
            "protoName": "TCP",
            "rfc": "Transmission Control Protocol"
        },
        {
            "id": 8,
            "hex": "0x07",
            "protoNumber": "7",
            "protoName": "CBT",
            "rfc": "Core-based trees"
        },
        {
            "id": 9,
            "hex": "0x08",
            "protoNumber": "8",
            "protoName": "EGP",
            "rfc": "Exterior Gateway Protocol"
        },
        {
            "id": 10,
            "hex": "0x09",
            "protoNumber": "9",
            "protoName": "IGP",
            "rfc": "Interior Gateway Protocol (any private interior gateway (used by Cisco for their IGRP))"
        },
        {
            "id": 11,
            "hex": "0x0A",
            "protoNumber": "10",
            "protoName": "BBN-RCC-MON",
            "rfc": "BBN RCC Monitoring"
        },
        {
            "id": 12,
            "hex": "0x0B",
            "protoNumber": "11",
            "protoName": "NVP-II",
            "rfc": "Network Voice Protocol"
        },
        {
            "id": 13,
            "hex": "0x0C",
            "protoNumber": "12",
            "protoName": "PUP",
            "rfc": "Xerox PUP"
        },
        {
            "id": 14,
            "hex": "0x0D",
            "protoNumber": "13",
            "protoName": "ARGUS",
            "rfc": "ARGUS"
        },
        {
            "id": 15,
            "hex": "0x0E",
            "protoNumber": "14",
            "protoName": "EMCON",
            "rfc": "EMCON"
        },
        {
            "id": 16,
            "hex": "0x0F",
            "protoNumber": "15",
            "protoName": "XNET",
            "rfc": "Cross Net Debugger"
        },
        {
            "id": 17,
            "hex": "0x10",
            "protoNumber": "16",
            "protoName": "CHAOS",
            "rfc": "Chaos"
        },
        {
            "id": 18,
            "hex": "0x11",
            "protoNumber": "17",
            "protoName": "UDP",
            "rfc": "User Datagram Protocol"
        },
        {
            "id": 19,
            "hex": "0x12",
            "protoNumber": "18",
            "protoName": "MUX",
            "rfc": "Multiplexing"
        },
        {
            "id": 20,
            "hex": "0x13",
            "protoNumber": "19",
            "protoName": "DCN-MEAS",
            "rfc": "DCN Measurement Subsystems"
        },
        {
            "id": 21,
            "hex": "0x14",
            "protoNumber": "20",
            "protoName": "HMP",
            "rfc": "Host Monitoring Protocol"
        },
        {
            "id": 22,
            "hex": "0x15",
            "protoNumber": "21",
            "protoName": "PRM",
            "rfc": "Packet Radio Measurement"
        },
        {
            "id": 23,
            "hex": "0x16",
            "protoNumber": "22",
            "protoName": "XNS-IDP",
            "rfc": "XEROX NS IDP"
        },
        {
            "id": 24,
            "hex": "0x17",
            "protoNumber": "23",
            "protoName": "TRUNK-1",
            "rfc": "Trunk-1"
        },
        {
            "id": 25,
            "hex": "0x18",
            "protoNumber": "24",
            "protoName": "TRUNK-2",
            "rfc": "Trunk-2"
        },
        {
            "id": 26,
            "hex": "0x19",
            "protoNumber": "25",
            "protoName": "LEAF-1",
            "rfc": "Leaf-1"
        },
        {
            "id": 27,
            "hex": "0x1A",
            "protoNumber": "26",
            "protoName": "LEAF-2",
            "rfc": "Leaf-2"
        },
        {
            "id": 28,
            "hex": "0x1B",
            "protoNumber": "27",
            "protoName": "RDP",
            "rfc": "Reliable Data Protocol"
        },
        {
            "id": 29,
            "hex": "0x1C",
            "protoNumber": "28",
            "protoName": "IRTP",
            "rfc": "Internet Reliable Transaction Protocol"
        },
        {
            "id": 30,
            "hex": "0x1D",
            "protoNumber": "29",
            "protoName": "ISO-TP4",
            "rfc": "ISO Transport Protocol Class 4"
        },
        {
            "id": 31,
            "hex": "0x1E",
            "protoNumber": "30",
            "protoName": "NETBLT",
            "rfc": "Bulk Data Transfer Protocol"
        },
        {
            "id": 32,
            "hex": "0x1F",
            "protoNumber": "31",
            "protoName": "MFE-NSP",
            "rfc": "MFE Network Services Protocol"
        },
        {
            "id": 33,
            "hex": "0x20",
            "protoNumber": "32",
            "protoName": "MERIT-INP",
            "rfc": "MERIT Internodal Protocol"
        },
        {
            "id": 34,
            "hex": "0x21",
            "protoNumber": "33",
            "protoName": "DCCP",
            "rfc": "Datagram Congestion Control Protocol"
        },
        {
            "id": 35,
            "hex": "0x22",
            "protoNumber": "34",
            "protoName": "3PC",
            "rfc": "Third Party Connect Protocol"
        },
        {
            "id": 36,
            "hex": "0x23",
            "protoNumber": "35",
            "protoName": "IDPR",
            "rfc": "Inter-Domain Policy Routing Protocol"
        },
        {
            "id": 37,
            "hex": "0x24",
            "protoNumber": "36",
            "protoName": "XTP",
            "rfc": "Xpress Transport Protocol"
        },
        {
            "id": 38,
            "hex": "0x25",
            "protoNumber": "37",
            "protoName": "DDP",
            "rfc": "Datagram Delivery Protocol"
        },
        {
            "id": 39,
            "hex": "0x26",
            "protoNumber": "38",
            "protoName": "IDPR-CMTP",
            "rfc": "IDPR Control Message Transport Protocol"
        },
        {
            "id": 40,
            "hex": "0x27",
            "protoNumber": "39",
            "protoName": "TP++",
            "rfc": "TP++ Transport Protocol"
        },
        {
            "id": 41,
            "hex": "0x28",
            "protoNumber": "40",
            "protoName": "IL",
            "rfc": "IL Transport Protocol"
        },
        {
            "id": 42,
            "hex": "0x29",
            "protoNumber": "41",
            "protoName": "IPv6",
            "rfc": "IPv6 Encapsulation"
        },
        {
            "id": 43,
            "hex": "0x2A",
            "protoNumber": "42",
            "protoName": "SDRP",
            "rfc": "Source Demand Routing Protocol"
        },
        {
            "id": 44,
            "hex": "0x2B",
            "protoNumber": "43",
            "protoName": "IPv6-Route",
            "rfc": "Routing Header for IPv6"
        },
        {
            "id": 45,
            "hex": "0x2C",
            "protoNumber": "44",
            "protoName": "IPv6-Frag",
            "rfc": "Fragment Header for IPv6"
        },
        {
            "id": 46,
            "hex": "0x2D",
            "protoNumber": "45",
            "protoName": "IDRP",
            "rfc": "Inter-Domain Routing Protocol"
        },
        {
            "id": 47,
            "hex": "0x2E",
            "protoNumber": "46",
            "protoName": "RSVP",
            "rfc": "Resource Reservation Protocol"
        },
        {
            "id": 48,
            "hex": "0x2F",
            "protoNumber": "47",
            "protoName": "GRE",
            "rfc": "Generic Routing Encapsulation"
        },
        {
            "id": 49,
            "hex": "0x30",
            "protoNumber": "48",
            "protoName": "DSR",
            "rfc": "Dynamic Source Routing Protocol"
        },
        {
            "id": 50,
            "hex": "0x31",
            "protoNumber": "49",
            "protoName": "BNA",
            "rfc": "Burroughs Network Architecture"
        },
        {
            "id": 51,
            "hex": "0x32",
            "protoNumber": "50",
            "protoName": "ESP",
            "rfc": "Encapsulating Security Payload"
        },
        {
            "id": 52,
            "hex": "0x33",
            "protoNumber": "51",
            "protoName": "AH",
            "rfc": "Authentication Header"
        },
        {
            "id": 53,
            "hex": "0x34",
            "protoNumber": "52",
            "protoName": "I-NLSP",
            "rfc": "Integrated Net Layer Security Protocol"
        },
        {
            "id": 54,
            "hex": "0x35",
            "protoNumber": "53",
            "protoName": "SwIPe",
            "rfc": "SwIPe"
        },
        {
            "id": 55,
            "hex": "0x36",
            "protoNumber": "54",
            "protoName": "NARP",
            "rfc": "NBMA Address Resolution Protocol"
        },
        {
            "id": 56,
            "hex": "0x37",
            "protoNumber": "55",
            "protoName": "MOBILE",
            "rfc": "IP Mobility (Min Encap)"
        },
        {
            "id": 57,
            "hex": "0x38",
            "protoNumber": "56",
            "protoName": "TLSP",
            "rfc": "Transport Layer Security Protocol (using Kryptonet key management)"
        },
        {
            "id": 58,
            "hex": "0x39",
            "protoNumber": "57",
            "protoName": "SKIP",
            "rfc": "Simple Key-Management for Internet Protocol"
        },
        {
            "id": 59,
            "hex": "0x3A",
            "protoNumber": "58",
            "protoName": "IPv6-ICMP",
            "rfc": "ICMP for IPv6"
        },
        {
            "id": 60,
            "hex": "0x3B",
            "protoNumber": "59",
            "protoName": "IPv6-NoNxt",
            "rfc": "No Next Header for IPv6"
        },
        {
            "id": 61,
            "hex": "0x3C",
            "protoNumber": "60",
            "protoName": "IPv6-Opts",
            "rfc": "Destination Options for IPv6"
        },
        {
            "id": 62,
            "hex": "0x3D",
            "protoNumber": "61",
            "protoName": "",
            "rfc": "Any host internal protocol"
        },
        {
            "id": 63,
            "hex": "0x3E",
            "protoNumber": "62",
            "protoName": "CFTP",
            "rfc": "CFTP"
        },
        {
            "id": 64,
            "hex": "0x3F",
            "protoNumber": "63",
            "protoName": "",
            "rfc": "Any local network"
        },
        {
            "id": 65,
            "hex": "0x40",
            "protoNumber": "64",
            "protoName": "SAT-EXPAK",
            "rfc": "SATNET and Backroom EXPAK"
        },
        {
            "id": 66,
            "hex": "0x41",
            "protoNumber": "65",
            "protoName": "KRYPTOLAN",
            "rfc": "Kryptolan"
        },
        {
            "id": 67,
            "hex": "0x42",
            "protoNumber": "66",
            "protoName": "RVD",
            "rfc": "MIT Remote Virtual Disk Protocol"
        },
        {
            "id": 68,
            "hex": "0x43",
            "protoNumber": "67",
            "protoName": "IPPC",
            "rfc": "Internet Pluribus Packet Core"
        },
        {
            "id": 69,
            "hex": "0x44",
            "protoNumber": "68",
            "protoName": "",
            "rfc": "Any distributed file system"
        },
        {
            "id": 70,
            "hex": "0x45",
            "protoNumber": "69",
            "protoName": "SAT-MON",
            "rfc": "SATNET Monitoring"
        },
        {
            "id": 71,
            "hex": "0x46",
            "protoNumber": "70",
            "protoName": "VISA",
            "rfc": "VISA Protocol"
        },
        {
            "id": 72,
            "hex": "0x47",
            "protoNumber": "71",
            "protoName": "IPCU",
            "rfc": "Internet Packet Core Utility"
        },
        {
            "id": 73,
            "hex": "0x48",
            "protoNumber": "72",
            "protoName": "CPNX",
            "rfc": "Computer Protocol Network Executive"
        },
        {
            "id": 74,
            "hex": "0x49",
            "protoNumber": "73",
            "protoName": "CPHB",
            "rfc": "Computer Protocol Heart Beat"
        },
        {
            "id": 75,
            "hex": "0x4A",
            "protoNumber": "74",
            "protoName": "WSN",
            "rfc": "Wang Span Network"
        },
        {
            "id": 76,
            "hex": "0x4B",
            "protoNumber": "75",
            "protoName": "PVP",
            "rfc": "Packet Video Protocol"
        },
        {
            "id": 77,
            "hex": "0x4C",
            "protoNumber": "76",
            "protoName": "BR-SAT-MON",
            "rfc": "Backroom SATNET Monitoring"
        },
        {
            "id": 78,
            "hex": "0x4D",
            "protoNumber": "77",
            "protoName": "SUN-ND",
            "rfc": "SUN ND PROTOCOL-Temporary"
        },
        {
            "id": 79,
            "hex": "0x4E",
            "protoNumber": "78",
            "protoName": "WB-MON",
            "rfc": "WIDEBAND Monitoring"
        },
        {
            "id": 80,
            "hex": "0x4F",
            "protoNumber": "79",
            "protoName": "WB-EXPAK",
            "rfc": "WIDEBAND EXPAK"
        },
        {
            "id": 81,
            "hex": "0x50",
            "protoNumber": "80",
            "protoName": "ISO-IP",
            "rfc": "International Organization for Standardization Internet Protocol"
        },
        {
            "id": 82,
            "hex": "0x51",
            "protoNumber": "81",
            "protoName": "VMTP",
            "rfc": "Versatile Message Transaction Protocol"
        },
        {
            "id": 83,
            "hex": "0x52",
            "protoNumber": "82",
            "protoName": "SECURE-VMTP",
            "rfc": "Secure Versatile Message Transaction Protocol"
        },
        {
            "id": 84,
            "hex": "0x53",
            "protoNumber": "83",
            "protoName": "VINES",
            "rfc": "VINES"
        },
        {
            "id": 85,
            "hex": "0x54",
            "protoNumber": "84",
            "protoName": "TTP",
            "rfc": "TTP"
        },
        {
            "id": 86,
            "hex": "0x54",
            "protoNumber": "84",
            "protoName": "IPTM",
            "rfc": "Internet Protocol Traffic Manager"
        },
        {
            "id": 87,
            "hex": "0x55",
            "protoNumber": "85",
            "protoName": "NSFNET-IGP",
            "rfc": "NSFNET-IGP"
        },
        {
            "id": 88,
            "hex": "0x56",
            "protoNumber": "86",
            "protoName": "DGP",
            "rfc": "Dissimilar Gateway Protocol"
        },
        {
            "id": 89,
            "hex": "0x57",
            "protoNumber": "87",
            "protoName": "TCF",
            "rfc": "TCF"
        },
        {
            "id": 90,
            "hex": "0x58",
            "protoNumber": "88",
            "protoName": "EIGRP",
            "rfc": "EIGRP"
        },
        {
            "id": 91,
            "hex": "0x59",
            "protoNumber": "89",
            "protoName": "OSPF",
            "rfc": "Open Shortest Path First"
        },
        {
            "id": 92,
            "hex": "0x5A",
            "protoNumber": "90",
            "protoName": "Sprite-RPC",
            "rfc": "Sprite RPC Protocol"
        },
        {
            "id": 93,
            "hex": "0x5B",
            "protoNumber": "91",
            "protoName": "LARP",
            "rfc": "Locus Address Resolution Protocol"
        },
        {
            "id": 94,
            "hex": "0x5C",
            "protoNumber": "92",
            "protoName": "MTP",
            "rfc": "Multicast Transport Protocol"
        },
        {
            "id": 95,
            "hex": "0x5D",
            "protoNumber": "93",
            "protoName": "AX.25",
            "rfc": "AX.25"
        },
        {
            "id": 96,
            "hex": "0x5E",
            "protoNumber": "94",
            "protoName": "OS",
            "rfc": "KA9Q NOS compatible IP over IP tunneling"
        },
        {
            "id": 97,
            "hex": "0x5F",
            "protoNumber": "95",
            "protoName": "MICP",
            "rfc": "Mobile Internetworking Control Protocol"
        },
        {
            "id": 98,
            "hex": "0x60",
            "protoNumber": "96",
            "protoName": "SCC-SP",
            "rfc": "Semaphore Communications Sec. Pro"
        },
        {
            "id": 99,
            "hex": "0x61",
            "protoNumber": "97",
            "protoName": "ETHERIP",
            "rfc": "Ethernet-within-IP Encapsulation"
        },
        {
            "id": 100,
            "hex": "0x62",
            "protoNumber": "98",
            "protoName": "ENCAP",
            "rfc": "Encapsulation Header"
        },
        {
            "id": 101,
            "hex": "0x63",
            "protoNumber": "99",
            "protoName": "",
            "rfc": "Any private encryption scheme"
        },
        {
            "id": 102,
            "hex": "0x64",
            "protoNumber": "100",
            "protoName": "GMTP",
            "rfc": "GMTP"
        },
        {
            "id": 103,
            "hex": "0x65",
            "protoNumber": "101",
            "protoName": "IFMP",
            "rfc": "Ipsilon Flow Management Protocol"
        },
        {
            "id": 104,
            "hex": "0x66",
            "protoNumber": "102",
            "protoName": "PNNI",
            "rfc": "PNNI over IP"
        },
        {
            "id": 105,
            "hex": "0x67",
            "protoNumber": "103",
            "protoName": "PIM",
            "rfc": "Protocol Independent Multicast"
        },
        {
            "id": 106,
            "hex": "0x68",
            "protoNumber": "104",
            "protoName": "ARIS",
            "rfc": "IBM's ARIS (Aggregate Route IP Switching) Protocol"
        },
        {
            "id": 107,
            "hex": "0x69",
            "protoNumber": "105",
            "protoName": "SCPS",
            "rfc": "SCPS (Space Communications Protocol Standards)"
        },
        {
            "id": 108,
            "hex": "0x6A",
            "protoNumber": "106",
            "protoName": "QNX",
            "rfc": "QNX"
        },
        {
            "id": 109,
            "hex": "0x6B",
            "protoNumber": "107",
            "protoName": "A/N",
            "rfc": "Active Networks"
        },
        {
            "id": 110,
            "hex": "0x6C",
            "protoNumber": "108",
            "protoName": "IPComp",
            "rfc": "IP Payload Compression Protocol"
        },
        {
            "id": 111,
            "hex": "0x6D",
            "protoNumber": "109",
            "protoName": "SNP",
            "rfc": "Sitara Networks Protocol"
        },
        {
            "id": 112,
            "hex": "0x6E",
            "protoNumber": "110",
            "protoName": "Compaq-Peer",
            "rfc": "Compaq Peer Protocol"
        },
        {
            "id": 113,
            "hex": "0x6F",
            "protoNumber": "111",
            "protoName": "IPX-in-IP",
            "rfc": "IPX in IP"
        },
        {
            "id": 114,
            "hex": "0x70",
            "protoNumber": "112",
            "protoName": "VRRP",
            "rfc": "Virtual Router Redundancy Protocol, Common Address Redundancy Protocol (not IANA assigned)"
        },
        {
            "id": 115,
            "hex": "0x71",
            "protoNumber": "113",
            "protoName": "PGM",
            "rfc": "PGM Reliable Transport Protocol"
        },
        {
            "id": 116,
            "hex": "0x72",
            "protoNumber": "114",
            "protoName": "",
            "rfc": "Any 0-hop protocol"
        },
        {
            "id": 117,
            "hex": "0x73",
            "protoNumber": "115",
            "protoName": "L2TP",
            "rfc": "Layer Two Tunneling Protocol Version 3"
        },
        {
            "id": 118,
            "hex": "0x74",
            "protoNumber": "116",
            "protoName": "DDX",
            "rfc": "D-II Data Exchange (DDX)"
        },
        {
            "id": 119,
            "hex": "0x75",
            "protoNumber": "117",
            "protoName": "IATP",
            "rfc": "Interactive Agent Transfer Protocol"
        },
        {
            "id": 120,
            "hex": "0x76",
            "protoNumber": "118",
            "protoName": "STP",
            "rfc": "Schedule Transfer Protocol"
        },
        {
            "id": 121,
            "hex": "0x77",
            "protoNumber": "119",
            "protoName": "SRP",
            "rfc": "SpectraLink Radio Protocol"
        },
        {
            "id": 122,
            "hex": "0x78",
            "protoNumber": "120",
            "protoName": "UTI",
            "rfc": "Universal Transport Interface Protocol"
        },
        {
            "id": 123,
            "hex": "0x79",
            "protoNumber": "121",
            "protoName": "SMP",
            "rfc": "Simple Message Protocol"
        },
        {
            "id": 124,
            "hex": "0x7A",
            "protoNumber": "122",
            "protoName": "SM",
            "rfc": "Simple Multicast Protocol"
        },
        {
            "id": 125,
            "hex": "0x7B",
            "protoNumber": "123",
            "protoName": "PTP",
            "rfc": "Performance Transparency Protocol"
        },
        {
            "id": 126,
            "hex": "0x7C",
            "protoNumber": "124",
            "protoName": "IS-IS over IPv4",
            "rfc": "Intermediate System to Intermediate System (IS-IS) Protocol over IPv4"
        },
        {
            "id": 127,
            "hex": "0x7D",
            "protoNumber": "125",
            "protoName": "FIRE",
            "rfc": "Flexible Intra-AS Routing Environment"
        },
        {
            "id": 128,
            "hex": "0x7E",
            "protoNumber": "126",
            "protoName": "CRTP",
            "rfc": "Combat Radio Transport Protocol"
        },
        {
            "id": 129,
            "hex": "0x7F",
            "protoNumber": "127",
            "protoName": "CRUDP",
            "rfc": "Combat Radio User Datagram"
        },
        {
            "id": 130,
            "hex": "0x80",
            "protoNumber": "128",
            "protoName": "SSCOPMCE",
            "rfc": "Service-Specific Connection-Oriented Protocol in a Multilink and Connectionless Environment"
        },
        {
            "id": 131,
            "hex": "0x81",
            "protoNumber": "129",
            "protoName": "IPLT",
            "rfc": ""
        },
        {
            "id": 132,
            "hex": "0x82",
            "protoNumber": "130",
            "protoName": "SPS",
            "rfc": "Secure Packet Shield"
        },
        {
            "id": 133,
            "hex": "0x83",
            "protoNumber": "131",
            "protoName": "PIPE",
            "rfc": "Private IP Encapsulation within IP"
        },
        {
            "id": 134,
            "hex": "0x84",
            "protoNumber": "132",
            "protoName": "SCTP",
            "rfc": "Stream Control Transmission Protocol"
        },
        {
            "id": 135,
            "hex": "0x85",
            "protoNumber": "133",
            "protoName": "FC",
            "rfc": "Fibre Channel"
        },
        {
            "id": 136,
            "hex": "0x86",
            "protoNumber": "134",
            "protoName": "RSVP-E2E-IGNORE",
            "rfc": "Reservation Protocol (RSVP) End-to-End Ignore"
        },
        {
            "id": 137,
            "hex": "0x87",
            "protoNumber": "135",
            "protoName": "Mobility Header",
            "rfc": "Mobility Extension Header for IPv6"
        },
        {
            "id": 138,
            "hex": "0x88",
            "protoNumber": "136",
            "protoName": "UDPLite",
            "rfc": "Lightweight User Datagram Protocol"
        },
        {
            "id": 139,
            "hex": "0x89",
            "protoNumber": "137",
            "protoName": "MPLS-in-IP",
            "rfc": "Multiprotocol Label Switching Encapsulated in IP"
        },
        {
            "id": 140,
            "hex": "0x8A",
            "protoNumber": "138",
            "protoName": "manet",
            "rfc": "MANET Protocols"
        },
        {
            "id": 141,
            "hex": "0x8B",
            "protoNumber": "139",
            "protoName": "HIP",
            "rfc": "Host Identity Protocol"
        },
        {
            "id": 142,
            "hex": "0x8C",
            "protoNumber": "140",
            "protoName": "Shim6",
            "rfc": "Site Multihoming by IPv6 Intermediation"
        },
        {
            "id": 143,
            "hex": "0x8D",
            "protoNumber": "141",
            "protoName": "WESP",
            "rfc": "Wrapped Encapsulating Security Payload"
        },
        {
            "id": 144,
            "hex": "0x8E",
            "protoNumber": "142",
            "protoName": "ROHC",
            "rfc": "Robust Header Compression"
        },
        {
            "id": 145,
            "hex": "0x8F",
            "protoNumber": "143",
            "protoName": "Ethernet",
            "rfc": "IPv6 Segment Routing (TEMPORARY - registered 2020-01-31, expires 2021-01-31)"
        },
        {
            "id": 146,
            "hex": "0x90-0xFC",
            "protoNumber": "144-252",
            "protoName": "Unassigned",
            "rfc": ""
        },
        {
            "id": 147,
            "hex": "0xFD-0xFE",
            "protoNumber": "253-254",
            "protoName": "Use for experimentation and testing",
            "rfc": "RFC 3692"
        },
        {
            "id": 148,
            "hex": "0xFF",
            "protoNumber": "255",
            "protoName": "Reserved",
            "rfc": ""
        }
    ]
    return speclist


def getprotobynumber(number: int) -> str:
    speclist = getprotospecs()
    for spec in speclist:
        if int(spec['protoNumber']) == number:
            return spec['protoName']
    return "Unassigned"
