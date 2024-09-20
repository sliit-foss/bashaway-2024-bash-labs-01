import os

db_config = {
    'host': os.getenv('MYSQL_HOST', 'mysql'),  # MySQL service name in Kubernetes
    'user': os.getenv('MYSQL_USER', 'demo_user'),
    'password': os.getenv('MYSQL_PASSWORD', 'password'),
    'database': os.getenv('MYSQL_DB', 'demo'),
}
