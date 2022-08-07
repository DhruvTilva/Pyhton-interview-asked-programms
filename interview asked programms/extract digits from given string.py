test_string="jkjl465jkj3k43k3"

res=''.join(filter(lambda i: i.isdigit(), test_string))
print(res)