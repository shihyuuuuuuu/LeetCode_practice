class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        output = set()
        for email in emails:
            split = email.split('@') # [local_name, domain_name]
            # local, domain = email.split('@')
            split[0] = split[0].split('+')[0]
            split[0] = split[0].replace('.', '')
            output.add(split[0] + '@' + split[1])
        return len(output)
