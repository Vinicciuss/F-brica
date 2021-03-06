#
SQL_DELETA_CARRO = 'delete from Carro where id = %s'
SQL_CARRO_POR_ID = 'SELECT id, marca, modelo, cor, combustivel, ano from Carro where id = %s'
SQL_USUARIO_POR_ID = 'SELECT id, nome, senha from usuario where id = %s'
SQL_ATUALIZA_CARRO = 'UPDATE Carro SET marca=%s, modelo=%s, cor=%s, combustivel=%s, ano=%s where id = %s'
SQL_BUSCA_CARROS = 'SELECT id, marca, modelo, cor, combustivel, ano  from Carro'
SQL_CRIA_CARRO = 'INSERT into Carro (marca, modelo, cor, combustivel, ano) values (%s, %s, %s, %s, %s) RETURNING id'
SQL_CRIA_USUARIO = 'INSERT into usuario (id, nome, senha) values (%s, %s, %s)'
SQL_ATUALIZA_USUARIO = 'UPDATE usuario SET id=%s, nome=%s, senha=%s where id = %s'
SQL_AUTENTICAR_USUARIO = 'SELECT id, nome, senha from usuario where id = %s AND senha = %s'