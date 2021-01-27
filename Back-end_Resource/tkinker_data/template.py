from faker import Faker
fake = Faker(['it_IT', 'en_US', 'ja_JP', 'zh_CN', 'en_CA', 'en_PH', 'en_TH', 'uk_UA'])
# fake = Faker(['zh_CN'])
TEMPLATES ={
    # "地理信息伪数据"
    'City' : print(fake.city()),  # 城市
    'Country': print(fake.country()),  # 国家
    'Country Code': print(fake.country_code()),  # 国家编码
    # 'Area': print(fake.district()), # 仅支持中国
    'Latitude': print(fake.latitude()),  # 地理坐标：纬度
    'Longitude': print(fake.longitude()),  # 地理坐标：经度
    'Postcode': print(fake.postcode()),  # 邮编
    # 'Province': print(fake.province()),  # 台湾，美国没有
    'Address': print(fake.address()),  # 详细地址
    'Street Address': print(fake.street_address()),  # 街道地址
    'Street Name': print(fake.street_name()),  # 街道名
    'Street Suffix': print(fake.street_suffix()),  # 街、路
    'Building NO.': print(fake.building_number()), # 楼牌号 eg：'B座'

    # "基础信息伪数据"
    'SSN': print(fake.ssn()),  # SSN号
    'Service Business': print(fake.bs()),  # 随机公司服务行业
    'Company Name': print(fake.company()),  # 随机公司名
    'Card Info': print(fake.credit_card_full()),  # 生成完整信用卡信息
    'Card NO.': print(fake.credit_card_number(card_type=None)),  # 生成信用卡号
    'Card Type': print(fake.credit_card_provider()),  # 信用卡类型
    'Card Security Code': print(fake.credit_card_security_code()),  # 信用卡安全码
    'Job': print(fake.job()),  # 职位
    'First Name': print(fake.first_name()),  # 名
    'Last Name': print(fake.last_name()),  # 姓
    'First Name(Female)': print(fake.first_name_female()),  # 女性 名
    'First Name(Male)': print(fake.first_name_male()),  # 男性 名
    'Last Name(Female)': print(fake.last_name_female()),  # 女性
    'Last Name(Male)': print(fake.last_name_male()),  # 男性
    'Full Name': print(fake.name()),  # 随机生成全名
    'Male Name': print(fake.name_male()),  # 男性全名
    'Female Name': print(fake.name_female()),  # 女性全名
    'ISDN NO.': print(fake.msisdn()),  # 移动台国际用户识别码，即移动用户的ISDN号码
    'Phone NO.': print(fake.phone_number()),  # 随机生成电话号
    'NO. Segment(Phone)': print(fake.phonenumber_prefix()),  # 随机生成手机号段如'139'

    # "个人账户信息伪数据"
    # 'Email(Company)': print(fake.ascii_company_email()),  # 随机ASCII公司邮箱名
    'Email Address': print(fake.email()),  # 邮箱

    # "网络基础信息伪数据"
    'Domain Name': print(fake.domain_name()),  # 生成域名
    'IP Address V4': print(fake.ipv4()),  # 随机IP4地址
    'IP Address V6': print(fake.ipv6()),  # 随机IP6地址
    'MAC Address': print(fake.mac_address()),  # 随机MAC地址
    'URI Address': print(fake.uri()),  # 随机URI地址
    'URL Address': print(fake.url()),  # 随机URL地址
    'User Name': print(fake.user_name()),  # 随机用户名

    # "浏览器信息伪数据"
    'User Agent': print(fake.user_agent()),  # 随机user_agent信息

    # "文件信息伪数据"
    'File Type': print(fake.file_extension()),  # 随机文件扩展名如'avi'，'txt'
    'File Name': print(fake.file_name()),  # 随机文件名（包含扩展名，不包含路径）
    'File Path': print(fake.file_path()),  # 随机文件路径（包含文件名，扩展名）
    'Mime Type': print(fake.mime_type()),  # 随机mime Type


}