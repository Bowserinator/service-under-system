USER_DATA_DIR = "accounts/"


def write_htop(file: str, secret: str, count: int, customer_name: str, reactivation_token: str):
    """
    Write to a HTOP file
    :param file: Path to .htop file
    :param secret: Secret file
    :param count: Activation key count
    :param customer_name: Customer name
    :param reactivation_token: Reactivation token
    :throws IOError: Invalid secret file
    """
    f = open(file, "w")
    f.write(secret + "\n")        # HOTP secret
    f.write(str(count) + "\n")    # Activation key count
    f.write(customer_name + "\n") # Customer name (your service provider)
    f.write(reactivation_token)   # Reactivation token
    f.close()


def read_htop(file: str):
    """
    Read a HTOP file
    :param file: Path to .htop file
    :return: secret, count, customer_name, reactivation_token
    :throws IOError: Invalid secret file
    """
    f = open(file, "r+")
    lines = [line.strip() for line in f.readlines()]
    return lines[0], int(lines[1]), lines[2], lines[3]


def update_htop_count(file: str, newcount: int):
    """
    Update the count in a HTOP file
    :param file: Path to .htop file
    :param newcount: New count for the file
    :throws IOError: Invalid secret file
    """
    secret, _, customer_name, reactivation_token = read_htop(file)
    write_htop(file, secret, newcount, customer_name, reactivation_token)
