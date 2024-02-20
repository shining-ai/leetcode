# local_partを上書きすると分かりづらいので、別変数(owner)を使用
# "@"が2つ以上ある場合に対応するため、rsplitを使用
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        receive_emails = set()
        for email in emails:
            local_part, domain = email.rsplit("@", maxsplit=1)
            owner = local_part.split("+")[0].replace(".", "")
            receive_emails.add(owner + "@" + domain)
        return len(receive_emails)


# ドメインは末尾から検索する形に修正
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        receive_emails = set()
        for email in emails:
            i = len(email) - 1
            while i > 0 and email[i] != "@":
                i -= 1
            domain = email[i:]  # "@"を含む
            local_name = ""
            for c in email[:i]:
                if c == ".":
                    continue
                if c == "+":
                    break
                local_name += c
            receive_emails.add(local_name + domain)
        return len(receive_emails)


# 正規表現で実装
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        receive_mails = set()
        for email in emails:
            regex = re.match(r"([\w\.@]+)\+?.*@(.+)", email)
            local_name = regex.group(1).replace(".", "")
            domain = regex.group(2)
            receive_mails.add(local_name + "@" + domain)
        return len(receive_mails)
