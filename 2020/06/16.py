"""
Validate IP Address

Write a function to check whether an input string is a valid IPv4 address or IPv6 address or neither.

IPv4 addresses are canonically represented in dot-decimal notation, which consists of four decimal numbers, each ranging from 0 to 255, separated by dots ("."), e.g.,172.16.254.1;

Besides, leading zeros in the IPv4 is invalid. For example, the address 172.16.254.01 is invalid.

IPv6 addresses are represented as eight groups of four hexadecimal digits, each group representing 16 bits. The groups are separated by colons (":"). For example, the address 2001:0db8:85a3:0000:0000:8a2e:0370:7334 is a valid one. Also, we could omit some leading zeros among four hexadecimal digits and some low-case characters in the address to upper-case ones, so 2001:db8:85a3:0:0:8A2E:0370:7334 is also a valid IPv6 address(Omit leading zeros and using upper cases).

However, we don't replace a consecutive group of zero value with a single empty group using two consecutive colons (::) to pursue simplicity. For example, 2001:0db8:85a3::8A2E:0370:7334 is an invalid IPv6 address.

Besides, extra leading zeros in the IPv6 is also invalid. For example, the address 02001:0db8:85a3:0000:0000:8a2e:0370:7334 is invalid.

 

Example 1:

Input: IP = "172.16.254.1"
Output: "IPv4"
Explanation: This is a valid IPv4 address, return "IPv4".

Example 2:

Input: IP = "2001:0db8:85a3:0:0:8A2E:0370:7334"
Output: "IPv6"
Explanation: This is a valid IPv6 address, return "IPv6".

Example 3:

Input: IP = "256.256.256.256"
Output: "Neither"
Explanation: This is neither a IPv4 address nor a IPv6 address.

 

Constraints:

    IP consists only of English letters, digits and the characters "." and ":".
"""

class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        ipv4 = IP.split('.')
        if len(ipv4) == 4:
            for octect in ipv4:
                try: # simple check 0-255
                    if int(octect) >= 0 and int(octect) <= 255 and len(octect) >=1 and len(octect) <= 3:
                        if len(octect) == 2 and int(octect) < 10: # leading char on 2
                            return 'Neither'
                        if len(octect) == 3 and int(octect) < 100: # leading char on 3
                            return 'Neither'
                        pass
                    else: # fails simple check
                        return 'Neither'
                except: # casting error
                    return 'Neither'
            return 'IPv4'
        
        ipv6 = IP.split(':')
        if len(ipv6) == 8:
            for word in ipv6:
                try: # simple check 0-65535
                    if int(word, 16) >= 0 and int(word, 16) <= 65535 and len(word) >= 1 and len(word) <= 4:
                        if len(word) == 2 and int(word, 16) < 16 and word[0] != '0': # leading char on 2
                            return 'Neither'
                        if len(word) == 3 and int(word, 16) < 256 and word[0] != '0': # leading char on 3
                            return 'Neither'
                        if len(word) == 4 and int(word, 16) < 4096 and word[0] != '0':# leading char on 4
                            return 'Neither'
                        pass
                    else: # fails simple check
                        return 'Neither'
                except: # casting error
                    return 'Neither'
            return 'IPv6'
        else:
            return 'Neither'
