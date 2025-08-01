class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        def parse(email):
            local, domain = email.split('@')
            local = local.split('+')[0].replace('.',"")
            return f"{local}@{domain}"
        parsed_emails = map(parse, emails)
        return len(set(parsed_emails))