# coding:utf8
__author__ = 'syx'

# CMDB数据中心资产管理

# 维保单位信息
maintenance_group_choice = (
    (u'szsm', u'神州数码'),
    (u'zj', u'中集'),
)

# 资产状态
asset_status_choices = (
    (u'在用', u'在用'),
    (u'借出', u'借出'),
    (u'维修', u'维修'),
    (u'闲置', u'闲置'),
    (u'出库', u'出库'),
    (u'报废', u'报废'),
)

# 资产来源
asset_befrom_choices = (
    (u'借用', u'借用'),
    (u'租用', u'租用'),
    (u'自购', u'自购'),
    (u'其他', u'其他'),
)

# 资产类型
asset_type_choices = (
    (u'服务器', u'服务器'),
    (u'路由', u'路由'),
    (u'交换机', u'交换机'),
    (u'防火墙', u'防火墙'),
    (u'存储设备', u'存储设备'),
    (u'小型机', u'小型机'),
    #(u'ups', u'ups'),
    # 小型机
)


# 工具类型
device_type_choices = (
    (u'维修工具', u'维修工具'),
    (u'网线', u'网线'),
    (u'光纤', u'光纤'),
    (u'模块', u'模块'),
    (u'连接线', u'连接线'),
    (u'其他工具', u'其他工具'),
)
#产品型号
product_type_choices = (
    (u'十字螺丝刀', u'十字螺丝刀'),
    (u'一字螺丝刀', u'一字螺丝刀'),
    (u'平口钳', u'平口钳'),
    (u'尖嘴钳', u'尖嘴钳'),
    (u'斜口钳', u'斜口钳'),
    (u'套筒扳手', u'套筒扳手'),
    (u'开口扳手', u'开口扳手'),
    (u'力矩加力杆', u'力矩加力杆'),
    (u'梅花扳手', u'梅花扳手'),
    (u'万用表', u'万用表'),
    (u'电流表', u'电流表'),
    (u'吸尘器', u'吸尘器'),
    (u'便携式起重机', u'便携式起重机'),
    (u'KVM连接线', u'KVM连接线'),
    (u'CONSOL连接线', u'CONSOL连接线'),
    (u'USB转COM连接线', u'USB转COM连接线'),
    (u'千兆网线', u'千兆网线'),
    (u'万兆网线', u'万兆网线'),
    (u'单模千兆光纤FC-FC', u'单模千兆光纤FC-FC'),
    (u'单模千兆光纤LC-FC', u'单模千兆光纤LC-FC'),
    (u'单模千兆光纤LC-LC', u'单模千兆光纤LC-LC'),
    (u'单模千兆光纤LC-ST', u'单模千兆光纤LC-ST'),
    (u'单模千兆光纤SC-LC', u'单模千兆光纤SC-LC'),
    (u'单模千兆光纤SC-SC方头', u'单模千兆光纤SC-SC方头'),
    (u'单模千兆光纤SC-SL', u'单模千兆光纤SC-SL'),
    (u'单模千兆光纤ST-SC', u'单模千兆光纤ST-SC'),
    (u'单模千兆光纤ST-ST', u'单模千兆光纤ST-ST'),

    (u'多模万兆光纤FC-FC', u'多模万兆光纤FC-FC'),
    (u'多模万兆光纤LC-FC', u'多模万兆光纤LC-FC'),
    (u'多模万兆光纤LC-LC', u'多模万兆光纤LC-LC'),
    (u'多模万兆光纤LC-ST', u'多模万兆光纤LC-ST'),
    (u'多模万兆光纤SC-LC', u'多模万兆光纤SC-LC'),
    (u'多模万兆光纤SC-SC方头', u'多模万兆光纤SC-SC方头'),
    (u'多模万兆光纤SC-SL', u'多模万兆光纤SC-SL'),
    (u'多模万兆光纤ST-SC', u'多模万兆光纤ST-SC'),
    (u'多模万兆光纤ST-ST', u'多模万兆光纤ST-ST'),

    (u'单模万兆光纤FC-FC', u'单模万兆光纤FC-FC'),
    (u'单模万兆光纤LC-FC', u'单模万兆光纤LC-FC'),
    (u'单模万兆光纤LC-LC', u'单模万兆光纤LC-LC'),
    (u'单模万兆光纤LC-ST', u'单模万兆光纤LC-ST'),
    (u'单模万兆光纤SC-LC', u'单模万兆光纤SC-LC'),
    (u'单模万兆光纤SC-SC方头', u'单模万兆光纤SC-SC方头'),
    (u'单模万兆光纤SC-SL', u'单模万兆光纤SC-SL'),
    (u'单模万兆光纤ST-SC', u'单模万兆光纤ST-SC'),
    (u'单模万兆光纤ST-ST', u'单模万兆光纤ST-ST'),

    (u'多模千兆光纤FC-FC', u'多模千兆光纤FC-FC'),
    (u'多模千兆光纤LC-FC', u'多模千兆光纤LC-FC'),
    (u'多模千兆光纤LC-LC', u'多模千兆光纤LC-LC'),
    (u'多模千兆光纤LC-ST', u'多模千兆光纤LC-ST'),
    (u'多模千兆光纤SC-LC', u'多模千兆光纤SC-LC'),
    (u'多模千兆光纤SC-SC方头', u'多模千兆光纤SC-SC方头'),
    (u'多模千兆光纤SC-SL', u'多模千兆光纤SC-SL'),
    (u'多模千兆光纤ST-SC', u'多模千兆光纤ST-SC'),
    (u'多模千兆光纤ST-ST', u'多模千兆光纤ST-ST'),


    (u'FSP', u'FSP'),
    (u'千兆模块', u'千兆模块'),
    (u'万兆模块', u'万兆模块'),

)

# 存储、磁带表
storage_type_choices = (
    (u'磁带机', u'磁带机'),
    (u'存储主机', u'存储主机'),
    (u'磁盘阵列', u'磁盘阵列'),
    (u'光纤交换机', u'光纤交换机'),
    (u'其他', u'其他'),
)
tape_type_choices = (
    (u'清洗带', u'清洗带'),
    (u'数据带', u'数据带'),
    (u'其他', u'其他'),
)
tape_model_choices = (
    (u'LT01', u'LT01'),
    (u'LT02', u'LT02'),
    (u'LT03', u'LT03'),
    (u'LT04', u'LT04'),
    (u'LT05', u'LT05'),
    (u'HP DAT 72', u'HP DAT 72'),
    (u'IBM DAT 160', u'IBM DAT 160'),
    (u'IBM TEST TAPE', u'IBM TEST TAPE'),
    (u'IBM 清洗带', u'IBM 清洗带'),
)
tape_status_choices = (
    (u'磁带机', u'磁带机'),
    (u'保险柜', u'保险柜'),
    (u'报废', u'报废'),
    (u'出库', u'出库'),
)


# Host表
host_type_choices = (
    (u'小型机', u'小型机'),
    (u'pc_server', u'pc_server'),
)

# NetworkDevice表
network_choices = (
    (u'交换机', u'交换机'),
    (u'防火墙', u'防火墙'),
    (u'路由器', u'路由器'),
    (u'其它', u'其它'),
)

# Storage表



# Tape表



# Tool表



# Equipment表
equipment_choice = (
    (u'空调设备', u'空调设备'),
    (u'消防设备', u'消防设备'),
    (u'配电柜', u'配电柜'),
    (u'UPS', u'UPS'),
    (u'发电机', u'发电机'),
    (u'蓄电池', u'蓄电池'),
    (u'机柜', u'机柜'),
    (u'保险柜', u'保险柜'),
    (u'其它', u'其它'),
)


# Software表
# 资产来源
Asset_source_choices = (
    (u'借用', u'借用'),
    (u'租用', u'租用'),
    (u'自购', u'自购'),
    (u'其他', u'其他'),
)

# 使用状态
Use_status_choices = (
    (u'在用', u'在用'),
    (u'闲置', u'闲置'),
)

# 设备存放位置
datacenter_choices = (
    (u'yz',u'亦庄亚太中立'),
    (u'yj',u'燕郊光环新网'),
    (u'lfxx',u'廊坊信息大厦'),
    (u'lfxz',u'廊坊新智机房'),
    (u'other',u'其他'),
)
zone_choices = (
    (u'A', u'A'), (u'B', u'B'), (u'C', u'C'), (u'D', u'D'), (u'E', u'E'), (u'F', u'F'),
    (u'G', u'G'), (u'H', u'H'), (u'I', u'I'), (u'J', u'J'), (u'K', u'K'), (u'L', u'L'),
)
cabinet_choices = (
    (1, u'1'), (2, u'2'), (3, u'3'), (4, u'4'), (5, u'5'), (6, u'6'),
    (7, u'7'), (8, u'8'), (9, u'9')
)
rack_unit_choices = (
    (1, u'1'), (2, u'2'), (3, u'3'), (4, u'4'), (5, u'5'), (6, u'6'),
    (7, u'7'), (8, u'8'), (9, u'9'), (10, u'10'), (11, u'11'), (12, u'12'),
    (13, u'13'), (14, u'14'), (15, u'15'), (16, u'16'), (17, u'17'), (18, u'18'),
    (19, u'19'), (20, u'20'), (21, u'21'), (22, u'22'), (23, u'23'), (24, u'24'),
    (25, u'25'), (26, u'26'), (27, u'27'), (28, u'28'), (29, u'29'), (30, u'30'),
    (31, u'31'), (32, u'32'), (33, u'33'), (34, u'34'), (35, u'35'), (36, u'36'),
    (37, u'37'), (38, u'38'), (39, u'39'), (40, u'40'), (41, u'41'), (42, u'42'),

)

#备件表
spare_part_type_choices = (
    (u'内存', u'内存'),
    (u'硬盘', u'硬盘'),
)

# disk nic ram cpu

disk_iface_choice = (
        ('SATA', 'SATA'),
        ('SAS', 'SAS'),
        ('SCSI', 'SCSI'),
        ('SSD', 'SSD'),
)