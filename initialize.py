''' Initialize environment/configuration. '''
from dotenv import dotenv_values

# Load env
env = dotenv_values('.env')

def initialize_firebase_env():
    ''' Initialize Firebase environment. '''
    firebase = {
        'service_account_key': {k: v for k, v in env.items() if k.startswith('FIREBASE.SERVICE_ACCOUNT_KEY')}
    }

    # Generate FIrebase JSON files.
    for key in firebase.keys():
        with open(f'{key}.json', 'w') as f:
            content = ''
            for k, v in firebase[key].items():
                k = k.lower()
                content += f'  "{k[k.index(key) + len(key) + 1:]}": "{v}",\n'
            content = '{\n' + content[:-2] + '\n}'
            f.write(content)


if __name__ == '__main__':
    initialize_firebase_env()