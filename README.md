# Flask Web ---hmsc

> 海马商城back-end code

### MySQL

###### 一、创建数据

create database hmsc;

###### 二、创建表格/插入数据

**1.创建stat_daily_site表**

```mysql
# 切换到hmsc库
use hmsc;
# 创建表格
drop table if exists stat_daily_site;
# 搭建表格结构
create table stat_daily_site ( id int(11) unsigned not null auto_increment, date date not null comment '日期', total_pay_money decimal(10,2) not null default '0.00' comment '当日收入总额', total_member_count int(11) not null comment '会员总数', total_new_member_count int(11) not null comment '当日新增会员数', total_order_count int(11) not null comment '当日订单数', total_shared_count int(11) not null comment '分享总数', updated_time timestamp not null default current_timestamp comment '最近更新时间', created_time timestamp not null default current_timestamp comment '插入时间', primary key (id), key idx_data (date) )engine=InnoDB default charset=utf8 comment='全站日统计';
```

**2.member会员账号**

（1.）会员账号/数据库

```mysql
# 切换到hmsc库/创建表格
use hmsc;
drop table if exists `member`;
# 搭建表格结构
create table `member` (
	`id` int(11) unsigned not null auto_increment,
	`nickname` varchar(100) not null default '' comment '会员昵称',
	`mobile` varchar(20) not null default '' comment '会员手机号码',
	`sex` tinyint(1) not null default '0' comment '1:男 2:女 0:没有填写',
	`avatar` varchar(200) not null default '' comment '会员头像',
	`salt` varchar(32) not null default '' comment '登录密码的随机密钥',
	`reg_ip` varchar(100) not null default '' comment '注册ip',
	`status` tinyint(1) not null default '1' comment '1:有效 0:无效',
	`updated_time` timestamp not null default current_timestamp comment '最后一次更新时间',
	`created_time` timestamp not null default current_timestamp comment '创建时间',
	primary key (`id`)
)ENGINE=InnoDB default charset=utf8 comment='会员表';
```

（2.）生成models

> pip install flask-sqlacodegen

```python
flask-sqlacodegen 'mysql://root:password@127.0.0.1/hmsc' --tables member --outfile "common/models/member/Member.py" --flask
```

（3.）插入数据

```mysql
insert into `member` (`id`,`nickname`,`mobile`,`sex`,`avatar`,`salt`,`reg_ip`,`status`,`updated_time`,`created_time`) values (1,'BruceNick','13933746521',1,'','cF3JfH5FJfQ8B2Ba','20200429',1,'2020-04-29 11:30:30','2020-04-29 11:10:30');
```

**3.member_comments会员评论**

（1.）会员评论/数据库

```mysql
# 创表
use hmsc_db;
drop table if exists `member_comments`;
# 结构
create table `member_comments`(
	`id` int(11) unsigned not null auto_increment,
	`member_id` int(11) not null default '0' comment '会员id',
	`goods_id` varchar(200) not null default '' comment '商品id',
	`pay_order_id` int(11) not null default '0' comment '订单id',
	`score` tinyint(4) not null default '0' comment '评分',
	`content` varchar(200) not null default '' comment '评论内容',
	`created_time` timestamp not null default current_timestamp on update current_timestamp comment '创建时间',
	primary key (`id`),
	key `idx_member_id` (`member_id`)
)ENGINE=InnoDB default charset=utf8 comment='会员评论表';
```

（2.）生成models

```python
flask-sqlacodegen 'mysql://root:password@127.0.0.1/hmsc' --tables member_comments --outfile "common/models/member/MemberComment.py" --flask
```

（3.）插入数据

```mysql
insert into `member_comments` (`id`,`member_id`,`goods_id`,`pay_order_id`,`score`,`content`,`created_time`) values (1,1,'1',1,'10','好，good','2020-04-29 11:10:30');
```

