def solve_1(emails):
    ans = set()

    for email in emails:
        local_name, domain_name = email.split("@")
        local_name = local_name.split("+")[0].replace(".", "")
        ans.add(local_name + "@" + domain_name)

    return len(ans)


if __name__ == "__main__":
    emails = [
        "test.email+alex@leetcode.com",
        "test.e.mail+bob.cathy@leetcode.com",
        "testemail+david@lee.tcode.com",
    ]

    print(solve_1(emails))
