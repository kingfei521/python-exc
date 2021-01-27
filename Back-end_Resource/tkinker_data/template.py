import random

from faker import Faker
fake = Faker(['it_IT', 'en_US', 'ja_JP', 'zh_CN',
              'en_CA', 'en_PH', 'en_TH', 'uk_UA'])
# fake = Faker(['zh_CN'])

TEMPLATES = (
    'Id NO.',
    'First Name',  # 名
    'Last Name',  # 姓
    'Email Address',  # 邮箱
    'Gender',
    'IP Address V4',  # 随机IP4地址
    # "地理信息伪数据"
    'City',  # 城市
    'Country',  # 国家
    'Country Code',  # 国家编码
    # 'Area'district, # 仅支持中国
    'Latitude',  # 地理坐标：纬度
    'Longitude',  # 地理坐标：经度
    'Postcode',  # 邮编
    # 'Province'province,  # 台湾，美国没有
    'Address',  # 详细地址
    'Street Address',  # 街道地址
    'Street Name',  # 街道名
    'Street Suffix',  # 街、路
    'Building NO.',  # 楼牌号 eg：'B座'

    # "基础信息伪数据"
    'SSN',  # SSN号
    'Service Business',  # 随机公司服务行业
    'Company Name',  # 随机公司名
    'Card Info',  # 生成完整信用卡信息
    'Card NO.',  # 生成信用卡号
    'Card Type',  # 信用卡类型
    'Card Security Code',  # 信用卡安全码
    'Job',  # 职位


    'First Name(Female)',  # 女性 名
    'First Name(Male)',  # 男性 名
    'Last Name(Female)',  # 女性
    'Last Name(Male)',  # 男性
    'Full Name',  # 随机生成全名
    'Male Name',  # 男性全名
    'Female Name',  # 女性全名
    'ISDN NO.',  # 移动台国际用户识别码，即移动用户的ISDN号码
    'Phone NO.',  # 随机生成电话号
    'NO. Segment(Phone)',  # 随机生成手机号段如'139'

    # "网络基础信息伪数据"
    'Domain Name',  # 生成域名

    'IP Address V6',  # 随机IP6地址
    'MAC Address',  # 随机MAC地址
    'URI Address',  # 随机URI地址
    'URL Address',  # 随机URL地址
    'User Name',  # 随机用户名

    # "浏览器信息伪数据"
    'User Agent',  # 随机user_agent信息

    # "文件信息伪数据"
    'File Type',  # 随机文件扩展名如'avi'，'txt'
    'File Name',  # 随机文件名（包含扩展名，不包含路径）
    'File Path',  # 随机文件路径（包含文件名，扩展名）
    'Mime Type',  # 随机mime Type
)


def data_generator(field):
    if field == 'Id NO.':
        return fake.random_int()
    if field == 'First Name':
        return fake.first_name()
    if field == 'Last Name':
        return fake.last_name()
    if field == 'Email Address':
        return fake.email()
    if field == 'Gender':
        return random.choice(['Female', 'Male', 'Non-binary'])
    if field == 'IP Address V4':
        return fake.ipv4()

    if field == 'City':
        return fake.city(),  # 城市
    if field == 'Country':
        return fake.country(),  # 国家
    if field == 'Country Code':
        return fake.country_code(),  # 国家编码
    # 'Area': fake.district(), # 仅支持中国
    if field == 'Latitude':
        return fake.latitude(),  # 地理坐标：纬度
    if field == 'Longitude':
        return fake.longitude(),  # 地理坐标：经度
    if field == 'Postcode':
        return fake.postcode(),  # 邮编
    # 'Province': return fake.province(),  # 台湾，美国没有
    if field == 'Address':
        return fake.address(),  # 详细地址
    if field == 'Street Address':
        return fake.street_address(),  # 街道地址
    if field == 'Street Name':
        return fake.street_name(),  # 街道名
    if field == 'Street Suffix':
        return fake.street_suffix(),  # 街、路
    if field == 'Building NO.':
        return fake.building_number(),  # 楼牌号 eg：'B座'

    # "基础信息伪数据"
    if field == 'SSN':
        return fake.ssn(),  # SSN号
    if field == 'Service Business':
        return fake.bs(),  # 随机公司服务行业
    if field == 'Company Name':
        return fake.company(),  # 随机公司名
    if field == 'Card Info':
        return fake.credit_card_full(),  # 生成完整信用卡信息
    if field == 'Card NO.':
        return fake.credit_card_number(card_type=None),  # 生成信用卡号
    if field == 'Card Type':
        return fake.credit_card_provider(),  # 信用卡类型
    if field == 'Card Security Code':
        return fake.credit_card_security_code(),  # 信用卡安全码
    if field == 'Job':
        return fake.job(),  # 职位

    if field == 'First Name(Female)':
        return fake.first_name_female(),  # 女性 名
    if field == 'First Name(Male)':
        return fake.first_name_male(),  # 男性 名
    if field == 'Last Name(Female)':
        return fake.last_name_female(),  # 女性
    if field == 'Last Name(Male)':
        return fake.last_name_male(),  # 男性
    if field == 'Full Name':
        return fake.name(),  # 随机生成全名
    if field == 'Male Name':
        return fake.name_male(),  # 男性全名
    if field == 'Female Name':
        return fake.name_female(),  # 女性全名
    if field == 'ISDN NO.':
        return fake.msisdn(),  # 移动台国际用户识别码，即移动用户的ISDN号码
    if field == 'Phone NO.':
        return fake.phone_number(),  # 随机生成电话号
    if field == 'NO. Segment(Phone)':
        return fake.phonenumber_prefix(),  # 随机生成手机号段如'139'

    # "网络基础信息伪数据"
    if field == 'Domain Name':
        return fake.domain_name(),  # 生成域名

    if field == 'IP Address V6':
        return fake.ipv6(),  # 随机IP6地址
    if field == 'MAC Address':
        return fake.mac_address(),  # 随机MAC地址
    if field == 'URI Address':
        return fake.uri(),  # 随机URI地址
    if field == 'URL Address':
        return fake.url(),  # 随机URL地址
    if field == 'User Name':
        return fake.user_name(),  # 随机用户名

    # "浏览器信息伪数据"
    if field == 'User Agent':
        return fake.user_agent(),  # 随机user_agent信息

    # "文件信息伪数据"
    if field == 'File Type':
        return fake.file_extension(),  # 随机文件扩展名如'avi'，'txt'
    if field == 'File Name':
        return fake.file_name(),  # 随机文件名（包含扩展名，不包含路径）
    if field == 'File Path':
        return fake.file_path(),  # 随机文件路径（包含文件名，扩展名）
    if field == 'Mime Type':
        return fake.mime_type(),  # 随机mime Type
