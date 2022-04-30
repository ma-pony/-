 
## 事务隔离级别

### 可序列化，串行 Serializable
无问题

### 可重复读 Repeatable Read
默认的隔离级别
可能发生幻读问题
更新数据时不仅会对数据加行级锁，还会增加GAP lock 


#### 为什么默认是可重复读？

MySQL早期只有statement这一种binlog格式
以下两种隔离级别可能会遇到bug：
已有数据a=2,b=1
同时执行两个事物AB,
A1: UPDATE t1 SET a=1 WHERE b=2;
B1: UPDATE t1 SET b=2 WHERE b=1;
B2: COMMIT;
A2: COMMIT;
A2: SELECT * FROM t1;
此时主数据库数据为a=2,b=2
此时的statement binlog为：
UPDATE t1 SET b=2 WHERE b=1; UPDATE t1 SET a=1 WHERE b=2;
从数据库执行binlog文件，从数据库数据为a=1,b=2


### 提交读 Read Committed
可能发生幻读，不可重复读问题

### 未提交读 Read Uncommitted
可能发生脏读，幻读，不可重复读问题
