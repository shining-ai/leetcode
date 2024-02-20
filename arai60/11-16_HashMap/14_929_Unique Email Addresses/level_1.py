# 初見で思いついたもの
# splitで分割
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        receive_emails = set()
        for email in emails:
            local_name, domain = email.split("@")
            local_name = local_name.split("+")[0].replace(".", "")
            receive_emails.add(local_name + "@" + domain)
        return len(receive_emails)


# 解答を見て実装
# 一文字ずつ見ていく
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        receive_emails = set()
        for email in emails:
            local_name = ""
            for i, c in enumerate(email):
                if c == ".":
                    continue
                if c == "+" or c == "@":
                    break
                local_name += c
            while i < len(email) and email[i] != "@":
                i += 1
            domain = email[i:]
            receive_emails.add(local_name + domain)
        return len(receive_emails)
