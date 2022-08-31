import mysql.connector

connectDB = mysql.connector.connect(host='127.0.0.1', database='MeuDB', user='root', password='Info@1234')

if connectDB.is_connected():
    #ver informações do Servidor SQL
    db_info = connectDB.get_server_info()
    print(f'Conectado ao sevidor SQL versão {db_info}')

    # Enviar um SQL para o servidor
    cursor = connectDB.cursor();
    cursor.execute('select database();')
    linha = cursor.fetchone()

    print(f"Conectado ao Banco de Dados: {linha}")

    connectDB.close()
    print('Conexão encerrada...!!! ')


