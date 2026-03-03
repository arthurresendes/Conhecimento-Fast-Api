from passlib.context import CryptContext

CRIPTO = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")

# Função para verificar se a senha está correta
def verificar_senha(senha: str, hash_senha: str) -> bool:
    return CRIPTO.verify(senha, hash_senha)

# Gera e retorna o hash da senha em str
def gerar_hash_senha(senha: str) -> str:
    return CRIPTO.hash(senha)