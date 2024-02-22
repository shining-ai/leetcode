class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        receive_mails = set()
        for email in emails:
            local_part, domain = email.rsplit("@", 1)
            local_name = local_part.split("+")[0].replace(".","")
            receive_mails.add(local_name + "@" + domain)
        return len(receive_mails)
