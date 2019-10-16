CREATE USER 'replica'@'%' IDENTIFIED BY 'acilper';
GRANT REPLICATION SLAVE ON *.* TO 'replica'@'%';
