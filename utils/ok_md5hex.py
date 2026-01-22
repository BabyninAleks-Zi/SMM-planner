import hashlib


def get_md5(full_string):
    bytes_value = full_string.encode('utf-8')
    md5_hash_object = hashlib.md5(bytes_value)
    return md5_hash_object.hexdigest()


def make_sig(params, session_secret_key):
    sorted_params = sorted(params.items())
    base_string = ''
    for param_name, param_value in sorted_params:
        base_string += f'{param_name}={param_value}'
    full_string = base_string + session_secret_key
    return get_md5(full_string)